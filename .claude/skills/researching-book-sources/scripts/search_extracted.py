#!/usr/bin/env python3
"""抽出済みの書籍本文から語を探し、ページ番号を付けて返す。

research/extracted/<出典ID>.<変換器>.txt は1冊で数十万字あり、
全文を読むと文脈窓を使い切る。この道具は該当する行だけを、
その行が属するページ番号とともに返す。

使い方:
    python search_extracted.py SRC-REVIEW-001 レビュー 観点
    python search_extracted.py all 静的解析 --context 2
    python search_extracted.py SRC-TEST-002 境界値 --all-terms --max 10

出力の形:
    SRC-REVIEW-001 p.87 L2431 | 指摘は観点と根拠をそろえて書く
"""

import argparse
import re
import sys
from pathlib import Path

EXTRACTED_DIR = Path("research/extracted")
# tools/extract_pdf.py の出力は変換器ごとにページの区切り方が違う。
#   pypdf   : "===== PAGE 12 =====" という行を挟む
#   poppler : 改ページ文字（\f）をページの末尾に置く
PAGE_MARKER = re.compile(r"^=====\s*PAGE\s+(\d+)\s*=====\s*$")
PAGE_BREAK = "\f"
# poppler の方が段組の復元がよいため既定にする。pypdf は控えとして残す。
VARIANTS = ("poppler", "pypdf")


def find_text_file(source_id: str, variant: str) -> Path | None:
    """出典IDと変換器名から抽出テキストのパスを返す。無ければ None を返す。"""
    candidate = EXTRACTED_DIR / f"{source_id}.{variant}.txt"
    if candidate.exists():
        return candidate
    for fallback in VARIANTS:
        candidate = EXTRACTED_DIR / f"{source_id}.{fallback}.txt"
        if candidate.exists():
            return candidate
    return None


def available_source_ids() -> list[str]:
    """抽出ずみの出典IDを並べて返す。"""
    ids = set()
    for path in EXTRACTED_DIR.glob("*.txt"):
        ids.add(path.name.split(".")[0])
    return sorted(ids)


def read_pages(path: Path) -> tuple[list[str], list[int]]:
    """本文を行に分け、行ごとのページ番号を添えて返す。

    変換器によってページの区切り方が違うため、ここで吸収する。
    """
    text = path.read_text(encoding="utf-8", errors="replace")

    if PAGE_BREAK in text:
        # poppler: 改ページ文字がページの末尾に置かれる。
        # 区切りの前の塊が1ページ目になる。
        lines = []
        page_of_line = []
        for page, chunk in enumerate(text.split(PAGE_BREAK), start=1):
            for line in chunk.splitlines():
                lines.append(line)
                page_of_line.append(page)
        return lines, page_of_line

    # pypdf: ページ番号を書いた行が挟まる。
    lines = text.splitlines()
    page_of_line = []
    page = 0
    for line in lines:
        marker = PAGE_MARKER.match(line)
        if marker:
            page = int(marker.group(1))
        page_of_line.append(page)
    return lines, page_of_line


def search_one(path: Path, source_id: str, terms: list[str],
               all_terms: bool, context: int) -> list[str]:
    """1冊分を走査し、整形ずみの行の一覧を返す。"""
    lines, page_of_line = read_pages(path)

    hits = []
    for index, line in enumerate(lines):
        if PAGE_MARKER.match(line):
            continue
        found = [term for term in terms if term in line]
        if not found:
            continue
        if all_terms and len(found) != len(terms):
            continue

        head = f"{source_id} p.{page_of_line[index]} L{index + 1}"
        if context == 0:
            hits.append(f"{head} | {line.strip()}")
            continue

        start = max(0, index - context)
        end = min(len(lines), index + context + 1)
        block = []
        for near in range(start, end):
            if PAGE_MARKER.match(lines[near]):
                continue
            mark = ">" if near == index else " "
            block.append(f"  {mark} {lines[near].strip()}")
        hits.append(head + "\n" + "\n".join(block))
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(
        description="抽出済みの書籍本文から語を探し、ページ番号を付けて返す")
    parser.add_argument("source_id",
                        help="出典ID（例: SRC-REVIEW-001）。all で抽出ずみ全冊")
    parser.add_argument("terms", nargs="+", help="探す語。1つ以上")
    parser.add_argument("--all-terms", action="store_true",
                        help="すべての語を含む行だけを返す。既定はいずれかを含む行")
    parser.add_argument("--context", type=int, default=0,
                        help="前後に何行を添えるか。既定は0")
    parser.add_argument("--max", type=int, default=40,
                        help="返す件数の上限。既定は40")
    parser.add_argument("--variant", choices=VARIANTS, default="poppler",
                        help="使う変換器。既定は poppler")
    args = parser.parse_args()

    if not EXTRACTED_DIR.is_dir():
        print(f"{EXTRACTED_DIR} が無い。"
              "リポジトリの根で実行し、先に tools/extract_pdf.py を通す。",
              file=sys.stderr)
        return 1

    if args.source_id == "all":
        source_ids = available_source_ids()
    else:
        source_ids = [args.source_id]

    if not source_ids:
        print(f"{EXTRACTED_DIR} に抽出テキストが無い。"
              "先に tools/extract_pdf.py を通す。", file=sys.stderr)
        return 1

    results = []
    missing = []
    for source_id in source_ids:
        path = find_text_file(source_id, args.variant)
        if path is None:
            missing.append(source_id)
            continue
        results.extend(
            search_one(path, source_id, args.terms, args.all_terms, args.context))

    for source_id in missing:
        print(f"未抽出: {source_id}。tools/extract_pdf.py で取り出す。",
              file=sys.stderr)

    shown = results[:args.max]
    for line in shown:
        print(line)

    searched = len(source_ids) - len(missing)
    print(f"\n該当 {len(results)} 件。表示 {len(shown)} 件。"
          f"探した冊数 {searched}。", file=sys.stderr)
    if len(results) > len(shown):
        print("語を増やすか --all-terms を付けて絞る。", file=sys.stderr)

    # 1冊も読めなかったときは失敗として返す。
    # 呼ぶ側が「該当0件」と「抽出していない」を区別できるようにするためである。
    return 1 if searched == 0 else 0


if __name__ == "__main__":
    sys.exit(main())

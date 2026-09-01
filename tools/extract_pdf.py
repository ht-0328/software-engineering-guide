#!/usr/bin/env python3
"""参考書のPDFから本文を取り出す。

抽出の中身は姉妹リポジトリ engineering-docs-standard が持つ。このスクリプトは
その入口であり、次の3つだけを行う。

1. 出典IDとファイル名の対応を research/sources.md の表から読む。
2. 入力を references/、出力を research/extracted/ に向ける。
3. 向こうの extract_pdf を動かす。

出典IDの採番は research/sources.md が一次情報である。ここには写しを持たない。

Dockerで動かす。ホストには何もインストールしない。

    docker run --rm --user "$(id -u):$(id -g)" -v "$PWD:/w" -w /w edocs-tools python tools/extract_pdf.py

引数にPDFのファイル名を渡すと、その本だけを処理する。省略すると全部を処理する。
出力は <出典ID>.pypdf.txt、<出典ID>.poppler.txt、<出典ID>.info.txt の3つである。
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STANDARD_TOOLS = ROOT / "engineering-docs-standard" / "tools"
CATALOG = ROOT / "research" / "sources.md"
SRC_DIR = ROOT / "references"
OUT_DIR = ROOT / "research" / "extracted"

# 出典カタログの表の行。1列目が出典ID、4列目がファイル名である。
CATALOG_ROW = re.compile(r"^\|\s*`(SRC-[A-Z]+-\d+)`\s*\|[^|]*\|[^|]*\|\s*`([^`]+\.pdf)`\s*\|")


def read_source_ids() -> dict[str, str]:
    """出典カタログから {ファイル名: 出典ID} を読む。"""
    ids: dict[str, str] = {}
    for line in CATALOG.read_text(encoding="utf-8").splitlines():
        match = CATALOG_ROW.match(line)
        if match:
            ids[match.group(2)] = match.group(1)
    return ids


def main(argv: list[str]) -> int:
    if not (STANDARD_TOOLS / "extract_pdf.py").is_file():
        print(
            "サブモジュールが取得されていない。"
            "`git submodule update --init --recursive` を実行する",
            file=sys.stderr,
        )
        return 2

    source_ids = read_source_ids()
    if not source_ids:
        print(f"出典カタログから対応を読めなかった: {CATALOG}", file=sys.stderr)
        return 2

    # カタログに載っていないPDFは、出典IDが無いまま抽出される。先に知らせる。
    unlisted = sorted(p.name for p in SRC_DIR.glob("*.pdf") if p.name not in source_ids)
    for name in unlisted:
        print(f"出典カタログに載っていない: {name}", file=sys.stderr)

    sys.path.insert(0, str(STANDARD_TOOLS))
    import extract_pdf  # noqa: PLC0415  入口として、取得できたあとに読み込む

    extract_pdf.SRC_DIR = SRC_DIR
    extract_pdf.OUT_DIR = OUT_DIR
    extract_pdf.SOURCE_IDS = source_ids
    return extract_pdf.main(argv)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

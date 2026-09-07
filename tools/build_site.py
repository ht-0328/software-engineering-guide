#!/usr/bin/env python3
"""docs/ の Markdown から、Zensical で公開用のサイトを作る。

下ごしらえの中身は姉妹リポジトリ engineering-docs-standard が持つ。このスクリプトは
その入口であり、次の4つだけを行う。

1. docs/ を build/zensical/ に写し、docs/ の外を指すリンクを GitHub の URL に直す。
   Zensical は docs_dir の中だけをサイトにするため、この写しが要る。
2. 写した側から docs/adr/ を除き、そこへ向いたリンクを GitHub の URL に直す。
   決定記録はこのリポジトリ自身の記録であり、公開サイトの読者向けではない。
3. 図を描く Mermaid とその起動スクリプトを、写した側に同梱する。
4. zensical.toml を渡して zensical build を動かす。

Dockerで動かす。ホストには何もインストールしない。

    bash engineering-docs-standard/tools/fetch_vendor.sh
    docker run --rm --user "$(id -u):$(id -g)" -v "$PWD:/w" -w /w \
      edocs-zensical python tools/build_site.py

引数はそのまま zensical に渡す。`--strict` を付けると、警告1件で失敗する。
"""

from __future__ import annotations

import os
import posixpath
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STANDARD_TOOLS = ROOT / "engineering-docs-standard" / "tools"
SITE = ROOT / "site"

# docs/ の外を指すリンクの差し替え先。fork したときはここを書き換える。
REPO_URL = "https://github.com/ht-0328/software-engineering-guide"
REPO_BRANCH = "master"

# 公開サイトに出さない docs/ の下のディレクトリ。docs/ から見た位置で書く。
# 決定記録はこのリポジトリ自身の構成を決めた記録であり、手引きの読者向けではない。
# リポジトリの中には残す。GitHub 上で読めればよい。
UNPUBLISHED = ("adr",)

# Markdown のリンク。`../` で始まるものはサブモジュール側が先に処理する。
# ここが拾うのは、docs/ の中を指したまま公開対象から外れたものである。
PAGE_LINK = re.compile(r"\]\((?!/|\w+:)([^)\s#]+\.md)(#[^)\s]*)?\)")


def drop_unpublished(base) -> int:
    """写した側から UNPUBLISHED のディレクトリを外し、リンクを差し替える。

    サブモジュールの stage() は docs/ の Markdown をすべて写す。ここで外さないと、
    `nav` に載せなくてもページは生成され、検索にも出る。**公開そのものを止める。**

    外したページを指すリンクは、そのままでは切れる。GitHub の URL に差し替えて、
    読者がリポジトリ側で読めるようにする。docs/ の外を指すリンクの扱いと同じである。

    戻り値は、外したページの数である。
    """
    removed = 0
    for name in UNPUBLISHED:
        target = base.BUILD / name
        if not target.is_dir():
            continue
        removed += len(list(target.rglob("*.md")))
        shutil.rmtree(target)

    if removed == 0:
        return 0

    for page in sorted(base.BUILD.rglob("*.md")):
        rel = page.relative_to(base.BUILD).as_posix()
        text = page.read_text(encoding="utf-8")
        replaced = rewrite_to_repo(text, posixpath.dirname(rel), base)
        if replaced != text:
            page.write_text(replaced, encoding="utf-8")

    return removed


def rewrite_to_repo(text: str, base_dir: str, base) -> str:
    """公開対象から外れたページを指すリンクを、GitHub の URL に直す。

    コードブロックの中は書き換えない。書き換えると、例として載せたリンクが変わる。
    """
    out: list[str] = []
    in_fence = False

    for line in text.splitlines(keepends=True):
        if base.FENCE.match(line):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        out.append(PAGE_LINK.sub(lambda m: to_repo_url(m, base_dir, base), line))

    return "".join(out)


def to_repo_url(match: re.Match[str], base_dir: str, base) -> str:
    """リンク1つを見て、公開対象から外れた先なら URL に差し替える。"""
    path = match.group(1)
    anchor = (match.group(2) or "").lstrip("#")

    inside_docs = posixpath.normpath(posixpath.join(base_dir, path))
    if not any(inside_docs.startswith(f"{name}/") for name in UNPUBLISHED):
        return match.group(0)

    return f"]({base.repo_url(posixpath.join('docs', inside_docs), anchor)})"


def main(argv: list[str]) -> int:
    if not (STANDARD_TOOLS / "build_site_zensical.py").is_file():
        print(
            "サブモジュールが取得されていない。"
            "`git submodule update --init --recursive` を実行する",
            file=sys.stderr,
        )
        return 2

    sys.path.insert(0, str(STANDARD_TOOLS))
    import build_site_zensical as base  # noqa: PLC0415  入口として、取得できたあとに読み込む

    # 下ごしらえの向き先を、このリポジトリに合わせる。
    base.ROOT = ROOT
    base.DOCS = ROOT / "docs"
    base.BUILD = ROOT / "build" / "zensical"
    base.SITE = SITE
    base.DIAGRAMS = ROOT / "diagrams" / "export"
    base.REPO_URL = REPO_URL
    base.REPO_BRANCH = REPO_BRANCH

    # Mermaid の本体と起動スクリプトは、サブモジュール側に置いたものを使う。
    # 取得は engineering-docs-standard/tools/fetch_vendor.sh が行う。
    base.VENDOR = STANDARD_TOOLS / "vendor"
    base.OVERRIDES = STANDARD_TOOLS / "zensical"

    # 姉妹リポジトリは、比較用であることの断り書きを最初のページに入れる。
    # このリポジトリのサイトは比較用ではないため、入れない。
    base.add_notice = lambda text: text

    count, warnings = base.stage()
    count -= drop_unpublished(base)
    for message in warnings:
        print(f"警告: {message}")
    print(f"下ごしらえしたページ: {count}")

    # zensical の出力と混ざらないよう、ここまでの表示を先に流す。
    sys.stdout.flush()

    # zensical.toml が `mdslug.toc_slugify` を名前で読み込む。
    # サブモジュールの tools/ を import の対象に入れておかないと、そこで失敗する。
    env = dict(os.environ)
    existing = env.get("PYTHONPATH")
    paths = [str(STANDARD_TOOLS)] + ([existing] if existing else [])
    env["PYTHONPATH"] = os.pathsep.join(paths)

    result = subprocess.run(
        ["zensical", "build", "-f", str(ROOT / "zensical.toml"), *argv],
        cwd=ROOT,
        env=env,
    )
    if result.returncode != 0:
        return result.returncode

    print(f"生成したページ: {len(list(SITE.rglob('index.html')))}")
    print(f"出力先: {SITE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

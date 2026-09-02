#!/usr/bin/env python3
"""docs/ の Markdown から、Zensical で公開用のサイトを作る。

下ごしらえの中身は姉妹リポジトリ engineering-docs-standard が持つ。このスクリプトは
その入口であり、次の3つだけを行う。

1. docs/ を build/zensical/ に写し、docs/ の外を指すリンクを GitHub の URL に直す。
   Zensical は docs_dir の中だけをサイトにするため、この写しが要る。
2. 図を描く Mermaid とその起動スクリプトを、写した側に同梱する。
3. zensical.toml を渡して zensical build を動かす。

Dockerで動かす。ホストには何もインストールしない。

    bash engineering-docs-standard/tools/fetch_vendor.sh
    docker run --rm --user "$(id -u):$(id -g)" -v "$PWD:/w" -w /w \
      edocs-zensical python tools/build_site.py

引数はそのまま zensical に渡す。`--strict` を付けると、警告1件で失敗する。
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STANDARD_TOOLS = ROOT / "engineering-docs-standard" / "tools"
SITE = ROOT / "site"

# docs/ の外を指すリンクの差し替え先。fork したときはここを書き換える。
REPO_URL = "https://github.com/ht-0328/software-engineering-guide"
REPO_BRANCH = "master"


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

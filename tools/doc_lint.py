#!/usr/bin/env python3
"""このリポジトリの文書を検査する。

検査の中身は姉妹リポジトリ engineering-docs-standard が持つ。このスクリプトは
その入口であり、次の2つだけを行う。

1. 基準の設定（engineering-docs-standard/.doclint.yml）に、このリポジトリの
   差分（./.doclint.yml）を重ねる。
2. 対象の起点をこのリポジトリに向けたうえで、向こうの doc_lint を動かす。

ルールの定義を写して持たない。写しは、直した側だけが新しくなるためである。

Dockerで動かす。ホストには何もインストールしない。

    docker run --rm --user "$(id -u):$(id -g)" -v "$PWD:/w" -w /w edocs-tools python tools/doc_lint.py

引数はそのまま向こうへ渡す。ファイルを指定すると、その file だけを検査する。
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
STANDARD = ROOT / "engineering-docs-standard"
STANDARD_TOOLS = STANDARD / "tools"


def merge(base: dict, overlay: dict) -> dict:
    """overlay を base に重ねる。辞書は再帰的に併合し、それ以外は置き換える。"""
    result = dict(base)
    for key, value in overlay.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = merge(result[key], value)
        else:
            result[key] = value
    return result


def main(argv: list[str]) -> int:
    base_path = STANDARD / ".doclint.yml"
    if not base_path.is_file():
        print(
            "サブモジュールが取得されていない。"
            "`git submodule update --init --recursive` を実行する",
            file=sys.stderr,
        )
        return 2

    base = yaml.safe_load(base_path.read_text(encoding="utf-8"))
    overlay = yaml.safe_load((ROOT / ".doclint.yml").read_text(encoding="utf-8")) or {}
    config = merge(base, overlay)

    sys.path.insert(0, str(STANDARD_TOOLS))
    import doc_lint  # noqa: PLC0415  入口として、取得できたあとに読み込む

    # 検査の起点をこのリポジトリに向ける。既定ではサブモジュール側を見てしまう。
    doc_lint.ROOT = ROOT

    with tempfile.NamedTemporaryFile("w", suffix=".yml", encoding="utf-8") as handle:
        yaml.safe_dump(config, handle, allow_unicode=True, sort_keys=False)
        handle.flush()
        sys.argv = [sys.argv[0], "--config", handle.name, *argv]
        return doc_lint.main()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

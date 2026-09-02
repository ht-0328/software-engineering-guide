#!/usr/bin/env bash
#
# このリポジトリ専用の許可リストで Antigravity（agy）を動かす。
#
# agy の許可リストは、個人のグローバル設定 ~/.gemini/antigravity-cli/settings.json
# にしか置けない。そこを書き換えると、このリポジトリ以外の作業にも同じ許可が及ぶ。
# そこで、HOME だけを差し替えた重ね合わせを build/agy-home に作り、
# 設定ファイルにはリポジトリの .agents/permissions.json を使う。
#
# 認証・会話履歴・スキルは、実体への symlink で共有する。**複製は作らない。**
# 差し替えるのは settings.json 1つだけである。
#
# 使い方（引数はそのまま agy へ渡す）
#   bash tools/agy.sh --output-format text --print "調べてほしいこと"
#
# 終了コードは agy のものをそのまま返す。

set -euo pipefail

REPO=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
SRC="${HOME}/.gemini/antigravity-cli"
OVERLAY="${REPO}/build/agy-home"
PERMISSIONS="${REPO}/.agents/permissions.json"

if ! command -v agy > /dev/null 2>&1; then
  echo "agy が PATH に無い。Antigravity CLI を入れてから実行する。" >&2
  exit 127
fi

if [ ! -d "$SRC" ]; then
  echo "agy の設定が $SRC に無い。先に agy を1度動かして認証する。" >&2
  exit 1
fi

if [ ! -f "$PERMISSIONS" ]; then
  echo "許可リストが $PERMISSIONS に無い。" >&2
  exit 1
fi

# 重ね合わせは毎回作り直す。実体側にファイルが増えても追随させるためである。
rm -rf "$OVERLAY"
mkdir -p "$OVERLAY/.gemini/antigravity-cli"

for path in "$SRC"/*; do
  name=$(basename "$path")
  if [ "$name" = "settings.json" ]; then
    continue
  fi
  ln -s "$path" "$OVERLAY/.gemini/antigravity-cli/$name"
done

if [ -e "${HOME}/.gemini/config" ]; then
  ln -s "${HOME}/.gemini/config" "$OVERLAY/.gemini/config"
fi

# 許可リストをそのまま設定として置く。
# agy は知らないキー（説明用の "_この設定について"）を捨てて読む。
cp "$PERMISSIONS" "$OVERLAY/.gemini/antigravity-cli/settings.json"

exec env HOME="$OVERLAY" agy "$@"

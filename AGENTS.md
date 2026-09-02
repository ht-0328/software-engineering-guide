# このリポジトリで作業するときの指示

このリポジトリは、システム開発の進め方を書籍とWebの情報から整理して手引きにする。**本文は日本語で書き、ファイル名は英語の小文字とハイフンで付ける。**

この指示書は codex と Antigravity が読む。Claude Code 向けの指示は [CLAUDE.md](CLAUDE.md) にある。

## 守ること

1. **主張には出典IDと該当箇所を添える。** 出典が無い記述は「出典なし・私見」と明記する。出典IDの一覧は [research/sources.md](research/sources.md) にある。
2. **書籍の本文を長く写さない。** 連続する3文以上をそのまま写さない。要約と、ページを指す出典IDを残す。
3. **参考書のPDFと `research/extracted/` を変更しない。** PDFは購入者を特定できる情報を含む。
4. **`docs/` と `research/` に書き込まない。** 調査を頼まれた場合は、結果を最終メッセージとして返す。ファイルは依頼した側が置く。
5. **未解決の印（`TBD`、`FIXME`）を残さない。** 決まっていないことは、決まっていないと書く。

## 調査を頼まれたとき

中間成果物の書式は [.agents/skills/writing-interim-artifacts/SKILL.md](.agents/skills/writing-interim-artifacts/SKILL.md) にある。**1行が1主張で、主張ID・根拠の所在・確からしさを必ず添える。**

書籍から調べるときは [.agents/skills/searching-book-extracts/SKILL.md](.agents/skills/searching-book-extracts/SKILL.md) に従う。**抽出テキストは1冊40万字ある。全文を読まない。**

## 使ってよい道具

読み取りと検索は自由に行ってよい。**禁止しているコマンドは [.codex/rules/repository.rules](.codex/rules/repository.rules) にある。** 破壊的な操作、外への通信、導入を伴うコマンドを止めている。

Webを調べるときは、組み込みの検索を使う。**根拠に使ってよい発信元は [.agents/rules/repository-constraints.md](.agents/rules/repository-constraints.md) にある。**

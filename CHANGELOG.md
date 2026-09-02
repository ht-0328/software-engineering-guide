# 変更履歴

このリポジトリの版ごとの変更を記録する。版の付け方は [セマンティックバージョニング](https://semver.org/lang/ja/) に従う。

**この手引きでは、章の追加を機能追加（マイナー）、観点の削除や意味の変更を破壊的変更（メジャー）として扱う。**

## 0.3.0（2026-09-03）

調査から文書までを、4系統の調査と3者の議論で進める仕組みを足した。**本文はまだ無い。**

### 追加

- 指揮役のエージェント（[.claude/agents/doc-research-orchestrator.md](.claude/agents/doc-research-orchestrator.md)）。題材から文書1本までを通しで進める。
- 中間成果物の書式のスキル（`.claude/skills/writing-interim-artifacts/`）。置き場所は `research/orchestration/<題材>/` とする。
- 公開情報の調査のスキル（`.claude/skills/researching-public-sources/`）。URLと確認日を必ず残す。
- 書籍の調査のスキル（`.claude/skills/researching-book-sources/`）。抽出テキストを全文読まずにページ番号つきで引く道具を同梱する。
- 3者の議論のスキル（`.claude/skills/running-multi-ai-debate/`）。codex と Antigravity に1往復の批評をさせる。
- 標準に沿った執筆のスキル（`.claude/skills/writing-docs-to-standard/`）。検査で落ちる型と直し方を参照先に持つ。
- 中間成果物の置き場所 `research/orchestration/`。Gitで追跡する。

### 変更

- [CLAUDE.md](CLAUDE.md) に、通しで文書を作るときの入口を足した。
- [README.md](README.md) のフォルダ構成に `research/orchestration/` を足した。

## 0.2.0（2026-09-02）

公開の仕組みと、プルリクエストの型を足した。**本文はまだ無い。**

### 追加

- Zensicalによるサイト生成（[tools/build_site.py](tools/build_site.py)、[zensical.toml](zensical.toml)）。
- GitHub Pagesへの公開（[.github/workflows/pages.yml](.github/workflows/pages.yml)）。`master` への push で動く。
- 取り込み前の検査（[.github/workflows/docs.yml](.github/workflows/docs.yml)）。公開はしない。
- プルリクエストの型（[.github/pull_request_template.md](.github/pull_request_template.md)）。対応の概要と意図を書く欄を持つ。
- このリポジトリの道具のイメージ（[tools/Dockerfile](tools/Dockerfile)）。検査・抽出・サイト生成をこの1つで動かす。
- 決定記録 [ADR-002](docs/adr/ADR-002-publish-with-zensical.md)。生成器と公開先の選定理由。

### 変更

- 機密区分を「社内限り」から「公開可」に変えた。GitHub Pagesで公開するためである。
- 道具を動かすイメージ名を `edocs-tools` から `guide-tools` に変えた。

## 0.1.0（2026-09-02）

初回セットアップ。**本文はまだ無い。**

### 追加

- 出典カタログ（[research/sources.md](research/sources.md)）。書籍22冊に出典IDを割り当てた。
- 章の予定と、章の書式（[docs/index.md](docs/index.md)）。
- 構成と規則の決定記録（[ADR-001](docs/adr/ADR-001-repository-structure.md)）。
- 文書の検査の入口（`tools/doc_lint.py`）。ルールの本体はサブモジュールが持つ。
- PDF抽出の入口（`tools/extract_pdf.py`）。出典IDの対応は出典カタログから読む。
- サブモジュール `engineering-docs-standard`（文書の書き方の標準）。

### 変更

- 参考書のPDFを置くフォルダの名前を `refarances/` から `references/` に直した。綴りの誤りである。
- `references/` の参考書のうち、日本語の書名だったファイル5件を英語の名前に変えた。

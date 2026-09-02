# 変更履歴

このリポジトリの版ごとの変更を記録する。版の付け方は [セマンティックバージョニング](https://semver.org/lang/ja/) に従う。

**この手引きでは、章の追加を機能追加（マイナー）、観点の削除や意味の変更を破壊的変更（メジャー）として扱う。**

## 0.4.0（2026-09-03）

codex と Antigravity の設定・スキル・許可リストを、リポジトリの中に置いた。**本文はまだ無い。**

### 追加

- 外部AI向けの指示書 [AGENTS.md](AGENTS.md)。codex と Antigravity が読む。
- 3者が共有するスキル `.agents/skills/`。中間成果物の書式と、抽出テキストの探し方の2つ。
- Antigravity 向けの制約 `.agents/rules/repository-constraints.md`。書き込みの禁止、実行しないコマンド、発信元の許可。
- codex の設定 [.codex/config.toml](.codex/config.toml)。読み取りのみ、シェルからの通信は閉じる。
- codex の実行方針 `.codex/rules/repository.rules`。破壊的な操作、外への通信、導入を伴うコマンドを止める。

### 変更

- 中間成果物の書式の正本を `.claude/skills/` から `.agents/skills/` へ移した。3者が同じ書式を読むためである。`.claude/skills/writing-interim-artifacts/` は正本を指し、司会だけが行う確認を持つ。
- 外部AIへの依頼文から書式の規則を外した。2者とも `AGENTS.md` と `.agents/skills/` を読むためである。

### 確かめたこと

- codex は `AGENTS.md`、`.agents/skills/`、`.codex/skills/`、`.codex/config.toml`、`.codex/rules/*.rules` を読む。
- `.codex/rules/` の `prefix_rule` は実際に実行を止める。`network_rule` による遮断は、この環境では確認できなかった。
- Antigravity の `read_url` の許可リストは実際に効く。許可していないホストは拒否される。
- **Antigravity はワークスペース側の設定を読まない。** `.agents/settings.json` と `.gemini/settings.json` は無視された。読むのは `~/.gemini/antigravity-cli/settings.json` だけである。

### Antigravity の許可について

**Antigravity の許可だけは、リポジトリの中に置けない。** そのため `~/.gemini/antigravity-cli/settings.json` の `permissions.allow` に、読み取りと取得を許すURLを足した。既存の設定は残してある。

`deny`（書き込みや破壊的なコマンドの拒否）は入れていない。**入れると、このリポジトリ以外での Antigravity の作業でもファイルを書けなくなるためである。** 実行しないコマンドの一覧は `.agents/rules/repository-constraints.md` に規則として置いた。

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

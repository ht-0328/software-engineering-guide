# 変更履歴

このリポジトリの版ごとの変更を記録する。版の付け方は [セマンティックバージョニング](https://semver.org/lang/ja/) に従う。

**この手引きでは、章の追加を機能追加（マイナー）、観点の削除や意味の変更を破壊的変更（メジャー）として扱う。**

## 0.7.0（2026-09-08）

**章「03 アーキテクチャ」を足した。** 観点は18件で、`AR-01` から `AR-18` まで振ってある。フロントエンド・BFF・API の責務、業務ルールの置き場所、BFF を置く判断、構造を決める材料、層の間でやり取りする値の形の5つに答える。

### 追加

- 章 [03 アーキテクチャ](docs/03-architecture.md)。悪い例と良い例を Java の対で示し、層の関係と判断の順序は Mermaid の図で示す。
- 公開情報の出典15件 `SRC-EXT-016` から `SRC-EXT-030`。記録は `research/external/` に1件1ファイルで置いた。
- 調査の中間成果物 `research/orchestration/architecture/`。計画、公開情報の調査、書籍の調査、Antigravity の回答と批評、議論の記録の6ファイル。
- [research/cross-reference.md](research/cross-reference.md) に「章 03 アーキテクチャ」の節。複数の出典が支持する原則10件、1つの出典にしか根拠が無い原則6件、根拠が独立していないもの3件、出典どうしの食い違い5件を記録した。

### 変更

- [research/sources.md](research/sources.md) の「書籍以外の出典」に、採番ずみの15件を足した。「読もうとして読めなかったもの」に ISO/IEC/IEEE 42010 と CMU/SEI-2000-TR-004 を足した。
- [docs/index.md](docs/index.md) の章の一覧で、03 の状態を「未着手」から「公開ずみ」に変えた。扱う内容も「サービス分割、API、品質特性」から「責務の境界、フロントエンド・BFF・API の分担」に直した。
- [zensical.toml](zensical.toml) の `nav` の「本文」に `03-architecture.md` を足した。
- [README.md](README.md) の版と「いまどこまで進んでいるか」の表を直した。

### この章の根拠の弱いところ

**4系統のうち3系統でしか調べていない。** codex は調査の途中で利用上限に達した。議論は Claude と Antigravity の2者で行った。**3章が連続して2者の議論で書かれている。**

**決着しなかった論点が4件ある。** 専任フロントエンドチームを置くことが誤りか、品質特性と変更の頻度とチームの分かれ方の優先順位、組織を先に変える進め方の有効性、BFF の保守費用の4つである。**どれも判定できる資料が見つからなかった。** 経緯は `research/orchestration/architecture/40-debate.md` にある。

**BFF の観点4件は、根拠が1人に集中している。** `SRC-ARCH-002` と `SRC-EXT-016` は、どちらも Sam Newman が書いたものである。**独立した2件ではない。**

**規格を3件読めていない。** ISO/IEC 25010、ISO/IEC/IEEE 42010、GraphQL 仕様の公式サイトが、2026-09-08 の時点でいずれも読めなかった。

## 0.6.0（2026-09-07）

**章「02 設計」を足した。** 観点は16件で、`DS-01` から `DS-16` まで振ってある。責務の分割、共通化の判断、パッケージ構成、名前が構造を歪める場面、変更容易性と YAGNI、デザインパターンの使いどころの6つに答える。

### 追加

- 章 [02 設計](docs/02-design.md)。悪い例と良い例を Java の対で示し、パッケージ構成はディレクトリ木で示す。デザインパターンは Strategy、State、Observer、Decorator の4つを、症状の側から説明する。
- 公開情報の出典9件 `SRC-EXT-007` から `SRC-EXT-015`。記録は `research/external/` に1件1ファイルで置いた。
- 調査の中間成果物 `research/orchestration/design/`。計画、公開情報の調査、書籍の調査、Antigravity の回答と批評、議論の記録の6ファイル。
- [research/cross-reference.md](research/cross-reference.md) に「章 02 設計」の節。複数の出典が支持する原則10件、1つの出典にしか根拠が無い原則9件、出典どうしの食い違い4件を記録した。

### 変更

- [research/sources.md](research/sources.md) の「書籍以外の出典」に、採番ずみの9件を足した。
- [docs/index.md](docs/index.md) の章の一覧で、02 の状態を「未着手」から「公開ずみ」に変えた。扱う内容も「モデリング」から「共通化の判断、パッケージ構成」に直した。
- [zensical.toml](zensical.toml) の `nav` の「本文」に `02-design.md` を足した。

### 修正

- 章 02 の本文で、DRY の定義の出典が `SRC-EXT-011`（Martin Fowler「Yagni」）になっていたのを `SRC-CODE-002` p.126 に直した。**その資料には DRY の定義が無い。**

### この章の根拠の弱いところ

**4系統のうち3系統でしか調べていない。** codex は利用上限に達し、起動できなかった。議論は Claude と Antigravity の2者で行った。

**決着しなかった論点が3件ある。** 変更容易性と YAGNI の2つの規則が同じものか、抽象化への投資がいつ回収されるか、パッケージ構成の「大まかな出発点」に何を置くか、の3つである。**どれも判定できる資料が見つからなかった。** 経緯は `research/orchestration/design/40-debate.md` にある。

**公開情報の突き合わせが無い。** 12件のうち Antigravity が独立に読んだのは1件だけで、残りは Claude しか読んでいない。

**デザインパターンの選定基準は、どの資料にも書かれていない。** 4つを選んだ基準は議論の中で決めたものである。

## 0.5.0（2026-09-07）

**最初の本文を足した。** 章「01 良いコードとは何か」である。観点は17件で、`GC-01` から `GC-17` まで振ってある。

### 追加

- 章 [01 良いコードとは何か](docs/01-good-code.md)。良し悪しの判断基準、変更しやすさ、テストしやすさ、名前の付け方の4つに答える。悪い例と良い例を Java の対で8組示す。
- 原則と出典の対応 [research/cross-reference.md](research/cross-reference.md)。複数の出典が支持する原則、1つの出典にしか根拠が無い原則、出典どうしの食い違いを分けて記録する。
- 公開情報の出典6件 `SRC-EXT-001` から `SRC-EXT-006`。記録は `research/external/` に1件1ファイルで置いた。
- 調査の中間成果物 `research/orchestration/good-code/`。計画、公開情報の調査、書籍の調査、Antigravity の回答と批評、議論の記録の6ファイル。

### 変更

- [research/sources.md](research/sources.md) の「書籍以外の出典」に、採番ずみの6件と、読めなかった資料の節を足した。
- [docs/index.md](docs/index.md) の章の一覧で、01 の状態を「未着手」から「公開ずみ」に変えた。
- [zensical.toml](zensical.toml) の `nav` に「本文」の分類と `01-good-code.md` を足した。

### この章の根拠の弱いところ

**4系統のうち3系統でしか調べていない。** codex は利用上限に達し、調査の途中で終了した。議論は Claude と Antigravity の2者で行った。

**ISO/IEC 25010 の規格本体を読めていない。** `www.iso.org` の該当ページと ISO Online Browsing Platform が、2026-09-07 の時点でどちらも HTTP 403 を返した。そのため「規格の用語を手引きの根拠に使ってよいか」は決着していない。**この章は規格を根拠にしていない。** 経緯は `research/orchestration/good-code/40-debate.md` の `D-4` にある。

**公開情報の調査は1系統しか行っていない。** 書籍の調査は Claude と Antigravity が独立に行い突き合わせができているが、公開情報にはそれが無い。

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

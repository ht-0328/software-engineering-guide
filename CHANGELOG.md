# 変更履歴

このリポジトリの版ごとの変更を記録する。版の付け方は [セマンティックバージョニング](https://semver.org/lang/ja/) に従う。

**この手引きでは、章の追加を機能追加（マイナー）、観点の削除や意味の変更を破壊的変更（メジャー）として扱う。**

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

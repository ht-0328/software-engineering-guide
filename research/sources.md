# 出典カタログ

| 項目 | 内容 |
|---|---|
| これは何か | この手引きが根拠に使う資料の一覧と、出典IDの採番規則 |
| 作成者 | Claude（Opus 5） |
| 機密区分 | 社内限り（書名と所在のみ。本文の転載は含まない） |
| 想定読者 | この手引きを書く人。および、記述の根拠をたどる人 |
| 保守責任者 | このリポジトリの保守担当 |
| 最終確認日 | 2026-09-02 |

## 出典IDの読み方

出典IDは `SRC-<分野>-<連番>` の形をとる。**本文で主張を書くときは、必ずこのIDと該当箇所（章・節）を添える。**

| 分野 | 扱う範囲 |
|---|---|
| `CODE` | コードそのものの良し悪し。命名、可読性、クラス設計 |
| `DESIGN` | 設計の原則とパターン。責務の分割、モデリング |
| `ARCH` | システム全体の構造。アーキテクチャ、サービス分割、API |
| `REVIEW` | コードレビューの観点と進め方 |
| `TEST` | テストの観点、技法、自動化 |
| `THINK` | 問題の見つけ方、抽象化、思考の型 |
| `UI` | 画面とインターフェースの設計 |
| `CLOUD` | クラウド基盤の仕組み |
| `AI` | 生成AIを組み込んだ開発 |
| `WRITE` | 文書の書き方（姉妹リポジトリが本編を持つ） |
| `EXT` | 書籍以外の公開情報。標準、公式文書、査読つき論文 |

**分野が重なる本は多い。** 分野は本の主題で決め、どの章でどの本を使うかは「章と出典の対応」で示す。

## 書籍

PDFは `references/` に置く。**購入者ウォーターマーク（メールアドレス）を含むため、Gitでは追跡しない。**

| ID | 書名 | 著者 | ファイル | ページ |
|---|---|---|---|---|
| `SRC-CODE-001` | リーダブルコード | Dustin Boswell、Trevor Foucher（角征典 訳） | `readeable-code.pdf` | 261 |
| `SRC-CODE-002` | 改訂新版 良いコード／悪いコードで学ぶ設計入門 | 仙塲大也 | `good-code-bad-code.pdf` | 409 |
| `SRC-DESIGN-001` | 現場で役立つシステム設計の原則 | 増田亨 | `system-principle.pdf` | 321 |
| `SRC-DESIGN-002` | Head Firstデザインパターン 第2版 | Eric Freeman、Elisabeth Robson（木下哲也 訳） | `head-first-design-pattern.pdf` | 673 |
| `SRC-ARCH-001` | Design It! プログラマーのためのアーキテクティング入門 | Michael Keeling（島田浩二 訳） | `design-it.pdf` | 404 |
| `SRC-ARCH-002` | マイクロサービスアーキテクチャ 第2版 | Sam Newman（木下哲也 訳） | `mircro-service-architecture.pdf` | 665 |
| `SRC-ARCH-003` | 初めてのGraphQL | Eve Porcello、Alex Banks（尾崎沙耶、あんどうやすし 訳） | `graph-ql.pdf` | 257 |
| `SRC-REVIEW-001` | コードレビューの教科書 | 佐藤晶彦 | `code-review-textbook.pdf` | 233 |
| `SRC-TEST-001` | ソフトウェアテスト徹底指南書 | 井芹洋輝 | `software-testing-guide.pdf` | 545 |
| `SRC-TEST-002` | 現場の仕事がバリバリ進む ソフトウェアテスト手法 | 高橋寿一、湯本剛 | `software-testing-methods.pdf` | 208 |
| `SRC-THINK-001` | システム開発と「具体と抽象」 | 細谷功 | `concrete-and-abstract.pdf` | 273 |
| `SRC-UI-001` | オブジェクト指向UIデザイン | ソシオメディア 上野学、藤井幸多 | `object-ui-design.pdf` | 361 |
| `SRC-UI-002` | UIデザインの教科書 新版 | 原田秀司 | `ui-design.pdf` | 211 |
| `SRC-CLOUD-001` | ゼロからわかる Amazon Web Services超入門 改訂新版 | 大澤文孝 | `aws-introduction.pdf` | 321 |
| `SRC-CLOUD-002` | 図解即戦力 Amazon Web Servicesのしくみと技術［改訂2版］ | 小笠原種高 | `aws-structure.pdf` | 353 |
| `SRC-AI-001` | LLMのプロンプトエンジニアリング | John Berryman、Albert Ziegler（服部佑樹、佐藤直生 訳） | `llm.pdf` | 277 |
| `SRC-AI-002` | 実践 AIエージェント開発 | Michael Albada（鈴木駿ほか 訳） | `ai-ajent.pdf` | 357 |
| `SRC-AI-003` | 生成AIデザインパターン | Valliappa Lakshmanan、Hannes Hapke（中田秀基 訳） | `ai-design-pattern.pdf` | 521 |
| `SRC-WRITE-001` | 大事な順に身につく 説明の「型」 | 海津佳寿美 | `clear.pdf` | 209 |
| `SRC-WRITE-002` | ITエンジニアのためのMarkdown実践入門 | 平田賀一 | `markdown.pdf` | 241 |
| `SRC-WRITE-003` | 技術者のためのテクニカルライティング入門講座 第2版 | 翔泳社 | `technical-writing.pdf` | 255 |
| `SRC-WRITE-004` | エンジニアのための文章術 再入門講座 新版 | 翔泳社 | `wtite-technique.pdf` | 227 |

書名と著者は、PDFの文書情報（`/Title`、`/Author`）から取った。ページ数はPDFのページ数であり、紙の本のノンブルとは一致しない。

**`SRC-WRITE-003` と `SRC-WRITE-004` だけは文書情報が空だった。** 本文の冒頭（版数、章構成、まえがき）と、姉妹リポジトリ [engineering-docs-standard](../engineering-docs-standard/README.md) が同じ出典IDで挙げている書名を突き合わせて同定した。**同定であって、文書情報による確認ではない。**

`SRC-WRITE-001` から `SRC-WRITE-004` の4冊は、姉妹リポジトリが本編の出典として読み込みずみである。**この手引きでは読み直さず、姉妹リポジトリの結論を参照する。**

## 章と出典の対応

**どの章がどの本に依拠するかの予定である。** 実際に使った出典は、各章を書いた時点で `research/cross-reference.md` に記録する。

| 章（予定） | 主に使う出典 |
|---|---|
| 01 良いコードとは何か | `SRC-CODE-001`、`SRC-CODE-002`、`SRC-DESIGN-001` |
| 02 設計 | `SRC-DESIGN-001`、`SRC-DESIGN-002`、`SRC-CODE-002` |
| 03 アーキテクチャ | `SRC-ARCH-001`、`SRC-ARCH-002`、`SRC-ARCH-003` |
| 04 コードレビュー | `SRC-REVIEW-001`、`SRC-CODE-001`、`SRC-CODE-002` |
| 05 テスト | `SRC-TEST-001`、`SRC-TEST-002` |
| 06 問題の見つけ方 | `SRC-THINK-001`、`SRC-ARCH-001` |
| 07 仕事の進め方 | `SRC-THINK-001`、`SRC-REVIEW-001`、`SRC-ARCH-001` |
| 08 画面とインターフェースの設計 | `SRC-UI-001`、`SRC-UI-002`、`SRC-ARCH-003` |

`SRC-CLOUD-001`、`SRC-CLOUD-002`、`SRC-AI-001` から `SRC-AI-003` は、上の章の主たる根拠にはしない。**特定の技術に依存する内容であり、この手引きが扱う「考え方」とは寿命が違う。** 章を立てる場合は分けて置く。

## 書籍以外の出典

`SRC-EXT-<連番>` を割り当て、調査結果を `research/external/` に1件1ファイルで置く。**URLと確認日を必ず書く。** 書籍と違い、公開情報は書き換わるためである。

この分野で参照する見込みのある公開情報を挙げる。**未調査である。**

| 候補 | 種別 |
|---|---|
| Google Engineering Practices（コードレビュー） | 公開されている社内標準 |
| ISTQB シラバス、JSTQB | テスト技術の用語と体系 |
| ISO/IEC 25010（システム／ソフトウェア品質モデル） | 国際規格 |
| Martin Fowler の記事（リファクタリング、テスト分類） | 個人の公開文書 |
| SWEBOK Guide | 知識体系 |

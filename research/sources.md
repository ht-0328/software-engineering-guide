# 出典カタログ

| 項目 | 内容 |
|---|---|
| これは何か | この手引きが根拠に使う資料の一覧と、出典IDの採番規則 |
| 作成者 | Claude（Opus 5） |
| 機密区分 | 公開可（書名と所在のみ。本文の転載は含まない） |
| 想定読者 | この手引きを書く人。および、記述の根拠をたどる人 |
| 保守責任者 | このリポジトリの保守担当 |
| 最終確認日 | 2026-09-08 |

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
| 02 設計 | `SRC-DESIGN-001`、`SRC-DESIGN-002`、`SRC-CODE-002`、`SRC-THINK-001` |
| 03 アーキテクチャ | `SRC-ARCH-001`、`SRC-ARCH-002`、`SRC-ARCH-003` |
| 04 コードレビュー | `SRC-REVIEW-001`、`SRC-CODE-001`、`SRC-CODE-002` |
| 05 テスト | `SRC-TEST-001`、`SRC-TEST-002` |
| 06 問題の見つけ方 | `SRC-THINK-001`、`SRC-ARCH-001`、`SRC-TEST-001`、`SRC-CODE-002` |
| 07 仕事の進め方 | `SRC-THINK-001`、`SRC-REVIEW-001`、`SRC-ARCH-001` |
| 08 画面とインターフェースの設計 | `SRC-UI-001`、`SRC-UI-002`、`SRC-ARCH-003` |

`SRC-CLOUD-001`、`SRC-CLOUD-002`、`SRC-AI-001` から `SRC-AI-003` は、上の章の主たる根拠にはしない。**特定の技術に依存する内容であり、この手引きが扱う「考え方」とは寿命が違う。** 章を立てる場合は分けて置く。

## 書籍以外の出典

`SRC-EXT-<連番>` を割り当て、調査結果を `research/external/` に1件1ファイルで置く。**URLと確認日を必ず書く。** 書籍と違い、公開情報は書き換わるためである。

### 採番ずみの公開情報

**章「01 良いコードとは何か」を書くために調べたものである。** 調査の記録は `research/external/` にある。

| ID | 資料 | 発行者 | URL | 確認日 | 種別 |
|---|---|---|---|---|---|
| `SRC-EXT-001` | NIST Special Publication 500-235 Structured Testing（1996年、Watson・McCabe 著、Wallace 編） | NIST（米国国立標準技術研究所） | https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication500-235.pdf | 2026-09-07 | 標準化団体の公式文書 |
| `SRC-EXT-002` | Martin Fowler「TwoHardThings」 | Martin Fowler（個人） | https://martinfowler.com/bliki/TwoHardThings.html | 2026-09-07 | 個人の公開文書 |
| `SRC-EXT-003` | Martin Fowler「TestCoverage」 | Martin Fowler（個人） | https://martinfowler.com/bliki/TestCoverage.html | 2026-09-07 | 個人の公開文書 |
| `SRC-EXT-004` | Google Java Style Guide | Google | https://google.github.io/styleguide/javaguide.html | 2026-09-07 | 公開されている社内標準 |
| `SRC-EXT-005` | Martin Fowler「UnitTest」 | Martin Fowler（個人） | https://martinfowler.com/bliki/UnitTest.html | 2026-09-07 | 個人の公開文書 |
| `SRC-EXT-006` | Google Engineering Practices（コードレビューで見るもの） | Google | https://google.github.io/eng-practices/review/reviewer/looking-for.html | 2026-09-07 | 公開されている社内標準 |

**`SRC-EXT-001` だけが標準化団体の一次資料である。** 他の5件は、Google と個人が公開している文書であり、規格ではない。主張の重みを判断するときに区別する。

**章「02 設計」を書くために調べたものを続けて採番した。** `SRC-EXT-007` から `SRC-EXT-015` である。

| ID | 資料 | 発行者 | URL | 確認日 | 種別 |
|---|---|---|---|---|---|
| `SRC-EXT-007` | Robert C. Martin「The Single Responsibility Principle」（2014-05-08） | Robert C. Martin（個人） | https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html | 2026-09-07 | 個人の公開文書（原則の提唱者本人による解説） |
| `SRC-EXT-008` | Sandi Metz「The Wrong Abstraction」（2016-01-20） | Sandi Metz（個人） | https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction | 2026-09-07 | 個人の公開文書 |
| `SRC-EXT-009` | Martin Fowler「Avoiding Repetition」（IEEE Software、2001年1-2月号 p.97-99） | IEEE Computer Society | https://www.martinfowler.com/ieeeSoftware/repetition.pdf | 2026-09-07 | 査読つき雑誌のコラム |
| `SRC-EXT-010` | Robert C. Martin「Granularity」（The C++ Report、1996年11-12月号） | The C++ Report（DePaul 大学が写しを公開） | https://condor.depaul.edu/dmumaugh/OOT/Design-Principles/granularity.pdf | 2026-09-07 | 雑誌の記事本体 |
| `SRC-EXT-011` | Martin Fowler「Yagni」（2015-05-26） | Martin Fowler（個人） | https://martinfowler.com/bliki/Yagni.html | 2026-09-07 | 個人の公開文書 |
| `SRC-EXT-012` | Martin Fowler「Is Design Dead?」（2000-07 初出、2004-05 改訂） | Martin Fowler（個人） | https://www.martinfowler.com/articles/designDead.html | 2026-09-07 | 個人の公開文書 |
| `SRC-EXT-013` | Java SE 21 API 仕様 `java.util.Objects` | Oracle | https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Objects.html | 2026-09-07 | 言語処理系の仕様書 |
| `SRC-EXT-014` | Martin Fowler「DesignStaminaHypothesis」（2007-06-20） | Martin Fowler（個人） | https://martinfowler.com/bliki/DesignStaminaHypothesis.html | 2026-09-07 | 個人の公開文書 |
| `SRC-EXT-015` | Kohavi ほか「Online Experimentation at Microsoft」（Microsoft ThinkWeek paper、2009年） | Microsoft（Experimentation Platform チーム） | https://ai.stanford.edu/~ronnyk/ExPThinkWeek2009Public.pdf | 2026-09-07 | 測定を行った当事者による報告 |

**`SRC-EXT-009`、`SRC-EXT-010`、`SRC-EXT-013`、`SRC-EXT-015` の4件が一次資料である。** 掲載誌の記事本体、仕様書、測定の当事者による報告であるためである。**残る5件は個人が公開している文書であり、規格ではない。**

**`SRC-EXT-007` は原則の提唱者本人が書いたものだが、原典ではない。** 原典は書籍 `Agile Software Development`（2002）であり、手元に無い。

**章「03 アーキテクチャ」を書くために調べたものを続けて採番した。** `SRC-EXT-016` から `SRC-EXT-030` である。

| ID | 資料 | 発行者 | URL | 確認日 | 種別 |
|---|---|---|---|---|---|
| `SRC-EXT-016` | Sam Newman「Backends For Frontends」（パターン定義ページ） | Sam Newman（個人） | https://samnewman.io/patterns/architectural/bff/ | 2026-09-08 | 個人の公開文書（パターンの命名者本人による定義） |
| `SRC-EXT-017` | Phil Calçado「The Back-end for Front-end Pattern (BFF)」（2015-09-18） | Phil Calçado（個人） | https://philcalcado.com/2015/09/18/the_back_end_for_front_end_pattern_bff.html | 2026-09-08 | 個人の公開文書（導入した当事者の報告） |
| `SRC-EXT-018` | Azure Architecture Center「Backends for Frontends pattern」（2025-03-19 版） | Microsoft | https://learn.microsoft.com/en-us/azure/architecture/patterns/backends-for-frontends | 2026-09-08 | 公開されている社内標準 |
| `SRC-EXT-019` | OWASP「Input Validation Cheat Sheet」 | OWASP Foundation | https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html | 2026-09-08 | 非営利団体が公開する指針 |
| `SRC-EXT-020` | Martin Fowler「PresentationDomainDataLayering」 | Martin Fowler（個人） | https://martinfowler.com/bliki/PresentationDomainDataLayering.html | 2026-09-08 | 個人の公開文書 |
| `SRC-EXT-021` | Martin Fowler「ConwaysLaw」（2022-10-20） | Martin Fowler（個人） | https://martinfowler.com/bliki/ConwaysLaw.html | 2026-09-08 | 個人の公開文書 |
| `SRC-EXT-022` | Melvin E. Conway「How Do Committees Invent?」（Datamation 1968年4月号 p.28-31） | Datamation（著者本人が写しを公開） | https://www.melconway.com/Home/Committees_Paper.html | 2026-09-08 | 雑誌の記事本体 |
| `SRC-EXT-023` | Roy T. Fielding 博士論文 第5章「Representational State Transfer (REST)」（2000年） | カリフォルニア大学アーバイン校 | https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm | 2026-09-08 | 学位論文の本体 |
| `SRC-EXT-024` | GraphQL 仕様 Section 1「Overview」 | GraphQL Foundation | https://github.com/graphql/graphql-spec/blob/main/spec/Section%201%20--%20Overview.md | 2026-09-08 | 仕様書の本文（版は未確認） |
| `SRC-EXT-025` | Alistair Cockburn「Hexagonal Architecture」（初出 2005-09-04） | Alistair Cockburn（個人） | https://alistair.cockburn.us/hexagonal-architecture/ | 2026-09-08 | 個人の公開文書（パターンの提唱者本人による定義） |
| `SRC-EXT-026` | Michael Nygard「Documenting Architecture Decisions」（2011-11-15） | Cognitect | https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions | 2026-09-08 | 企業のブログ（ADR の提唱者本人による定義） |
| `SRC-EXT-027` | Barbacci ほか「Using the ATAM to Evaluate the Software Architecture for a Product Line of Avionics Systems」（CMU/SEI-2003-TN-012、2003年7月） | Carnegie Mellon University Software Engineering Institute | https://www.sei.cmu.edu/documents/2021/2003_004_001_14150.pdf | 2026-09-08 | 技術報告書の本体 |
| `SRC-EXT-028` | Martin Fowler「MicroservicePremium」（2015-05-13） | Martin Fowler（個人） | https://martinfowler.com/bliki/MicroservicePremium.html | 2026-09-08 | 個人の公開文書 |
| `SRC-EXT-029` | Martin Fowler「AnemicDomainModel」（2003-11-25） | Martin Fowler（個人） | https://martinfowler.com/bliki/AnemicDomainModel.html | 2026-09-08 | 個人の公開文書 |
| `SRC-EXT-030` | Google AIP-121「Resource-oriented design」 | Google | https://google.aip.dev/121 | 2026-09-08 | 公開されている社内標準 |

**一次資料は6件である。** `SRC-EXT-022`（記事本体）、`SRC-EXT-023`（学位論文）、`SRC-EXT-024`（仕様書）、`SRC-EXT-027`（技術報告書）と、パターンの提唱者本人が書いた `SRC-EXT-016`・`SRC-EXT-025` である。**残る9件は企業と個人の公開文書であり、規格ではない。**

**`SRC-EXT-016` と `SRC-ARCH-002` は同じ著者（Sam Newman）が書いている。** 独立した2件として数えない。

**`SRC-EXT-024` は版を確認できていない。** 公式サイト `https://spec.graphql.org/October2021/` が 2026-09-08 の時点で HTTP 403 を返したため、GitHub 上の原稿を読んだ。

**章「04 コードレビュー」を書くために調べたものを続けて採番した。** `SRC-EXT-031` から `SRC-EXT-041` である。

| ID | 資料 | 発行者 | URL | 確認日 | 種別 |
|---|---|---|---|---|---|
| `SRC-EXT-031` | Google Engineering Practices「Navigating a CL in Review」 | Google | https://google.github.io/eng-practices/review/reviewer/navigate.html | 2026-09-08 | 公開されている社内標準 |
| `SRC-EXT-032` | Google Engineering Practices「Small CLs」 | Google | https://google.github.io/eng-practices/review/developer/small-cls.html | 2026-09-08 | 公開されている社内標準 |
| `SRC-EXT-033` | Google Engineering Practices「Handling Pushback in Code Reviews」 | Google | https://google.github.io/eng-practices/review/reviewer/pushback.html | 2026-09-08 | 公開されている社内標準 |
| `SRC-EXT-034` | Google Engineering Practices「Emergencies」 | Google | https://google.github.io/eng-practices/review/emergencies.html | 2026-09-08 | 公開されている社内標準 |
| `SRC-EXT-035` | Conventional Comments（Paul Slaughter、CC BY 3.0） | conventionalcomments.org | https://conventionalcomments.org/ | 2026-09-08 | 規約の本体 |
| `SRC-EXT-036` | GitLab「Code Review Guidelines」 | GitLab | https://docs.gitlab.com/development/code_review/ | 2026-09-08 | 公開されている社内標準 |
| `SRC-EXT-037` | Sadowski ほか「Modern Code Review: A Case Study at Google」（ICSE-SEIP 2018、p.181-190） | ACM（著者が写しを公開） | https://sback.it/publications/icse2018seip.pdf | 2026-09-08 | 査読つき論文の本体 |
| `SRC-EXT-038` | Bacchelli・Bird「Expectations, Outcomes, and Challenges of Modern Code Review」（ICSE 2013、p.712-721） | Microsoft Research | https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ICSE202013-codereview.pdf | 2026-09-08 | 査読つき論文の本体 |
| `SRC-EXT-039` | Bosu・Greiler・Bird「Characteristics of Useful Code Reviews: An Empirical Study at Microsoft」（MSR 2015） | 著者が写しを公開 | https://www.amiangshu.com/papers/CodeReview-MSR-2015.pdf | 2026-09-08 | 査読つき論文の本体 |
| `SRC-EXT-040` | SmartBear「Best Kept Secrets of Peer Code Review」（Cisco MeetingPlace の事例研究、2006年） | SmartBear Software | https://static0.smartbear.co/smartbear/media/pdfs/best-kept-secrets-of-peer-code-review_redirected.pdf | 2026-09-08 | 測定した当事者の報告 |
| `SRC-EXT-041` | RFC 2119「Key words for use in RFCs to Indicate Requirement Levels」（BCP 14、1997年3月、S. Bradner） | IETF | https://datatracker.ietf.org/doc/html/rfc2119 | 2026-09-08 | 標準化団体の文書の本体 |

**一次資料は5件である。** 査読つき論文3件（`SRC-EXT-037`、`SRC-EXT-038`、`SRC-EXT-039`）、規約の本体（`SRC-EXT-035`）、標準化団体の文書（`SRC-EXT-041`）である。**Google の4件と GitLab の1件は公開された社内標準であり、規格ではない。**

**`SRC-EXT-040` は測定の当事者による報告だが、発行者は利害関係を持つ。** SmartBear はレビューの道具を販売しており、この文書は自社の道具で集めた指標を分析したものである。**対象は2006年5月までの2500件であり、1社1部門の事例研究である。**

**`SRC-EXT-031` から `SRC-EXT-034` は `SRC-EXT-006` と同じサイトにある。** `SRC-EXT-006` は `standard.html`、`looking-for.html`、`comments.html`、`speed.html` の4ページを指す。**重複しないよう、この4ページは `SRC-EXT-006` のままとした。**

**`SRC-EXT-041` はコードレビューのために書かれた文書ではない。** 仕様書の記述水準を示すためのものであり、同文書の第6節は、これらの語を控えめに使うよう求めている。章「04 コードレビュー」は、この点を観点 `RV-22` で扱う。

**章「05 テスト」を書くために調べたものを続けて採番した。** `SRC-EXT-042` から `SRC-EXT-052` である。

| ID | 資料 | 発行者 | URL | 確認日 | 種別 |
|---|---|---|---|---|---|
| `SRC-EXT-042` | ISTQB Certified Tester Foundation Level Syllabus v4.0.1（2024-09-15 発行。v4.0 は 2023-04-21） | International Software Testing Qualifications Board | https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf | 2026-09-08 | 資格制度の本体文書 |
| `SRC-EXT-043` | Martin Fowler「TestPyramid」（2012-05-01） | Martin Fowler（個人） | https://martinfowler.com/bliki/TestPyramid.html | 2026-09-08 | 個人の公開文書 |
| `SRC-EXT-044` | Ham Vocke「The Practical Test Pyramid」（2018-02-26） | martinfowler.com | https://martinfowler.com/articles/practical-test-pyramid.html | 2026-09-08 | 個人の公開文書 |
| `SRC-EXT-045` | Mike Wacker「Just Say No to More End-to-End Tests」（2015-04-22） | Google Testing Blog | https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html | 2026-09-08 | 公開されている社内の見解 |
| `SRC-EXT-046` | Simon Stewart「Test Sizes」（2010-12-13） | Google Testing Blog | https://testing.googleblog.com/2010/12/test-sizes.html | 2026-09-08 | 公開されている社内標準 |
| `SRC-EXT-047` | Alex Eagle「Testing on the Toilet: Change-Detector Tests Considered Harmful」（2015-01-27） | Google Testing Blog | https://testing.googleblog.com/2015/01/testing-on-toilet-change-detector-tests.html | 2026-09-08 | 公開されている社内標準 |
| `SRC-EXT-048` | Andrew Trenk「Testing on the Toilet: Test Behavior, Not Implementation」（2013-08-05） | Google Testing Blog | https://testing.googleblog.com/2013/08/testing-on-toilet-test-behavior-not.html | 2026-09-08 | 公開されている社内標準 |
| `SRC-EXT-049` | Andrew Trenk「Testing on the Toilet: Writing Descriptive Test Names」（2014-10-16） | Google Testing Blog | https://testing.googleblog.com/2014/10/testing-on-toilet-writing-descriptive.html | 2026-09-08 | 公開されている社内標準 |
| `SRC-EXT-050` | Kuhn・Wallace・Gallo「Software Fault Interactions and Implications for Software Testing」（IEEE Transactions on Software Engineering 30(6)、2004年6月、p.418-421） | NIST（著者の所属。NIST が原稿を公開） | https://csrc.nist.gov/CSRC/media/Projects/automated-combinatorial-testing-for-software/documents/kuhn-wallace-gallo-tse-preprint.pdf | 2026-09-08 | 査読つき論文の本体 |
| `SRC-EXT-051` | IPA/SEC「組込みソフトウェア開発における品質向上の勧め［バグ管理手法編］」（SEC BOOKS、2013年） | 独立行政法人情報処理推進機構 | https://www.ipa.go.jp/archive/publish/qv6pgp00000010b6-att/000027629.pdf | 2026-09-08 | 公的機関の刊行物 |
| `SRC-EXT-052` | 西康晴「テスト観点に基づくテスト開発方法論 VSTeP の概要」（2013-04-03） | 電気通信大学（提唱者本人が公開） | https://qualab.jp/materials/VSTeP.130403.bw.pdf | 2026-09-08 | 提唱者本人の公開資料 |

**一次資料は4件である。** 査読つき論文の本体（`SRC-EXT-050`）、資格制度の本体文書（`SRC-EXT-042`）、公的機関の刊行物（`SRC-EXT-051`）、方法論の提唱者本人の資料（`SRC-EXT-052`）である。**Google の5件と個人の2件は、規格ではない。**

**`SRC-EXT-045` から `SRC-EXT-049` は、同じ Google Testing Blog の5件である。** 発行者は1つであり、独立した5件として数えない。

**`SRC-EXT-050` は過去の4研究をまとめている。** 医療機器、Webブラウザ、HTTPサーバ、NASA の分散システムの測定値を1本の論文が並べたものである。**独立した4件として数えない。**

**`SRC-EXT-042` は資格制度のシラバスであり、規格ではない。** ISO/IEC/IEEE 29119 を読めていないため、章「05 テスト」の技法の定義はこの文書の記述で代えている。

**章「06 問題の見つけ方」を書くために調べたものを続けて採番した。** `SRC-EXT-053` から `SRC-EXT-066` である。

| ID | 資料 | 発行者 | URL | 確認日 | 種別 |
|---|---|---|---|---|---|
| `SRC-EXT-053` | Frederick P. Brooks, Jr.「No Silver Bullet: Essence and Accidents of Software Engineering」（UNC TR86-020、1986年9月。IEEE Computer 1987年4月号の原稿） | University of North Carolina at Chapel Hill | https://www.cs.unc.edu/techreports/86-020.pdf | 2026-09-08 | 著者の技術報告 |
| `SRC-EXT-054` | IREB CPRE Foundation Level Syllabus v3.2.0（2024-02-26 発行。Stan Bühne、Martin Glinz） | International Requirements Engineering Board | https://isqi.org/media/7f/9a/3e/1744288053/cpre_foundationlevel_syllabus_EN_v.3.2.pdf | 2026-09-08 | 資格制度の本体文書 |
| `SRC-EXT-055` | Edsger W. Dijkstra「The Humble Programmer」（EWD340、1972年 ACM チューリング賞講演） | University of Texas at Austin（著者の草稿を公開） | https://www.cs.utexas.edu/~EWD/transcriptions/EWD03xx/EWD340.html | 2026-09-08 | 著者本人の草稿 |
| `SRC-EXT-056` | Google「Site Reliability Engineering」12章 Effective Troubleshooting | Google | https://sre.google/sre-book/effective-troubleshooting/ | 2026-09-08 | 公開されている社内標準 |
| `SRC-EXT-057` | Google「Site Reliability Engineering」6章 Monitoring Distributed Systems | Google | https://sre.google/sre-book/monitoring-distributed-systems/ | 2026-09-08 | 公開されている社内標準 |
| `SRC-EXT-058` | Google「Site Reliability Engineering」15章 Postmortem Culture: Learning from Failure | Google | https://sre.google/sre-book/postmortem-culture/ | 2026-09-08 | 公開されている社内標準 |
| `SRC-EXT-059` | Andreas Zeller「Isolating Failure-Inducing Input」（Zeller・Hildebrandt, IEEE Transactions on Software Engineering 28(2)、2002年2月 の原稿） | Universität Passau（著者の原稿） | https://homes.cs.washington.edu/~mernst/teaching/6.893/readings/zeller-tse.pdf | 2026-09-08 | 査読つき論文の原稿 |
| `SRC-EXT-060` | git-bisect の公式マニュアル | Git プロジェクト | https://git-scm.com/docs/git-bisect | 2026-09-08 | 道具の公式文書 |
| `SRC-EXT-061` | Richard I. Cook「How Complex Systems Fail」（1998年、1999年、2000年） | Cognitive Technologies Laboratory, University of Chicago | https://how.complexsystems.fail/ | 2026-09-08 | 著者の公開文書 |
| `SRC-EXT-062` | Hochschild ほか「Cores that don't count」（HotOS '21、2021-05-31 から 06-02、DOI 10.1145/3458336.3465297） | Google（著者の所属。SIGOPS が原稿を公開） | https://sigops.org/s/conferences/hotos/2021/papers/hotos21-s01-hochschild.pdf | 2026-09-08 | 査読つき国際会議の論文 |
| `SRC-EXT-063` | Altman・Bland「Absence of evidence is not evidence of absence」（BMJ 1995;311:485、Statistics Notes） | BMJ | https://www.acsu.buffalo.edu/~wdmccall/os512d/EvidAbs.html | 2026-09-08 | 査読つき雑誌の記事 |
| `SRC-EXT-064` | SEI CERT Oracle Coding Standard for Java, ERR00-J「Do not suppress or ignore checked exceptions」 | Software Engineering Institute, Carnegie Mellon University | https://cmu-sei.github.io/secure-coding-standards/sei-cert-oracle-coding-standard-for-java/rules/exceptional-behavior-err/err00-j | 2026-09-08 | 公的研究機関の規約 |
| `SRC-EXT-065` | CWE-778「Insufficient Logging」（CWE 4.20） | MITRE | https://cwe.mitre.org/data/definitions/778.html | 2026-09-08 | 標準化された分類の本体 |
| `SRC-EXT-066` | OWASP Logging Cheat Sheet | OWASP Foundation | https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html | 2026-09-08 | 業界団体の公開指針 |

**一次資料は7件である。** 査読つき論文2件（`SRC-EXT-059`、`SRC-EXT-062`）、査読つき雑誌の記事1件（`SRC-EXT-063`）、資格制度の本体文書1件（`SRC-EXT-054`）、標準化された分類1件（`SRC-EXT-065`）、公的研究機関の規約1件（`SRC-EXT-064`）、道具の公式文書1件（`SRC-EXT-060`）である。

**`SRC-EXT-056` から `SRC-EXT-058` は、同じ「Site Reliability Engineering」の3章である。** 発行者は1つであり、独立した3件として数えない。

**`SRC-EXT-063` は本文が走査画像である。** PubMed Central の PDF から本文を取り出せなかったため、University at Buffalo が公開する本文の再掲を読んだ。**原本そのものではない。**

**`SRC-EXT-053` は IEEE Computer 1987年4月号の記事の原稿である。** 読んだのは UNC の技術報告 TR86-020（1986年9月）であり、雑誌に載った版とは字句が違う可能性がある。

**`SRC-EXT-059` の題は「Isolating Failure-Inducing Input」である。** IEEE Transactions on Software Engineering 28(2)（2002）に載った Zeller・Hildebrandt「Simplifying and Isolating Failure-Inducing Input」の原稿にあたる。**雑誌に載った版そのものは読んでいない。**

**`SRC-EXT-066` は業界団体の指針であり、規格ではない。** 章「06 問題の見つけ方」は、記録する項目の一覧をこの資料の記述で代えている。

### 読もうとして読めなかったもの

| 資料 | 状態 |
|---|---|
| ISO/IEC 25010（製品品質モデル） | `www.iso.org` の該当ページと ISO Online Browsing Platform が、2026-09-07 の時点でどちらも HTTP 403 を返した。**規格本体を読めていない。** 出典IDは振っていない |
| Stevens・Myers・Constantine「Structured Design」（IBM Systems Journal 13(2)、1974） | 凝集度と結合度の原典である。ACM Digital Library の該当ページ（`https://dl.acm.org/doi/10.1147/sj.132.0115`）が 2026-09-07 の時点で HTTP 403 を返した。**本体を読めていない。** 出典IDは振っていない |
| GoF『Design Patterns』（Gamma ほか、1994） | デザインパターンの原典である。電子版・紙版とも手元に無い。**章「02 設計」は `SRC-DESIGN-002` の記述で代えている。** 出典IDは振っていない |
| ISO/IEC/IEEE 42010（アーキテクチャ記述） | 解説ページ `https://www.iso-architecture.org/42010/` への接続が 2026-09-08 に拒否された（`ECONNREFUSED`）。**規格本体を読めていない。** 出典IDは振っていない |
| SEI「ATAM: Method for Architecture Evaluation」（CMU/SEI-2000-TR-004） | ATAM そのものの定義文書である。`apps.dtic.mil` の該当PDFが 2026-09-08 の時点で HTTP 403 を返した。**章「03 アーキテクチャ」は `SRC-EXT-027`（CMU/SEI-2003-TN-012）の要約で代えている** |
| IEEE Std 1028-2008「Software Reviews and Audits」 | レビューの種類と手順を定めた規格である。`standards.ieee.org` の該当ページが 2026-09-08 の時点で HTTP 403 を返し、IEEE Xplore は HTTP 202 を返して本文を返さなかった。**規格本体を読めていない。** 出典IDは振っていない |
| Chromium「Respectful Code Reviews」（`cr_respect.md`） | `SRC-CODE-002` 17.4.3 が訳出して紹介している指針である。**原典を開いていない。** 章「04 コードレビュー」は同書の訳出を根拠にしている。出典IDは振っていない |
| ISO/IEC/IEEE 29119-4「Test techniques」（2021年） | テスト技法を定めた規格である。`www.iso.org` の該当ページが 2026-09-08 の時点で HTTP 403 を返した。**規格本体を読めていない。** 章「05 テスト」は `SRC-EXT-042` の記述で代えている |
| SWEBOK Guide v4.0「Software Testing」章（2024年10月） | IEEE Computer Society のページが申込みの入力を求め、`swebokwiki.org` が HTTP 403 を返した。**本体を読めていない。** 出典IDは振っていない |
| ISTQB「Certified Tester Test Automation Strategy Syllabus v1.0」 | 自動化の投資回収を扱う文書である。**開いていない。** 章「05 テスト」は、この文書を根拠にした主張を採っていない |
| James Bach「Good Enough Quality: Beyond the Buzzword」（1997年） | `SRC-TEST-002` 7-3 が引いている論文である。**原典を開いていない。** 同書の記述を根拠にしている |
| Kent Beck「Test Desiderata」 | テストの望ましい12の性質を挙げた文書である。Medium が HTTP 403 を返し、著者のリポジトリからも取得できなかった。**主張に採っていない** |
| ISO/IEC/IEEE 29148:2018「Requirements engineering」 | 要求工学のライフサイクル過程を定めた規格である。`iso.org` と `standards.iteh.ai` のいずれも本文を返さなかった。**章「06 問題の見つけ方」は `SRC-EXT-054` の記述で代えている。** 出典IDは振っていない |
| Curtis・Krasner・Iscoe「A field study of the software design process for large systems」（CACM 31(11)、1988） | 17件の大規模開発を聞き取った実地調査である。`dl.acm.org` の該当PDFが 2026-09-08 の時点で HTTP 403 を返した。**本体を読めていない。** 出典IDは振っていない |
| Card「The problem with '5 whys'」（BMJ Qual Saf 2017;26(8):671-677、DOI 10.1136/bmjqs-2016-005849） | なぜなぜ分析への批判である。PubMed が要旨を持たず、`pslhub.org` が HTTP 403 を返した。**書誌情報だけを確認し、主張に採っていない。** 出典IDは振っていない |
| Leveson「A New Accident Model for Engineering Safer Systems」（Safety Science 42(4)、2004、p.237-270） | 直線的な因果モデルへの批判である。`sunnyday.mit.edu` への接続が 2026-09-08 に拒否された（`ECONNREFUSED`）。**同じ向きの主張は `SRC-EXT-061` で代えている。** 出典IDは振っていない |
| Wason「On the failure to eliminate hypotheses in a conceptual task」（Quarterly Journal of Experimental Psychology 12(3)、1960、p.129-140） | 確証バイアスの原典である。出版社の頁が本文を返さなかった。**章「06 問題の見つけ方」は認知バイアスの名前を使っていない。** 出典IDは振っていない |
| David Agans『Debugging』、Andreas Zeller『Why Programs Fail』 | 外部AI（Antigravity）が根拠に挙げた書籍である。**手元に無く、抽出テキストも無い。** 章「06 問題の見つけ方」は、この2冊を根拠にした主張を採っていない。出典IDは振っていない |

### まだ調べていない公開情報

| 候補 | 種別 |
|---|---|
| JSTQB が公開する日本語版シラバスと用語集 | テスト技術の用語と体系。英語版の `SRC-EXT-042` で代えている |
| SWEBOK Guide | 知識体系 |
| Martin Fowler の記事のうち、リファクタリングの手順を扱うもの | 個人の公開文書 |
| 日本の企業が公開するコードレビューの基準 | 公開されている社内標準 |

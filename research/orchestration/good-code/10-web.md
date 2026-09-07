# 良いコードとは何か（公開情報の調査）

| 項目 | 内容 |
|---|---|
| 題材 | 良いコードとは何か（きれいさ、可読性、命名、保守性、テスト容易性） |
| 答える問い | `Q1`、`Q2`、`Q3`、`Q4`、`Q5` |
| 調べた者 | Claude Code（Opus 5） |
| 調べた日 | 2026-09-07 |
| 調べた範囲 | NIST SP 500-235 の本文（PDFを取得して全文検索）、Google Engineering Practices の4ページ、Google Java Style Guide の第5節、martinfowler.com の5ページ、IPA の公開資料1件。**ISO/IEC 25010 の規格本体は読めていない**（`www.iso.org` が HTTP 403 を返した）。SWEBOK、ISTQB 用語集の本体、IEEE の規格は未取得 |

## 主張

| 主張ID | 主張 | 根拠の所在 | 確からしさ |
|---|---|---|---|
| `W-1` | 「完璧なコード」は存在せず、レビューの基準は「コードベース全体の健全性を確実に良くするか」に置かれる | https://google.github.io/eng-practices/review/reviewer/standard.html （2026-09-07 確認）。原文 "there is no such thing as 'perfect' code—there is only better code" | 二次資料（Google の公開する社内標準） |
| `W-2` | コードの良し悪しを見る観点は9つに分けられる。設計、機能、複雑さ、テスト、命名、コメント、スタイル、一貫性、文書 | https://google.github.io/eng-practices/review/reviewer/looking-for.html （2026-09-07 確認） | 二次資料（Google の公開する社内標準） |
| `W-3` | 複雑さは「行・関数・クラス」の各層で見る。ある層だけを見て複雑さを判定しない | 同上。原文 "Check this at every level of the CL—are individual lines too complex? Are functions too complex? Are classes too complex?" | 二次資料 |
| `W-4` | 良い名前とは「何であるか・何をするかを十分に伝えるだけの長さがあり、かつ読みにくくなるほど長くない」名前である | 同上。原文 "A good name is long enough to fully communicate what the item is or does, without being so long that it becomes hard to read." | 二次資料 |
| `W-5` | テストは原則として本体コードと同じ変更に含める。緊急対応のときだけ例外とする | 同上 | 二次資料 |
| `W-6` | 複雑なコードにコメントを足して済ませてはならない。まずコードを単純にする | https://google.github.io/eng-practices/review/reviewer/comments.html （2026-09-07 確認）。原文 "as long as it's not just explaining overly complex code" | 二次資料 |
| `W-7` | レビューが遅いとコードの健全性が下がる。整理・リファクタリング・改善が抑制されるためである | https://google.github.io/eng-practices/review/reviewer/speed.html （2026-09-07 確認） | 二次資料 |
| `W-8` | 循環的複雑度を制限する理由は4つある。複雑なモジュールは誤りを含みやすく、理解しにくく、テストしにくく、変更しにくい | NIST SP 500-235 §2.5 p.15（Watson、McCabe 著、Wallace 編、1996年）https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication500-235.pdf （2026-09-07 確認、PDFを取得して本文を読んだ） | 一次資料 |
| `W-9` | 循環的複雑度の上限として McCabe が提案した10には裏づけがあるが、上限をいくつにするかは決着していない。15で運用した例もある | NIST SP 500-235 §2.5 p.15（1996年）。原文 "The precise number to use as a limit, however, remains somewhat controversial." | 一次資料 |
| `W-10` | 10を超える上限を選んでよいのは、経験のある要員、形式的な設計、コードウォークスルー、網羅的なテスト計画といった条件がそろう場合に限られる | NIST SP 500-235 §2.5 p.15（1996年） | 一次資料 |
| `W-11` | NIST が最も有効とする運用方針は「各モジュールの循環的複雑度を10に抑えるか、超えた理由を文書で示すかのどちらかにする」である | NIST SP 500-235 §2.5 p.16（1996年）。原文 "For each module, either limit cyclomatic complexity to 10 ..., or provide a written explanation of why the limit was exceeded." | 一次資料 |
| `W-12` | 循環的複雑度はテストに必要な経路の数を与える。したがって複雑さの数値はテストの手間の下限を示す | NIST SP 500-235 §2.5 p.16（1996年）。原文 "Cyclomatic complexity gives the number of tests" | 一次資料 |
| `W-13` | 指標を小さく見せるために測り方を変えると、テストが各分岐を通らなくなり、テストとして成立しなくなる | NIST SP 500-235 §2.5 pp.15-16（1996年）。複雑度90のモジュールに何もしない10分岐を足して「修正複雑度10」に見せた実例が挙がっている | 一次資料 |
| `W-14` | 内部品質（コードの構造）は利用者に見えないが、機能追加の速さを通じて費用に効く。「品質と費用のどちらを取るか」という形の選択ではない | https://martinfowler.com/articles/is-quality-worth-cost.html （2026-09-07 確認、2019年公開）。原文 "Better internal quality makes adding new features easier, therefore quicker and cheaper." | 二次資料（著者個人の公開文書） |
| `W-15` | 内部品質の低下による減速は数週間で現れる。したがって短命な開発でも内部品質への投資は回収されうる | 同上。原文 "developers find poor quality code significantly slows them down within a few weeks" | 二次資料 |
| `W-16` | コードの臭い（code smell）とは「表面に現れた兆候であり、多くの場合はより深い問題に対応する」ものである | https://martinfowler.com/bliki/CodeSmell.html （2026-09-07 確認） | 二次資料 |
| `W-17` | 臭いは規則ではなく手がかりである。長いメソッドが常に問題とは限らない | 同上。原文 "Smells don't always indicate a problem." | 二次資料 |
| `W-18` | 自動テストが十分にあると、コードを良い形に保つ時間が取れ、機能追加が次第に速くなる循環に入る | https://martinfowler.com/bliki/SelfTestingCode.html （2026-09-07 確認） | 二次資料 |
| `W-19` | テストのカバレッジを目標値にすると、質の低いテストで数値だけを満たせてしまう。カバレッジは「テストされていない箇所を見つける道具」として使う | https://martinfowler.com/bliki/TestCoverage.html （2026-09-07 確認）。原文 "If you make a certain level of coverage a target, people will try to attain it." | 二次資料 |
| `W-20` | 単体テストの共通の性質は3つである。対象の範囲が小さいこと、プログラマ自身が書くこと、速いこと | https://martinfowler.com/bliki/UnitTest.html （2026-09-07 確認） | 二次資料 |
| `W-21` | テストダブルは、外部サービスとの通信のような非決定性を取り除くのに有効である | 同上。原文 "Test doubles are invaluable to remove non-determinism when talking to remote services." | 二次資料 |
| `W-22` | 命名の難しさは業界で広く共有されている。「コンピュータ科学で難しいのはキャッシュの無効化と名前付けの2つだけ」（Phil Karlton） | https://martinfowler.com/bliki/TwoHardThings.html （2026-09-07 確認） | 二次資料 |
| `W-23` | Java の命名規約は識別子の種類ごとに決まっている。クラスは UpperCamelCase の名詞句、メソッドは lowerCamelCase の動詞句、定数は UPPER_SNAKE_CASE、フィールドとローカル変数と引数は lowerCamelCase である | Google Java Style Guide §5.2.2-5.2.7 https://google.github.io/styleguide/javaguide.html （2026-09-07 確認） | 二次資料（Google の公開する社内標準） |
| `W-24` | Java の定数（UPPER_SNAKE_CASE で書くもの）は「深く不変で、観測できる副作用を持たない `static final` フィールド」に限る。`final` であることだけでは定数にならない | 同上 §5.2.4、§5.2.7 | 二次資料 |
| `W-25` | 識別子に `name_`、`mName`、`s_name`、`kName` のような接頭辞・接尾辞を付けない | 同上 §5.1 | 二次資料 |
| `W-26` | 頭字語は1語として扱う。`XMLHTTPRequest` ではなく `XmlHttpRequest` と書く | 同上 §5.3 | 二次資料 |
| `W-27` | 公開メソッドの引数に1文字の名前を使わない | 同上 §5.2.6 | 二次資料 |
| `W-28` | ISO/IEC 25010:2013 の製品品質モデルは品質特性を8つに分け、そのうち1つが保守性である。8つは機能適合性、性能効率性、互換性、使用性、信頼性、セキュリティ、保守性、移植性である | IPA/SEC「ソフトウェア品質説明の考え方」p.16（2014年）https://www.ipa.go.jp/archive/digital/iot-en-ci/mieruka/ps6vr7000000y3u7-att/000040880.pdf （2026-09-07 確認、PDFを取得して本文を読んだ） | 二次資料（IPA による規格の要約。規格本体は読めていない） |

## 答えられなかったこと

| 問い | 状態 | 理由 |
|---|---|---|
| `Q1` | 調べたが読めない | ISO/IEC 25010 の規格本体を読もうとしたが、`www.iso.org/standard/78176.html` と ISO Online Browsing Platform がいずれも HTTP 403 を返した（2026-09-07）。**保守性の副特性（モジュール性、再利用性、解析性、修正性、試験性）の一覧と定義は、規格本体で確認できていない。** IPA の資料で確認できたのは2013年版の最上位8特性までである |
| `Q3` | 調べたが見つからない | 「テスト容易性の高いコードの性質」を規格の水準で定義した公開文書は見つけられなかった。NIST SP 500-235 は複雑度とテスト経路数の関係を示すが、コードの性質そのものは扱っていない |
| `Q4` | 調べたが見つからない | 命名について、Java の表記規約（大文字小文字の使い分け）を超えて「意味の付け方」を定めた公開規格は見つからなかった。Google Java Style Guide も表記規約が中心である |
| `Q5` | 調べていない | 「悪い例と良い例の対」は書籍側で扱う範囲であり、公開情報では探していない |

## 出典IDについて

**`SRC-EXT-` の番号はここでは振らない。** 最終文書の根拠に採用すると決めた時点で `research/sources.md` に採番する。

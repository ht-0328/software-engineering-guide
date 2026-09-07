# 設計 の公開情報の調査

| 項目 | 内容 |
|---|---|
| 題材 | 設計（責務の分割、共通化の判断、パッケージ構成、デザインパターンの使いどころ） |
| 答える問い | `Q1` から `Q6`（`00-plan.md` の番号） |
| 調べた者 | Claude Code（Opus 5）。司会 |
| 調べた日 | 2026-09-07 |
| 調べた範囲 | 下の「読んだ資料」の10件を本文まで開いた。ISO/IEC 25010 は章01 の調査で HTTP 403 のため未読であり、この調査でも再試行していない。GoF『Design Patterns』（1994）の本体は電子版・紙版とも手元に無く、読んでいない |

## 読んだ資料

**「段」は `researching-public-sources` の3段（一次・二次・三次）である。**

| 資料 | 発行者 | URL | 確認日 | 段 |
|---|---|---|---|---|
| Robert C. Martin「The Single Responsibility Principle」（2014-05-08） | Robert C. Martin（個人） | https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html | 2026-09-07 | 二次（原則の提唱者本人による解説） |
| Robert C. Martin「Granularity」（The C++ Report、1996年11-12月号） | The C++ Report（DePaul 大学が写しを公開） | https://condor.depaul.edu/dmumaugh/OOT/Design-Principles/granularity.pdf | 2026-09-07 | 一次（掲載誌の記事本体） |
| Martin Fowler「Avoiding Repetition」（IEEE Software、2001年1-2月号 p.97-99） | IEEE Computer Society | https://www.martinfowler.com/ieeeSoftware/repetition.pdf | 2026-09-07 | 一次（査読誌のコラム本体） |
| Martin Fowler「Yagni」（2015-05-26） | Martin Fowler（個人） | https://martinfowler.com/bliki/Yagni.html | 2026-09-07 | 二次（個人の公開文書） |
| Martin Fowler「Is Design Dead?」（2000-07 初出、2004-05 改訂） | Martin Fowler（個人） | https://www.martinfowler.com/articles/designDead.html | 2026-09-07 | 二次（個人の公開文書） |
| Martin Fowler「DesignStaminaHypothesis」（2007-06-20） | Martin Fowler（個人） | https://martinfowler.com/bliki/DesignStaminaHypothesis.html | 2026-09-07 | 二次（個人の公開文書） |
| Sandi Metz「The Wrong Abstraction」（2016-01-20） | Sandi Metz（個人） | https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction | 2026-09-07 | 二次（個人の公開文書） |
| Google Engineering Practices「What to look for in a code review」 | Google | https://google.github.io/eng-practices/review/reviewer/looking-for.html | 2026-09-07 | 二次（公開されている社内標準） |
| Google Java Style Guide §5.2.2 | Google | https://google.github.io/styleguide/javaguide.html | 2026-09-07 | 二次（公開されている社内標準） |
| Java SE 21 API 仕様 `java.util.Objects` | Oracle | https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Objects.html | 2026-09-07 | 一次（言語処理系の仕様書） |
| Simon Brown「Modular monoliths」（発表資料。本文に「It's 2024!」の記載あり） | Simon Brown（個人） | https://static.simonbrown.je/modular-monoliths.pdf | 2026-09-07 | 二次（個人の公開文書） |
| The Pragmatic Programmer 20th Anniversary Edition の Tips 一覧 | Pragmatic Bookshelf（版元） | https://pragprog.com/tips/ | 2026-09-07 | 二次（版元による書籍からの抜粋） |
| Kohavi ほか「Online Experimentation at Microsoft」（Microsoft ThinkWeek paper、2009年） | Microsoft（Experimentation Platform チーム） | https://ai.stanford.edu/~ronnyk/ExPThinkWeek2009Public.pdf | 2026-09-07 | 一次（測定を行った当事者による報告） |

**一次資料は4件だけである。** 残りは個人と Google が公開している文書であり、規格でも標準化団体の文書でもない。

## 主張

### Q1 単一責任の「単一」とは何か

| 主張ID | 主張 | 根拠の所在 | 確からしさ |
|---|---|---|---|
| `W-01` | SRP の定義は「モジュールが変更される理由は1つだけであるべきだ」である。提唱者本人の言葉では each software module should have one and only one reason to change | blog.cleancoder.com（2026-09-07 確認、2014-05-08 付） | 二次資料 |
| `W-02` | 提唱者は2014年に「reason for change（変更の理由）」を「アクター」と言い直した。アクターとは、そのモジュールへの変更を求める人の集団である。本人は This principle is about people と書いている | 同上 | 二次資料 |
| `W-03` | したがって「単一」は、機能の個数でも行数でもなく、**変更を要求してくる人の集団の数**で数える | 同上 | 二次資料 |
| `W-04` | 提唱者の例は `Employee` クラスであり、`calculatePay` は CFO、`reportHours` は COO、`save` は CTO の組織が変更を要求する。3つのアクターがいるので責務は3つである | 同上 | 二次資料 |
| `W-05` | 提唱者は SRP の別の言い方として Gather together the things that change for the same reasons. Separate those things that change for different reasons を挙げる。**分ける基準と集める基準は同じ1つである** | 同上 | 二次資料 |
| `W-06` | 提唱者が挙げる害は、あるアクターのための変更が別のアクターの機能を壊すことである。顧客と管理者を最も怖がらせるのは、自分が頼んだ変更と無関係に見える故障だと本人が書いている | 同上 | 二次資料 |

### Q2 共通化の判断基準

| 主張ID | 主張 | 根拠の所在 | 確からしさ |
|---|---|---|---|
| `W-07` | DRY の原典の言い回しは Every piece of knowledge must have a single, unambiguous, authoritative representation within a system である。版元の Tips 一覧では Tip 15、p.31 | https://pragprog.com/tips/ （2026-09-07 確認、20th Anniversary Edition） | 二次資料 |
| `W-08` | **DRY の対象は「知識」であって「コードの字面」ではない。** 原典の文が knowledge と書いており、code とは書いていない | 同上 | 二次資料 |
| `W-09` | Fowler は重複除去の手順を3段に整理する。共通と可変を見分ける、共通を可変から切り離す方法を見つける、共通の側の重複を消す | IEEE Software 2001年1-2月号 p.97（2026-09-07 確認） | 一次資料 |
| `W-10` | **Fowler は「見た目が同じでも偶然の重複はある」と認めている。** ただし本人は it is rare and easy to spot（まれで見分けやすい）とし、原則として重複は消す側に立つ | 同上 | 一次資料 |
| `W-11` | Metz は逆の立場をとる。duplication is far cheaper than the wrong abstraction（重複は、誤った抽象よりはるかに安い）と書き、prefer duplication over the wrong abstraction を勧める | sandimetz.com（2026-09-07 確認、2016-01-20 付） | 二次資料 |
| `W-12` | Metz が示す劣化の道筋は8段である。重複を見つけて抽象に抜き出す、時間が経つ、ほぼ合う新要件が来る、引数と条件分岐を足す、これを繰り返して incomprehensible になる、次の担当者が引き継ぐ | 同上 | 二次資料 |
| `W-13` | Metz は、抽象を捨てられない理由を埋没費用の誤謬に帰する。作り込んだものほど残したくなる圧力が働く | 同上 | 二次資料 |
| `W-14` | Metz の処方は「元に戻す」である。抽象を全呼び出し元へ展開し直し（inline）、呼び出し元ごとに不要な部分を消す。When the abstraction is wrong, the fastest way forward is back | 同上 | 二次資料 |
| `W-15` | **`W-10` と `W-11` は正面から食い違う。** Fowler は偶然の重複を「まれ」とし、Metz は誤った抽象の害を重複の害より大きいとする。どちらも測定ではなく経験に基づく | 上の2件 | 推測（食い違いの指摘は調べた者による整理） |
| `W-16` | Google のレビュー基準は、重複そのものではなく「複雑さ」で見る。Too complex usually means can't be understood quickly by code readers と定義する | google.github.io/eng-practices（2026-09-07 確認） | 二次資料 |

### Q3 パッケージ構成

| 主張ID | 主張 | 根拠の所在 | 確からしさ |
|---|---|---|---|
| `W-17` | Martin は1996年にパッケージ結合度の3原則を提示した。REP、CRP、CCP である | The C++ Report 1996年11-12月号（2026-09-07 確認） | 一次資料 |
| `W-18` | REP の本文は THE GRANULE OF REUSE IS THE GRANULE OF RELEASE である。再利用の粒度はリリースの粒度を下回れない | 同上 | 一次資料 |
| `W-19` | CRP の本文は THE CLASSES IN A PACKAGE ARE REUSED TOGETHER である。1つを使うなら全部を使うことになる粒度で切る | 同上 | 一次資料 |
| `W-20` | CCP の本文は THE CLASSES IN A PACKAGE SHOULD BE CLOSED TOGETHER AGAINST THE SAME KINDS OF CHANGES である | 同上 | 一次資料 |
| `W-21` | **Martin は3原則に順位を付けている。** More important than reusability, is maintainability（再利用性より保守性のほうが大切だ）と本文に書く。つまり CCP が REP・CRP に優先する | 同上 | 一次資料 |
| `W-22` | **Martin はパッケージ構成をトップダウンに設計できないと明言する。** The package structure cannot be designed from the top down。クラスを多く設計したあとに決まり、その後も流動し続ける | 同上 | 一次資料 |
| `W-23` | Martin は、パッケージ依存図は機能の説明ではなくビルドの地図（a map of how to build the application）だとする。だから着手時には要らない | 同上 | 一次資料 |
| `W-24` | Brown は分け方を3つに整理する。package by layer（技術的な役割で横に切る）、package by feature（機能・ドメイン概念で縦に切る）、package by component（1つのコンポーネントに関わるものを束ねる） | static.simonbrown.je/modular-monoliths.pdf（2026-09-07 確認） | 二次資料 |
| `W-25` | Brown が package by layer に挙げる欠点は Changes to a layered architecture usually result in changes across all layers（1つの変更が全層に及ぶ）である。**これは `W-20` の CCP に反する** | 同上 | 二次資料 |
| `W-26` | Brown が package by feature の利点として挙げるのは、凝集度が高い、結合度が低い、関係するコードを見つけやすい、の3つである。本人は cited benefits（そう言われている利点）と書いており、測定結果としては示していない | 同上 | 二次資料 |
| `W-27` | Brown の中心の主張は「model-code gap」の解消である。図と実装が食い違うのが問題であり、The code structure should reflect the architectural intent とする | 同上 | 二次資料 |

### Q4 `Util`・`Common`・`Manager`・`Helper` という名前

| 主張ID | 主張 | 根拠の所在 | 確からしさ |
|---|---|---|---|
| `W-28` | **Google Java Style Guide には `Util`・`Utils`・`Helper` への言及が無い。** §5.2.2 が定めるのは「クラス名は `UpperCamelCase`、通常は名詞句」「テストクラスは `Test` で終わる」だけである | google.github.io/styleguide/javaguide.html §5.2.2（2026-09-07 確認） | 二次資料 |
| `W-29` | **JDK 自身が `Util` を名前に持つ。** `java.util.Objects` は Java SE 21 の API 仕様で This class consists of static utility methods for operating on objects と説明されている | docs.oracle.com Java SE 21 API（2026-09-07 確認） | 一次資料 |
| `W-30` | `java.util.Objects` は `public final class` であり、メソッドはすべて `static` である。**状態を持たない** | 同上 | 一次資料 |
| `W-31` | したがって「`Util` という語を使うな」という規則を、公開情報からは支持できない。**支持できるのは、状態を持つクラスに `Util` を付けるなという、より狭い規則である** | `W-28` から `W-30` の整理 | 推測 |
| `W-32` | Google のレビュー基準は名前を長さで評価する。A good name is long enough to fully communicate what the item is or does, without being so long that it becomes hard to read | google.github.io/eng-practices（2026-09-07 確認） | 二次資料 |
| `W-33` | 同じ文書は、そもそも置き場所を問う。Does this change belong in your codebase, or in a library? を設計のレビュー項目に挙げる。**`Util` に入れたくなったものは、置き場所の問題である** | 同上 | 二次資料 |

### Q5 変更容易性と YAGNI

| 主張ID | 主張 | 根拠の所在 | 確からしさ |
|---|---|---|---|
| `W-34` | YAGNI の対象は presumptive feature（あると見込んだ機能）である。将来必要になると見込んだ能力を今作らない、という主張である | martinfowler.com/bliki/Yagni.html（2026-09-07 確認、2015-05-26 付） | 二次資料 |
| `W-35` | **Fowler は適用範囲を明示的に限定している。** Yagni only applies to capabilities built into the software to support a presumptive feature, it does not apply to effort to make the software easier to modify | 同上 | 二次資料 |
| `W-36` | **したがって「変更容易性」と YAGNI は、原典の定義ではぶつからない。** ぶつかっているように見えるのは、見込み機能のための抽象化を「変更容易性のための投資」と呼び替えているときである | 同上 | 推測（整理は調べた者による） |
| `W-37` | Fowler は YAGNI を内部品質の言い訳にすることを否定する。Yagni is not a justification for neglecting the health of your code base. Yagni requires (and enables) malleable code | 同上 | 二次資料 |
| `W-38` | 見込み機能の費用は4つに分かれる。cost of build（作る費用）、cost of delay（他の機能が遅れる費用）、cost of carry（抱えている間の複雑さの費用）、cost of repair（後で作り直す費用） | 同上 | 二次資料 |
| `W-39` | Google のレビュー基準も同じ向きである。Encourage developers to solve the problem they know needs to be solved now, not the problem that the developer speculates might need to be solved in the future | google.github.io/eng-practices（2026-09-07 確認） | 二次資料 |
| `W-40` | 同文書は判断の時期も述べる。The future problem should be solved once it arrives and you can see its actual shape and requirements in the physical universe。**将来の要件は形が見えてから解く** | 同上 | 二次資料 |
| `W-41` | Fowler は設計への投資が報われるまでの時間を「設計の payoff line」と呼び、usually weeks not months（普通は数か月ではなく数週間）と見積もる | martinfowler.com/bliki/DesignStaminaHypothesis.html（2026-09-07 確認、2007-06-20 付） | 二次資料 |
| `W-42` | **ただし Fowler 本人が、これは証明ではないと断っている。** I call this a hypothesis because it is a conjecture, there is no objective proof that this phenomenon actually occurs。生産性も設計品質も測れないためである | 同上 | 二次資料 |
| `W-43` | Fowler は「進化的設計」が規律なしでは破綻するとする。In its common usage, evolutionary design is a disaster. The design ends up being the aggregation of a bunch of ad-hoc tactical decisions | martinfowler.com/articles/designDead.html（2026-09-07 確認、2004-05 改訂） | 二次資料 |
| `W-44` | 同記事は Beck の「単純な設計」の4条件を重要度順に挙げる。すべてのテストが通る、重複が無い、意図をすべて表している、クラスとメソッドの数が最小である | 同上 | 二次資料 |
| `W-45` | 同記事は、先行設計を全否定していない。there is a role for a broad starting point architecture（大まかな出発点としてのアーキテクチャには役割がある）とし、ただし these early architectural decisions aren't expected to be set in stone と続ける | 同上 | 二次資料 |
| `W-52` | **Fowler は線引きの規則を1文で書いている。** yagni only applies when you introduce extra complexity now that you won't take advantage of until later（YAGNI が当てはまるのは、今は使わない複雑さを今持ち込むときだけである）。複雑さが増えないなら YAGNI を持ち出す理由は無い、と続ける | martinfowler.com/bliki/Yagni.html（2026-09-07 確認） | 二次資料 |
| `W-53` | **同記事は判断のための思考実験を示す。** 「その能力が必要になったときに、後から入れるとしたらどんなリファクタリングが要るか」を想像させる。多くの場合、それだけで後から足しても大して高くつかないと分かる | 同上 | 二次資料 |
| `W-54` | 同じ思考実験のもう1つの結果として、「今やるのは簡単で、複雑さをほとんど増やさず、後の費用を大きく下げるもの」が見つかることがある。例はエラーメッセージを直書きせずルックアップ表にすることである | 同上 | 二次資料 |
| `W-55` | 同記事は Jeremy Miller の言葉を引く。使われることのない拡張点は、無駄なだけでなく邪魔にもなる | 同上 | 二次資料 |
| `W-56` | **同記事は YAGNI の失敗も認めている。** 早く手を打っていればずっと安く済んだ場面はある。ただし事前には見分けにくく、成功例より記憶に残りやすい（利用可能性バイアス）とする。**「まれである」は Fowler 本人の感触（My sense is）である** | 同上 | 二次資料 |
| `W-57` | **Fowler が挙げる「見込みが外れる確率は少なくとも3分の2」の出所は測定である。** Microsoft の Experimentation Platform チームの報告であり、Fowler 自身が脚注で出典を示している | 同上（脚注3） | 二次資料 |
| `W-58` | 測定の中身は次のとおりである。Microsoft で、主要な指標を改善するために設計され、適切に設計・実行された対照実験を評価したところ、その指標を実際に改善したのは約3分の1だけだった | Kohavi ほか（2009）§5.1（2026-09-07 確認） | 一次資料 |
| `W-59` | 同報告は、アイデアを10個そのまま出した場合の内訳を、良い3分の1・変化なし3分の1・悪い3分の1と見積もる。**これは ExP チームの当時の推定値であり、測定値ではないと本文に書いてある** | Kohavi ほか（2009）§4（2026-09-07 確認） | 一次資料 |
| `W-60` | 同報告は、同種の結果が社外にもあるとする。QualPro 社は22年間に15万件の業務改善案を試験し、重要な意思決定と改善案の75%は成果に影響しないか、むしろ悪化させたと報告している | Kohavi ほか（2009）§5.1（2026-09-07 確認） | 二次資料（同報告による他社の引用） |
| `W-61` | **測定の対象は、Web 製品の機能案が指標を改善するかどうかである。** 「将来に備えた抽象化が後で役に立つか」を測ったものではない。**この数値を設計の抽象化に当てはめるのは外挿である** | `W-58` の原典を読んだうえでの整理 | 推測 |

### Q6 デザインパターンの使いどころ

| 主張ID | 主張 | 根拠の所在 | 確からしさ |
|---|---|---|---|
| `W-46` | **Fowler はパターンを使うかどうかの判断基準を1つの問いに落としている。** When you insist on using a pattern, ask, "What repetition is this removing?" 答えられないなら使わないほうがよい、とする | IEEE Software 2001年1-2月号 p.99（2026-09-07 確認） | 一次資料 |
| `W-47` | 同コラムは、パターンを覚えている効用を「早く着く」ことに限定する。重複を消そうとすれば Template Method に相当する構造には自力でも到達でき、Knowing the pattern just gets you there quicker と書く | 同上 | 一次資料 |
| `W-48` | 同コラムが示す実例は、ASCII 出力と HTML 出力の2メソッドである。全体の流れ（ヘッダ・明細の繰り返し・フッタ）が同じで、各段の中身だけが違う。共通のインタフェースを1つ立てて差分を実装に押し出す | 同上 p.98（2026-09-07 確認） | 一次資料 |
| `W-49` | Fowler はパターンの過剰適用を明確に害とする。one of the problems with people who have just read a pattern is that they insist on using it, which often leads to more complicated designs | 同上 p.99 | 一次資料 |
| `W-50` | 同じ趣旨が「Is Design Dead?」にもある。32行に16個のパターンを詰め込む書き手を戯画として挙げ、Concentrate on when to apply the pattern (not too early) と助言する | martinfowler.com/articles/designDead.html（2026-09-07 確認） | 二次資料 |
| `W-51` | **同記事は撤去も勧める。** If you put a pattern in, and later realize that it isn't pulling its weight - don't be afraid to take it out again。パターンは入れたら固定するものではない | 同上 | 二次資料 |

## 答えられなかったこと

| 問い | 状態 | 理由 |
|---|---|---|
| `Q1` の「凝集度」の一次定義 | 調べたが読めない | Stevens・Myers・Constantine「Structured Design」（IBM Systems Journal 13(2)、1974）が凝集度・結合度の原典である。ACM Digital Library の該当ページ（`https://dl.acm.org/doi/10.1147/sj.132.0115`）は 2026-09-07 の時点で HTTP 403 を返し、本体を読めなかった。無料で読める全文は写しのみで、忠実性を確認できない |
| `Q6` のパターンの定義と一覧 | 調べていない | GoF『Design Patterns』（Gamma ほか、1994）の本体が手元に無い。書籍側の調査（`SRC-DESIGN-002` Head First デザインパターン）に任せる |
| `Q3` の「1パッケージあたりのクラス数」などの数値 | 調べたが見つからない | 上の12件のいずれにも、パッケージの大きさに関する数値の基準は無い。Martin は数値ではなく CCP・CRP・REP という判断規準を置いている |
| `Q4` の「`Manager` を避けよ」という規則 | 調べたが見つからない | Google Java Style Guide、Google Engineering Practices のどちらにも `Manager`・`Helper`・`Common` への言及が無い。書籍側に委ねる |
| `Q2` の食い違いの決着（`W-15`） | 調べたが見つからない | Fowler と Metz のどちらが正しいかを判定できる測定結果を、公開情報の中に見つけられなかった。どちらも経験に基づく主張である |
| `Q5` の「抽象化の投資が回収される時期」 | 調べたが見つからない | `W-41` の「数週間」は Fowler 本人が推測（conjecture）だと明言している。`W-58` の3分の1は測定だが、対象が違う（`W-61`）。**設計の抽象化そのものを測った結果は見つからなかった** |

## 転載の確認

**連続する3文以上の転載は無い。** 英語の原文を引いた箇所はいずれも1文以内であり、原則の定義と本人の言い切りに限っている。`granularity.pdf` の原則本文（REP・CRP・CCP）は、原典で大文字の箇条として置かれた1文から2文であり、定義そのものである。

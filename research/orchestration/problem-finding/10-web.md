# 公開情報の調査 — 問題の見つけ方

| 項目 | 内容 |
|---|---|
| 題材 | 問題の見つけ方（具体と抽象の往復、要求の掘り下げ、原因の切り分け） |
| 答える問い | `Q1`、`Q2`、`Q3`、`Q4`、`Q5`（`00-plan.md` の番号） |
| 調べた者 | Claude（Opus 5）。司会が兼ねる |
| 調べた日 | 2026-09-08 |
| 調べた範囲 | 下の「開いた資料」の12件を本文まで開いた。PDF4件は取り出して全文を検索した。ISO/IEC/IEEE 29148、Leveson 2004、Card 2017、Wason 1960、Curtis ほか1988 は本文を読めていない |

## 開いた資料

**URLと確認日を1件ずつ記す。** 出典IDは振らない。採番は `research/sources.md` が一次情報である。

| 略称 | 資料 | URL | 確認日 | 段 |
|---|---|---|---|---|
| SRE-12 | Google「Site Reliability Engineering」12章 Effective Troubleshooting | https://sre.google/sre-book/effective-troubleshooting/ | 2026-09-08 | 公開されている社内標準 |
| SRE-6 | Google「Site Reliability Engineering」6章 Monitoring Distributed Systems | https://sre.google/sre-book/monitoring-distributed-systems/ | 2026-09-08 | 公開されている社内標準 |
| SRE-15 | Google「Site Reliability Engineering」15章 Postmortem Culture | https://sre.google/sre-book/postmortem-culture/ | 2026-09-08 | 公開されている社内標準 |
| IREB | IREB CPRE Foundation Level Syllabus v3.2.0（2024-02-26、Stan Bühne・Martin Glinz） | https://isqi.org/media/7f/9a/3e/1744288053/cpre_foundationlevel_syllabus_EN_v.3.2.pdf | 2026-09-08 | 資格制度の本体文書 |
| NSB | Frederick P. Brooks, Jr.「No Silver Bullet: Essence and Accidents of Software Engineering」UNC TR86-020（1986年9月） | http://www.cs.unc.edu/techreports/86-020.pdf | 2026-09-08 | 著者の技術報告（IEEE Computer 1987年4月号の原稿） |
| EWD340 | Edsger W. Dijkstra「The Humble Programmer」EWD340（1972年 ACM チューリング賞講演） | https://www.cs.utexas.edu/~EWD/transcriptions/EWD03xx/EWD340.html | 2026-09-08 | 著者本人の草稿を大学が公開したもの |
| DD | Andreas Zeller「Isolating Failure-Inducing Input」（Zeller・Hildebrandt, IEEE TSE 28(2), 2002 の原稿） | https://homes.cs.washington.edu/~mernst/teaching/6.893/readings/zeller-tse.pdf | 2026-09-08 | 査読つき論文の原稿 |
| BISECT | git-bisect の公式マニュアル | https://git-scm.com/docs/git-bisect | 2026-09-08 | 道具の公式文書 |
| COOK | Richard I. Cook「How Complex Systems Fail」（Cognitive Technologies Laboratory, University of Chicago、1998・1999・2000） | https://how.complexsystems.fail/ | 2026-09-08 | 著者の公開文書 |
| CEE | Hochschild ほか「Cores that don't count」（HotOS '21、2021-05-31 から 06-02、DOI 10.1145/3458336.3465297） | https://sigops.org/s/conferences/hotos/2021/papers/hotos21-s01-hochschild.pdf | 2026-09-08 | 査読つき国際会議の論文 |
| AB95 | Altman・Bland「Absence of evidence is not evidence of absence」（BMJ 1995;311:485、Statistics Notes） | https://www.acsu.buffalo.edu/~wdmccall/os512d/EvidAbs.html | 2026-09-08 | 査読つき雑誌の記事（本文の再掲を読んだ） |
| ERR00J | SEI CERT Oracle Coding Standard for Java, ERR00-J | https://cmu-sei.github.io/secure-coding-standards/sei-cert-oracle-coding-standard-for-java/rules/exceptional-behavior-err/err00-j | 2026-09-08 | 公的研究機関の規約 |
| CWE778 | CWE-778 Insufficient Logging（CWE 4.20） | https://cwe.mitre.org/data/definitions/778.html | 2026-09-08 | 標準化された分類の本体 |
| OWASPLOG | OWASP Logging Cheat Sheet | https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html | 2026-09-08 | 業界団体の公開指針 |

## 主張

### Q1 要望の裏にある本当の問題をどう見つけるか

| 主張ID | 主張 | 根拠の所在 | 確からしさ |
|---|---|---|---|
| `W-01` | 「作るものを正確に決めること」がソフトウェア構築で最も難しい単一の部分である。他のどの部分も、間違えたときにこれほど成果物を損なわず、後から直すのがこれほど難しくない | NSB 5.2（https://www.cs.unc.edu/techreports/86-020.pdf 2026-09-08 確認）。「The hardest single part of building a software system is deciding precisely what to build.」 | 一次資料 |
| `W-02` | 依頼者は自分が何を欲しいかを知らない。何を問われるべきかも知らず、指定に必要な細かさで問題を考えたことがほとんど無い | NSB 5.2（同上）。「the client does not know what he wants」 | 一次資料 |
| `W-03` | 依頼者が技術者と組んでも、作って試す前に要求を完全・正確に指定するのは実際には不可能である | NSB 5.2（同上）。原文は「it is really impossible for a client ... to specify completely, precisely, and correctly」 | 一次資料 |
| `W-04` | したがって、作り手が依頼者のために行う最も重要な仕事は、要求を反復して取り出し、精密にしていくことである | NSB 5.2（同上）。「iterative extraction and refinement of the product requirements」 | 一次資料 |
| `W-05` | 試作は、指定した概念構造を実物にして依頼者が一貫性と使いやすさを試せるようにするためのものである。例外処理や不正入力への応答は作らない | NSB 5.2（同上） | 一次資料 |
| `W-06` | 問題・要求・解決策は切り離せない三つ組であり、この順に現れるとは限らない。解決策の案が先に来て、そこから利用者の必要が生まれることもある | IREB 2.2 原則5（https://isqi.org/media/7f/9a/3e/1744288053/cpre_foundationlevel_syllabus_EN_v.3.2.pdf 2026-09-08 確認、v3.2.0） | 一次資料 |
| `W-07` | それでも、考えるとき・伝えるとき・書くときには、問題と要求と解決策をできる限り分けて扱う。関心の分離によって作業が扱いやすくなるためである | IREB 2.2 原則5（同上） | 一次資料 |
| `W-08` | 問題とは、関係者が現状に満足していない状態を指す。要求は、その問題を無くすか和らげるために関係者が必要とするものを写し取ったものである | IREB 2.2 原則5（同上） | 一次資料 |
| `W-09` | 要求の出どころは3種類に分けられる。関係者、文書、稼働している既存システムである。1つでも欠けると、理解も要求も不完全になる | IREB 4.1（同上） | 一次資料 |
| `W-10` | 関係者に聞くだけでは足りない。多くの関係者は当たり前のこと、すなわち自分の「潜在的な」要求を口に出さないためである | IREB 4.1（同上）。「most stakeholders do not talk about the obvious」 | 一次資料 |
| `W-11` | 引き出しの主眼は、暗黙の要望・希望・期待を明示された要求に変えることにある。集めることではない | IREB 4.2（同上）。「turning implicit demands, wishes, and expectations into explicit requirements」 | 一次資料 |
| `W-12` | 狩野モデルは要求を3つに分ける。魅力的品質（言われない・気づかれていない）、一元的品質（言われる・意識されている）、当たり前品質（言われない・意識の下にある） | IREB 4.2（同上）。原典は Kano ほか1984年 | 一次資料 |
| `W-13` | 引き出しの技法は2系統に分かれる。既にある源から集める技法と、発想を促す技法である。前者は一元的品質と当たり前品質を、後者は魅力的品質を引き出す | IREB 4.2（同上） | 一次資料 |
| `W-14` | 集める技法は4種類に分かれる。質問、協働、観察、成果物に基づくものである | IREB 4.2（同上） | 一次資料 |
| `W-15` | 品質要求と制約は実務で軽く扱われがちである。品質要求を引き出すには ISO/IEC 25010 のような品質モデルを確認表として使う | IREB 4.2（同上） | 一次資料 |
| `W-16` | 制約は、解の空間を狭めうるもの（技術・法・組織・文化・環境）を数え上げて見つける | IREB 4.2（同上） | 一次資料 |
| `W-17` | 単一の要求に対する品質の基準のうち、最も重要なのは適切さ（本当の合意された必要を述べているか）と分かりやすさである。この2つを欠く要求は、他の基準を満たしても役に立たないか有害である | IREB 3.8（同上） | 一次資料 |
| `W-18` | 検証されていない要求は役に立たない。検証は開発後ではなく要求工学の段階で始める。確かめるのは、合意ができているか、必要が十分に覆われているか、文脈の前提が妥当かの3点である | IREB 2.2 原則6、4.4（同上） | 一次資料 |
| `W-19` | 要求の検証で押さえる点は4つである。適切な関係者を巻き込む、欠陥の指摘と修正を分ける、複数の視点から見る、繰り返し行う | IREB 4.4（同上） | 一次資料 |
| `W-20` | 検証の技法は3系統に分かれる。レビュー（ウォークスルー、インスペクション）、探索（試作、アルファ・ベータ試験、A/B試験、MVP）、標本開発である | IREB 4.4（同上） | 一次資料 |
| `W-21` | 関係者が言ったとおりのものを与えることは、期待を超えて必要を満たす機会を逃すことでもある | IREB 2.2 原則8（同上） | 一次資料 |
| `W-22` | 要求が変わるのは事故ではなく通常の状態である。要求工学は「変更を許す」と「要求を安定させる」の2つを同時に追う | IREB 2.2 原則7（同上） | 一次資料 |
| `W-23` | システムは文脈の中に埋め込まれており、文脈を理解せずに正しく指定することはできない。システム境界は最初ははっきりせず、時間とともに動くこともある | IREB 2.2 原則4（同上） | 一次資料 |

### Q2 具体と抽象をどう行き来するか

| 主張ID | 主張 | 根拠の所在 | 確からしさ |
|---|---|---|---|
| `W-24` | 抽象化の目的は曖昧になることではない。絶対的に正確でいられる新しい意味の層を作ることである | EWD340（https://www.cs.utexas.edu/~EWD/transcriptions/EWD03xx/EWD340.html 2026-09-08 確認）。「the purpose of abstracting is not to be vague, but to create a new semantic level in which one can be absolutely precise」 | 一次資料 |
| `W-25` | 有能なプログラマは自分の頭の容量が厳しく限られていることを十分に承知している。だから謙虚に課題へ向かい、巧妙な小技を避ける | EWD340（同上） | 一次資料 |
| `W-26` | ソフトウェアの難しさは、本質（ソフトウェアの性質そのものに内在するもの）と偶有（現在の作り方にたまたま伴うもの）に分けられる | NSB 1章・2章（https://www.cs.unc.edu/techreports/86-020.pdf 2026-09-08 確認）。アリストテレスの区分に倣うと明記している | 一次資料 |
| `W-27` | ソフトウェアの複雑さは本質的な性質であって偶有的なものではない。したがって、複雑さを捨象した記述は、しばしば本質も一緒に捨ててしまう | NSB 2章（同上）。「descriptions of a software entity that abstract away its complexity often abstract away its essence」 | 一次資料 |
| `W-28` | 数学と自然科学は、複雑な現象を単純化した模型で3世紀にわたって前進した。それが成り立ったのは、模型で無視した複雑さが現象の本質ではなかったからである。複雑さが本質であるときには成り立たない | NSB 2章（同上） | 一次資料 |
| `W-29` | 要求は複数の抽象の階層に同時に存在する。適切な階層は、対象と読み手によって決まる | IREB 3.1.2（https://isqi.org/media/7f/9a/3e/1744288053/cpre_foundationlevel_syllabus_EN_v.3.2.pdf 2026-09-08 確認） | 一次資料 |
| `W-30` | 小さい・中くらいの成果物では、要求をおおむね同じ抽象の階層にそろえる。階層が違うものは文書の構成で分けて置く | IREB 3.1.2（同上） | 一次資料 |
| `W-31` | 高い抽象の階層にある要求は、より具体的な複数の要求へ詳細化されうる | IREB 3.1.2（同上） | 一次資料 |
| `W-32` | 詳細に書くほど、想定外のものが出てくる危険は下がるが、書く費用は上がる。詳細の度合いは6つの条件で決める（問題と開発の文脈、共通理解の程度、設計者に残す自由度、素早い反応が得られるか、費用と価値、課された標準と規制） | IREB 3.1.3（同上） | 一次資料 |
| `W-33` | 自然言語の要求で避けるべき落とし穴は4つある。不完全な記述、特定できない名詞、不完全な条件、不完全な比較である | IREB 3.2（同上） | 一次資料 |
| `W-34` | 注意して使うべきものが3つある。受動態、全称の量化子（「すべて」「決して」）、名詞化（動詞から作った名詞。例「認証」）である | IREB 3.2（同上） | 一次資料 |
| `W-35` | 定型（テンプレート）には落とし穴がある。人は中身より枠を埋めることに気を取られ、枠に無い観点は落ちやすい | IREB 3.3（同上） | 一次資料 |

### Q3 不具合の原因をどう切り分けるか

| 主張ID | 主張 | 根拠の所在 | 確からしさ |
|---|---|---|---|
| `W-36` | 障害対応の最初の反応として「根本原因をできるだけ速く見つけよう」とする本能は、無視すべきである。先に、その状況でできる限りシステムを動く状態に戻す | SRE-12「Triage」（https://sre.google/sre-book/effective-troubleshooting/ 2026-09-08 確認）。「Ignore that instinct!」 | 二次資料 |
| `W-37` | 新人パイロットは、緊急時の第一の責務は飛行機を飛ばすことだと教えられる。原因究明は二の次である | SRE-12「Triage」（同上）。同章が使う比喩である | 二次資料 |
| `W-38` | 切り分けは仮説演繹法の適用である。観測とシステムの理解を材料に、原因の仮説を立て、それを試して確かめることを繰り返す | SRE-12「Theory」（同上）。「the hypothetico-deductive method」 | 二次資料 |
| `W-39` | 良い障害報告は3つを含む。期待した振る舞い、実際の振る舞い、可能なら再現の手順である | SRE-12「Problem Report」（同上） | 二次資料 |
| `W-40` | 診断では「何をしているか」を先に突き止め、次に「なぜそれをしているか」と「どこで資源を使い、どこへ出力しているか」を問う | SRE-12「Ask "what," "where," and "why"」（同上） | 二次資料 |
| `W-41` | 「単純化して減らす」ことで、部品の間のつながりを見て、どの部品が正しく動いているかを判定できるようになる。既知のデータを各部品に通す試験が有効である | SRE-12「Simplify and reduce」（同上） | 二次資料 |
| `W-42` | 分割統治は汎用の手法である。階層のどちらかの端から順にたどるのが良い場合が多い | SRE-12「Divide and conquer」（同上） | 二次資料 |
| `W-43` | 大きなシステムでは二分法が速い。半分に割って両側の通信経路を見て、片側が正常と分かれば繰り返す | SRE-12（同上）。原文は bisection | 二次資料 |
| `W-44` | 仮説を試すためにシステムを変えるときは、系統立てて記録しながら行う。そうすれば試験前の状態に戻せる。記録しないと、正体不明の設定のまま動かすことになる | SRE-12「Test and Treat」（同上） | 二次資料 |
| `W-45` | 否定の結果は無視も割引もしてはならない。自分が誤っていたと分かることには大きな価値がある。否定の結果を出した実験は結論が出ている | SRE-12「Negative Results Are Magic」（同上） | 二次資料 |
| `W-46` | 検査を助けるため、記録には複数の詳細度を用意し、プロセスを再起動せずに詳細度を上げられるようにする | SRE-12「Examine」（同上） | 二次資料 |
| `W-47` | 上流と下流の記録を突き合わせる手間を減らすため、一連の呼び出しに一意の要求識別子を通す | SRE-12「Making Troubleshooting Easier」（同上） | 二次資料 |
| `W-48` | テキストの記録は実時間の対処に役立ち、構造化した形式の記録は後からの分析に役立つ | SRE-12「Examine」（同上） | 二次資料 |
| `W-49` | 失敗する入力を最小にする作業は自動化できる。ddmin は、どの1要素を取り除いても失敗が消える状態（1-minimal）まで入力を縮める | DD 3.1、定義10（https://homes.cs.washington.edu/~mernst/teaching/6.893/readings/zeller-tse.pdf 2026-09-08 確認） | 一次資料 |
| `W-50` | Mozilla の事例で、95個の利用者操作は3個に、896行の HTML は1行に縮んだ。自動試験は139回、500MHz の機で35分だった | DD 要旨、4章（同上） | 一次資料 |
| `W-51` | ddmin の試験回数は最悪で n の2乗＋3n である。すべての試験が成功か失敗のどちらかを返す最良の場合は、二分探索と同じ複雑さになる | DD 命題12、命題13（同上） | 一次資料 |
| `W-52` | 障害報告には相反する2つの要請がある。技術者が文脈を再現できるよう具体的でなければならず、同時に、最小の事例ほど一般的な文脈を表すため単純でなければならない | DD 1章（同上） | 一次資料 |
| `W-53` | 最小化した事例は、短い問題記述と洞察をもたらすだけでなく、現在と将来の複数の障害報告を1件に束ねる | DD 1章（同上） | 一次資料 |
| `W-54` | 変更のどれが不具合を入れたかは二分探索で特定できる。675版が残っている時点で「およそ10段」と表示されるとおり、必要な試行は版数の対数に比例する | BISECT（https://git-scm.com/docs/git-bisect 2026-09-08 確認） | 一次資料 |
| `W-55` | 二分探索は自動化できる。判定を script に委ね、終了コード0を正常、1から127（125を除く）を異常、125を「この版は試験できない」として扱う | BISECT（同上） | 一次資料 |
| `W-56` | 探している版の隣を飛ばすと、どちらが最初の異常版かを機械は決められなくなる | BISECT（同上） | 一次資料 |
| `W-57` | 検査例外を握りつぶしてはならない。各 catch は、不変条件が保たれている場合にだけ処理を続けることを保証しなければならない | ERR00J（https://cmu-sei.github.io/secure-coding-standards/sei-cert-oracle-coding-standard-for-java/rules/exceptional-behavior-err/err00-j 2026-09-08 確認）。「Do not suppress or ignore checked exceptions」 | 一次資料 |
| `W-58` | スタックトレースを印字するだけの catch も違反である。例外が起きなかったかのように処理が続くうえ、内部の情報が漏れうる | ERR00J（同上）。非適合例は `catch (IOException ioe) { ioe.printStackTrace(); }` である | 一次資料 |
| `W-59` | 適合する対処は4つである。回復する、外側へ投げ直す、報告の仕組みへ渡して記録する、機微な情報を落としてから報告する | ERR00J（同上） | 一次資料 |
| `W-60` | 事象を記録しない、または重要な項目を落として記録することは、独立した弱点として分類されている（CWE-778） | CWE778（https://cwe.mitre.org/data/definitions/778.html 2026-09-08 確認、CWE 4.20） | 一次資料 |
| `W-61` | 記録が足りないと、何が問題を起こしたかを発見することが困難または不可能になる | CWE778（同上） | 一次資料 |
| `W-62` | 記録すべき項目は「いつ・どこで・誰が・何を」に整理できる。日時、アプリケーションの識別子と版、入口、発生元のアドレス、利用者の識別、事象の種類と深刻度と説明である | OWASPLOG（https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html 2026-09-08 確認） | 二次資料 |
| `W-63` | 記録してはならないものがある。セッション識別子、アクセストークン、パスワード、接続文字列、鍵、決済情報である | OWASPLOG（同上） | 二次資料 |

### Q4 「問題が無い」と「問題を見つけられていない」の区別

| 主張ID | 主張 | 根拠の所在 | 確からしさ |
|---|---|---|---|
| `W-64` | テストは欠陥の存在を示すには非常に有効だが、欠陥の不在を示すには絶望的に不十分である | EWD340（https://www.cs.utexas.edu/~EWD/transcriptions/EWD03xx/EWD340.html 2026-09-08 確認）。「program testing can be a very effective way to show the presence of bugs, but is hopelessly inadequate for showing their absence」 | 一次資料 |
| `W-65` | 差が出なかった試験を「差が無いことを示した」と読むのは誤りである。示されたのはたいてい「差の証拠が無い」ことだけであり、この2つはまったく別の主張である | AB95（https://www.acsu.buffalo.edu/~wdmccall/os512d/EvidAbs.html 2026-09-08 確認）。「These are quite different statements」 | 一次資料 |
| `W-66` | 危険が小さい場合、有意確率は誤解を招きやすい。信頼区間は広くなり、不確かさが大きいことを示す | AB95（同上） | 一次資料 |
| `W-67` | 外形監視は症状に着目したものであり、予測ではなく現に起きている問題を表す。「今、正しく動いていない」を示す | SRE-6（https://sre.google/sre-book/monitoring-distributed-systems/ 2026-09-08 確認）。「Black-box monitoring is symptom-oriented and represents active—not predicted—problems」 | 二次資料 |
| `W-68` | まだ起きていないが差し迫っている問題に対して、外形監視はほとんど役に立たない | SRE-6（同上） | 二次資料 |
| `W-69` | 監視は「何が壊れているか」と「なぜか」の2つを分けて扱う。前者が症状、後者が原因である。この区別は良い監視を書くうえで最も重要なものの1つである | SRE-6「Symptoms Versus Causes」（同上） | 二次資料 |
| `W-70` | 誤りを検出する仕組みに引っかからないまま、計算結果だけが狂う故障が現に存在する。Google はこれを「静かな実行破損（CEE）」と呼び、そういう中核を「mercurial（気まぐれ）」と呼ぶ | CEE 要旨・1章（https://sigops.org/s/conferences/hotos/2021/papers/hotos21-s01-hochschild.pdf 2026-09-08 確認） | 一次資料 |
| `W-71` | この種の故障は、唯一の症状が「誤った計算結果」であるため、長らく「コードベースには必ず未診断の不具合が潜んでいる」という前提に覆い隠されてきた | CEE 1章（同上）。「typically obscured by the undiagnosed software bugs that we always assume lurk within a code base at scale」 | 一次資料 |
| `W-72` | 検出のされ方は4段階に分かれる。即座に検出できて再試行できるもの、機械チェックとして現れるもの、検出はされるが再試行には遅すぎるもの、まったく検出されないものである | CEE 2章（同上） | 一次資料 |
| `W-73` | 発見の速さは、独立した検算があるかどうかで決まる。CEE は「期待した結果と突き合わせる」ことでしか検出できなかった | CEE 1章（同上） | 一次資料 |
| `W-74` | 数千台に数個という頻度でも、規模が大きければ問題として立ち上がってくる。逆に言えば、規模が小さいうちは「無い」と「見えない」を区別できない | CEE 1章（同上）。「a few mercurial cores per several thousand machines」 | 一次資料 |

### Q5 問題の見つけ方が失敗するときの型

| 主張ID | 主張 | 根拠の所在 | 確からしさ |
|---|---|---|---|
| `W-75` | 切り分けが下手になる型は4つ挙げられている。関係のない症状を見る、または指標の意味を取り違える | SRE-12「Common Pitfalls」（https://sre.google/sre-book/effective-troubleshooting/ 2026-09-08 確認） | 二次資料 |
| `W-76` | 第2の型は、仮説を安全かつ有効に試すために、システムや入力や環境をどう変えればよいかを取り違えることである | SRE-12（同上） | 二次資料 |
| `W-77` | 第3の型は、突飛な説を立てること、および過去の障害の原因に飛びつき「一度起きたのだから今回もそれだ」と考えることである | SRE-12（同上） | 二次資料 |
| `W-78` | 第4の型は、偶然の一致や共通原因による見かけの相関を追いかけることである | SRE-12（同上） | 二次資料 |
| `W-79` | 対処としてオッカムの剃刀が挙げられている。「蹄の音を聞いたら、シマウマではなく馬を思え」という医学の言い回しも引かれる。ただし相関は因果ではないとも釘を刺している | SRE-12（同上） | 二次資料 |
| `W-80` | 動いていた計算機は、設定変更や負荷の質の変化のような外力が加わるまで、動いたままでいる傾向がある | SRE-12（同上）。慣性の法則になぞらえた記述である | 二次資料 |
| `W-81` | 事故のあとに1つの「根本原因」を割り当てることは、根本的に誤っている。表に出る失敗は複数の不備を要するため、孤立した「原因」というものは存在しない | COOK 7（https://how.complexsystems.fail/ 2026-09-08 確認）。「Post-accident attribution to a 'root cause' is fundamentally wrong.」 | 一次資料 |
| `W-82` | 大事故には複数の失敗が必要であり、単一点の失敗だけでは足りない。個々の小さな失敗は必要条件にすぎず、組み合わさって初めて十分条件になる | COOK 3（同上） | 一次資料 |
| `W-83` | 「原因」の見方そのものが、次の事故への防御の有効さを制限する | COOK 15（同上） | 一次資料 |
| `W-84` | 複雑なシステムは、失敗の種を混ぜ持ったまま動き続けている。その組み合わせは時とともに変わる | COOK 4（同上） | 一次資料 |
| `W-85` | 後知恵は、事故後の人の働きの評価を歪める | COOK 8（同上） | 一次資料 |
| `W-86` | 変更は新しい形の失敗を持ち込む。失敗を無くすために導入した新技術が、より大きな影響を持つ稀な破局への新しい経路を作ることは珍しくない | COOK 14（同上） | 一次資料 |
| `W-87` | 事後分析の記録は「原因（複数形）」を書くものとして定義されている。単数形ではない | SRE-15（https://sre.google/sre-book/postmortem-culture/ 2026-09-08 確認）。「the root cause(s)」 | 二次資料 |
| `W-88` | 責めない事後分析とは、個人や班を糾弾せずに「寄与した原因」を特定することに集中するものである | SRE-15（同上）。「focus on identifying the contributing causes」 | 二次資料 |
| `W-89` | 責めから調査へ移ると、なぜその人が不完全または誤った情報しか持てなかったのかという系統的な理由が見え、有効な予防策を置けるようになる。人は直せないが、仕組みと手順は直せる | SRE-15（同上）。「You can't 'fix' people, but you can fix systems and processes.」 | 二次資料 |
| `W-90` | 責めを除くと、人は報復を恐れずに問題を上へ上げられるようになる。逆に言えば、責める場では問題が隠される | SRE-15（同上） | 二次資料 |
| `W-91` | 人が「疑わしい」と挙げた中核のうち、深く調べて実際に故障と証明できたのはおよそ半分だった。残りの半分は、濡れ衣と再現できなかったものが混ざっている | CEE 5章（https://sigops.org/s/conferences/hotos/2021/papers/hotos21-s01-hochschild.pdf 2026-09-08 確認）。「roughly half of these human-identified suspects are actually proven」 | 一次資料 |
| `W-92` | 同じ中核が、データ複製の命令とベクトル命令の両方で故障を示した例がある。調べると両者は同じ論理回路を共有していた。命令と欠陥箇所の対応は自明でない | CEE 3章（同上） | 一次資料 |
| `W-93` | 同じ中核から繰り返し信号が出ること（再犯）は、その中核が本当に壊れているという確信を高める。1回の観測では区別がつかない | CEE 5章（同上） | 一次資料 |

## 答えられなかったこと

| 問い | 状態 | 理由 |
|---|---|---|
| `Q1` の規格側の定義 | 調べたが読めない | ISO/IEC/IEEE 29148:2018（要求工学のライフサイクル過程）は有料であり、本体を読めていない。`standards.iteh.ai` と `iso.org` はいずれも本文を返さなかった。**この調査は IREB のシラバスで代えている** |
| `Q1` の実地調査の裏づけ | 調べたが読めない | Curtis・Krasner・Iscoe「A field study of the software design process for large systems」（CACM 31(11)、1988）は、`dl.acm.org` が 2026-09-08 の時点で HTTP 403 を返した。**「要求の揺れと衝突」を実地に測った研究であり、読めていれば `Q1` の裏づけになった** |
| `Q5` の「なぜなぜ」批判 | 調べたが読めない | Card「The problem with '5 whys'」（BMJ Qual Saf 2017;26(8):671-677、DOI 10.1136/bmjqs-2016-005849）は、PubMed が要旨を持たず、`pslhub.org` が HTTP 403 を返した。**書誌情報だけを確認し、主張には採っていない** |
| `Q5` の直線的因果モデルの批判 | 調べたが読めない | Leveson「A New Accident Model for Engineering Safer Systems」（Safety Science 42(4)、2004、p.237-270）は、`sunnyday.mit.edu` への接続が拒否された（`ECONNREFUSED`）。**同じ向きの主張は COOK で代えている** |
| `Q5` の確証バイアスの実験 | 一部だけ調べた | Wason「On the failure to eliminate hypotheses in a conceptual task」（Quarterly Journal of Experimental Psychology 12(3)、1960、p.129-140）は、出版社の頁が本文を返さなかった。**書誌と要旨の水準しか確認していないため、主張に採っていない** |
| `Q2` の公開情報 | 調べたが少ない | 具体と抽象の往復そのものを扱う一次資料は、EWD340 と NSB と IREB 3.1.2 の3件しか見つからなかった。**この問いは書籍側（`SRC-THINK-001`）が主に答える** |
| `Q3` の「一度に1つだけ変える」 | 調べたが見つからない | 実験計画として明示した一次資料を見つけられなかった。SRE-12 の「系統立てて記録しながら変える」が最も近い |
| `Q4` の数量的な基準 | 調べたが見つからない | 「どれだけ観測できていれば『問題が無い』と言えるか」を数値で示した資料は見つからなかった。CEE は逆に、規模を上げないと見えないと述べている |

## 転載の確認

**連続する3文以上の転載は無い。** 引用は1文または句の水準にとどめ、原文を添えたものは短い語句に限っている。

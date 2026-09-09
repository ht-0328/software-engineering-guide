# SRC-EXT-056 Google「Site Reliability Engineering」12章 Effective Troubleshooting

| 項目 | 内容 |
|---|---|
| 資料 | Google「Site Reliability Engineering」12章 Effective Troubleshooting |
| 発行者 | Google |
| URL | https://sre.google/sre-book/effective-troubleshooting/ |
| 確認日 | 2026-09-08 |
| 読んだ範囲 | 章全体を開いた |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| 大きな障害での最初の反応として、根本原因を速く見つけようとする本能は無視する | Triage |
| 先に、その状況でできる限りシステムを動く状態に戻す | Triage |
| 新人パイロットは、緊急時の第一の責務は飛行機を飛ばすことだと教えられる | Triage |
| 良い障害報告は、期待した振る舞い・実際の振る舞い・再現の手順を含む | Problem Report |
| 切り分けは仮説演繹法の適用である | Theory |
| 「何をしているか」を先に突き止め、次に「なぜ」と「どこで」を問う | Diagnose |
| 単純化して減らすことで、部品の間のつながりを見られるようになる | Diagnose |
| 分割統治は汎用の手法である。階層の端から順にたどるのが良い場合が多い | Diagnose |
| 大きなシステムでは二分法が速い。半分に割って通信経路を見る | Diagnose |
| システムを変えるときは系統立てて記録し、試験前の状態に戻せるようにする | Test and Treat |
| 否定の結果は無視も割引もしない。誤っていたと分かることには価値がある | Negative Results Are Magic |
| 記録に複数の詳細度を用意し、再起動せずに詳細度を上げられるようにする | Examine |
| 一連の呼び出しに一意の要求識別子を通す | Making Troubleshooting Easier |
| 切り分けが下手になる型は4つある。無関係な症状、変え方の誤り、突飛な説、見かけの相関である | Common Pitfalls |
| オッカムの剃刀を使う。ただし相関は因果ではない | Common Pitfalls |

## この資料の位置づけ

**公開されている社内標準であり、規格ではない。** Google の運用の考え方を書いたものである。

**`SRC-EXT-057` および `SRC-EXT-058` と同じ書籍の別の章である。** 発行者は1つであり、独立した3件として数えない。

## 使った章

章「06 問題の見つけ方」の観点 `PF-12`、`PF-14`、`PF-15`、`PF-17`。

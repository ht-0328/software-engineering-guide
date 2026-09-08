# SRC-EXT-059 Andreas Zeller「Isolating Failure-Inducing Input」

| 項目 | 内容 |
|---|---|
| 資料 | Andreas Zeller「Isolating Failure-Inducing Input」（Zeller・Hildebrandt, IEEE Transactions on Software Engineering 28(2)、2002年2月 の原稿） |
| 発行者 | Universität Passau（著者の原稿。University of Washington が講義資料として公開） |
| URL | https://homes.cs.washington.edu/~mernst/teaching/6.893/readings/zeller-tse.pdf |
| 確認日 | 2026-09-08 |
| 読んだ範囲 | PDFを取り出して全文を検索した。使ったのは要旨、1章、2章、3.1、4章、6章である |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| 障害報告には相反する2つの要請がある。文脈を再現できる具体性と、最小の事例の単純さである | 1章 |
| 最小の事例は、最も一般的な文脈を表す | 1章 |
| 最小化した事例は、現在と将来の複数の障害報告を1件に束ねる | 1章 |
| ddmin は、どの1要素を取り除いても失敗が消える状態（1-minimal）まで入力を縮める | 3.1、定義10 |
| ddmin の試験回数は、最悪で要素数の2乗に3倍の要素数を加えた値である | 命題12 |
| すべての試験が成功か失敗のどちらかを返す最良の場合は、二分探索と同じ複雑さになる | 命題13 |
| Mozilla を落とす95個の利用者操作は3個に縮んだ | 要旨、4章 |
| Mozilla を落とす896行の HTML は1行に縮んだ | 要旨、4章 |
| 自動試験は139回、500MHz の機で35分だった | 要旨 |

## この資料の位置づけ

**査読つき論文の原稿であり、一次資料である。** 雑誌に載った題は「Simplifying and Isolating Failure-Inducing Input」であり、著者は Zeller と Hildebrandt の2名である。**読んだのは Zeller 単独名義の原稿であり、雑誌に載った版そのものではない。**

**書籍4冊の読んだ範囲に、入力の最小化を扱った記述は無い。** 章「06 問題の見つけ方」の `PF-16` は、この資料だけを根拠にしている。

## 使った章

章「06 問題の見つけ方」の観点 `PF-16`。

# SRC-EXT-050 Kuhn・Wallace・Gallo「Software Fault Interactions and Implications for Software Testing」

| 項目 | 内容 |
|---|---|
| 資料 | Kuhn・Wallace・Gallo「Software Fault Interactions and Implications for Software Testing」（IEEE Transactions on Software Engineering 30(6)、2004年6月、p.418-421） |
| 発行者 | NIST と NASA Goddard（著者の所属）。NIST が原稿を公開 |
| URL | https://csrc.nist.gov/CSRC/media/Projects/automated-combinatorial-testing-for-software/documents/kuhn-wallace-gallo-tse-preprint.pdf |
| 確認日 | 2026-09-08 |
| 読んだ範囲 | PDFを取り出して全文を検索した。使ったのは要旨、1章、4章、表1 である |

## 測定の内容

| 対象 | 2条件までで引き起こされた障害の割合 |
|---|---|
| 医療機器 | 97% |
| Webブラウザ | 76.1% |
| HTTPサーバ | 70.3% |
| NASA の分散システム | 93.3% |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| 障害を引き起こすのに必要な条件の数を FTFI 数と呼ぶ | 表1、4章 |
| 調べた範囲では、FTFI 数が6を超える障害は無かった | 要旨、4章 |
| すべての欠陥が n 個以下の引数の組で起きるなら、n 個組の網羅は網羅テストと実質的に等しい | 要旨 |
| 前提がある。振る舞いが複雑な事象の順序に依存せず、変数が離散的で少数の値しか取らない | 要旨 |
| 入力20個で各10値の対象は、網羅すると10の20乗件になる | 1章 |
| 数百件しか実行できない予算では、可能な場合の1兆分の1にも満たない | 1章 |

## この資料の位置づけ

**査読つき論文の本体であり、一次資料である。** ただし、この論文は過去の4研究をまとめたものである。**独立した4件として数えない。組み合わせの次数を支える測定は、この1件だけである。**

**2004年の測定である。** この文書の最終確認日である2026-09-08 とは、対象のソフトウェアも開発の進め方も異なる。

## 使った章

章「05 テスト」の観点 `TS-11`。

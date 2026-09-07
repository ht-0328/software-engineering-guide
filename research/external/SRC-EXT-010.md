# SRC-EXT-010 Robert C. Martin「Granularity」

| 項目 | 内容 |
|---|---|
| 資料 | Robert C. Martin "Granularity"（Engineering Notebook 欄） |
| 発行者 | The C++ Report（1996年11-12月号）。写しを DePaul 大学が公開 |
| 発行年 | 1996年 |
| URL | https://condor.depaul.edu/dmumaugh/OOT/Design-Principles/granularity.pdf |
| 確認日 | 2026-09-07 |
| 読んだ範囲 | 記事全文 |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| パッケージ結合度の3原則を提示する。REP（Reuse-Release Equivalence）、CRP（Common Reuse）、CCP（Common Closure） | 前半 |
| REP は「再利用の粒度はリリースの粒度である」。再利用の単位は、リリースの単位を下回れない | REP の節 |
| CRP は「1つのパッケージの中のクラスは一緒に再利用される」。1つを使うなら全部を使うことになる粒度で切る | CRP の節 |
| CCP は「1つのパッケージの中のクラスは、同じ種類の変更に対して一緒に閉じている」 | CCP の節 |
| 3原則に順位を付ける。More important than reusability, is maintainability（再利用性より保守性が大切だ）と書き、CCP を REP・CRP に優先させる | CCP の節 |
| パッケージ構成をトップダウンに設計できないと明言する。The package structure cannot be designed from the top down | 終盤 |
| パッケージ依存図は機能の説明ではなく、ビルドの地図（a map of how to build the application）だとする。だから着手時には要らない | 終盤 |
| パッケージ構成はクラスを多く設計したあとに決まり、その後も流動し続けるとする | 終盤 |

## この資料の位置づけ

**掲載誌の記事本体であり、一次資料である。** ただし1996年の文書であり、当時の C++ の開発環境（リリース単位のライブラリ配布、ビルド時間）を前提にしている。**「リリース」を単位に置く議論は、その前提に依存する。**

写しを公開しているのは DePaul 大学であり、版元ではない。**原本との一致は確認していない。**

## 使った章

章「02 設計」の観点 `DS-08`（パッケージを業務領域の単位で分けているか）、`DS-09`（パッケージ間の参照が一方向か）、`DS-11`（パッケージ構成を最初に固定していないか）。

# SRC-EXT-034 Google Engineering Practices「Emergencies」

| 項目 | 内容 |
|---|---|
| 資料 | Google Engineering Practices「Emergencies」（緊急時のレビュー） |
| 発行者 | Google |
| URL | https://google.github.io/eng-practices/review/emergencies.html |
| 確認日 | 2026-09-08 |
| 読んだ範囲 | ページ全体（What Is An Emergency?、What Is Not An Emergency?） |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| 緊急の変更は、重大な問題を即座に解決する小さな変更である | What Is An Emergency? |
| 例として、巻き戻しの代わりに大きな公開を続けられるようにするものがある | What Is An Emergency? |
| 例として、利用者に影響している本番の不具合を直すものがある | What Is An Emergency? |
| 緊急時に優先するのはレビューの速さと、緊急を実際に解決しているかの正しさである | What Is An Emergency? |
| 事後により丁寧なレビューを行う | What Is An Emergency? |
| 緊急ではないものが6つ列挙されている（今週公開したい、著者が長く取り組んだ、など） | What Is Not An Emergency? |
| テストが落ちている変更の巻き戻しは緊急ではない | What Is Not An Emergency? |

## この資料の位置づけ

**Google が公開している社内標準であり、規格ではない。** 章「04 コードレビュー」の観点 `RV-12` は、この1件だけを根拠にしている。

**事後のレビューの時期と担当を決める方法は書かれていない。** 章では、この点を「決着しなかったこと」に入れた。

## 使った章

章「04 コードレビュー」の観点 `RV-12`。

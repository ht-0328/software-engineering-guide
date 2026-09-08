# SRC-EXT-032 Google Engineering Practices「Small CLs」

| 項目 | 内容 |
|---|---|
| 資料 | Google Engineering Practices「Small CLs」（変更を小さく保つ指針） |
| 発行者 | Google |
| URL | https://google.github.io/eng-practices/review/developer/small-cls.html | 
| 確認日 | 2026-09-08 |
| 読んだ範囲 | Why Write Small CLs、What is Small?、When are Large CLs Okay? |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| 100行はおおむね妥当な大きさであり、1000行はたいてい大きすぎる | What is Small? |
| 1ファイル200行の変更は問題ないが、50ファイルに散っていればたいてい大きすぎる | What is Small? |
| 硬い規則は無い、と同文書が明記している | What is Small? |
| レビュアーは、大きすぎるという理由だけで変更を差し戻す裁量を持つ | Why Write Small CLs |
| ファイル全体の削除は1行の変更として数える | When are Large CLs Okay? |
| 自動リファクタリングの道具が生成した変更も例外である | When are Large CLs Okay? |

## この資料の位置づけ

**Google が公開している社内標準であり、規格ではない。** 数値は経験則として示されており、測定の裏づけは書かれていない。**同じ文書が「硬い規則は無い」と述べている点を、章では明記した。**

## 使った章

章「04 コードレビュー」の観点 `RV-06`、`RV-23`。

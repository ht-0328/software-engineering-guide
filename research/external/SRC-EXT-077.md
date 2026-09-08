# SRC-EXT-077 Google Engineering Practices「Writing good CL descriptions」

| 項目 | 内容 |
|---|---|
| 資料 | Google Engineering Practices「Writing good CL descriptions」 |
| 発行者 | Google |
| URL | https://google.github.io/eng-practices/review/developer/cl-descriptions.html |
| 確認日 | 2026-09-09 |
| 読んだ範囲 | ページ全体を開いた |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| 1行目は、命令として書いた完全な文とし、空行を1つ置く | First Line |
| 1行目だけで何をしたかが分かるようにする | 同節 |
| 本文には、解いた問題、その手段を選んだ理由、限界、背景を書く | The Body Is Informative |
| 悪い説明の例は `Fix bug`、`Fix build`、`Add patch`、`Moving code from A to B` である | Bad CL Descriptions |
| 説明は版管理の歴史に恒久的に残り、多数の人に読まれうる | 冒頭 |
| 後で人はこの説明を手がかりに変更を探す | 同節 |
| レビューの過程で変更が変われば説明も直す | Review the Description Before Submitting |

## この資料の位置づけ

**公開された社内標準であり、規格ではない。**

**`SRC-EXT-006` および `SRC-EXT-031` から `SRC-EXT-034` と同じサイトにある。** `SRC-EXT-006` が指すのは `standard.html`、`looking-for.html`、`comments.html`、`speed.html` の4ページである。このページはそのいずれとも重ならないため、新しい番号を振った。

## 使った章

章「07 仕事の進め方」の観点 `WF-33`。

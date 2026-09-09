# SRC-EXT-006 Google Engineering Practices

| 項目 | 内容 |
|---|---|
| 資料 | Google Engineering Practices「What to Look For in a Code Review」ほか3ページ |
| 発行者 | Google |
| URL | https://google.github.io/eng-practices/review/reviewer/looking-for.html |
| 確認日 | 2026-09-07 |
| 読んだ範囲 | `looking-for.html`、`standard.html`、`comments.html`、`speed.html` の4ページ。2026-09-07 と 2026-09-08 の2回読んだ |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| 良い名前とは「何であるか・何をするかを十分に伝えるだけの長さがあり、かつ読みにくくなるほど長くない」名前である | `looking-for.html` の Naming |
| 複雑さは行・関数・クラスの各層で見る | `looking-for.html` の Complexity |
| 「完璧なコード」は存在しない。あるのはより良いコードだけである | `standard.html` |
| 複雑なコードにコメントを足して済ませない。まずコードを単純にする | `comments.html` |
| レビューが遅いとコードの健全性が下がる。整理とリファクタリングが抑制される | `speed.html` |

## この資料の位置づけ

**Google が公開している社内標準であり、規格ではない。** 章「01 良いコードとは何か」では命名の長さの基準（`GC-15`）にだけ使った。**レビューの観点は章「04 コードレビュー」で使った。**

**同じサイトの別の4ページには、別の出典IDを振ってある。** `SRC-EXT-031`（`navigate.html`）、`SRC-EXT-032`（`small-cls.html`）、`SRC-EXT-033`（`pushback.html`）、`SRC-EXT-034`（`emergencies.html`）である。

## 章「04 コードレビュー」で追加して使った記述

**同じ4ページを読み直し、レビューの観点として使った。** 確認日は 2026-09-08 である。

| 記述 | 該当箇所 |
|---|---|
| 観点は12項目で、先頭は Design である | `looking-for.html` |
| レビューで扱う最も重要なものは変更全体の設計である | `looking-for.html` |
| 割り当てられたコードは全行を見る。複数のレビュアーがいる場合は見た範囲を宣言する | `looking-for.html` の Every Line |
| 自分に判断できない領域は、判断できるレビュアーを足す | `looking-for.html` の Every Line |
| 変更行だけでなく、その周りとシステム全体を見て判断する | `looking-for.html` の Context |
| 良い点も伝える。とくに指摘への対応が良かったときに伝える | `looking-for.html` の Good Things |
| スタイルガイドにない純粋な好みの問題を差し戻しの理由にしない | `looking-for.html` の Style |
| その変更がシステム全体のコードの健全性を確実に良くする状態になったら承認する | `standard.html` |
| 技術的な事実とデータが、意見と個人の好みに優先する | `standard.html` |
| 合意できないときは、対面または会議を持ち、最後に技術リードや管理者へ上げる | `standard.html` |
| 必須でない指摘には `Nit:` を付けるか、必須でないと明示する | `standard.html` |
| 指摘は常にコードについて述べ、開発者については述べない | `comments.html` |
| 「何を」ではなく「なぜ」を書く | `comments.html` |
| 問題の指摘と直接の指示の間で釣り合いを取る | `comments.html` |
| 説明で終わらせず、コードをより明確に書き直させる | `comments.html` |
| レビュー要求に応じるまでの上限は1営業日である | `speed.html` |
| 集中を要する作業の途中で、レビューのために自分を中断しない | `speed.html` |
| 指摘を残したまま承認してよい場合が3つある | `speed.html` |
| 分割できない大きな変更でも、設計面の指摘を返す | `speed.html` |

## 使った章

章「01 良いコードとは何か」の観点 `GC-15`。

章「04 コードレビュー」の観点 `RV-05` から `RV-07`、`RV-09` から `RV-11`、`RV-14` から `RV-17`、`RV-24`、`RV-25`。

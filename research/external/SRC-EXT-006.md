# SRC-EXT-006 Google Engineering Practices

| 項目 | 内容 |
|---|---|
| 資料 | Google Engineering Practices「What to Look For in a Code Review」ほか3ページ |
| 発行者 | Google |
| URL | https://google.github.io/eng-practices/review/reviewer/looking-for.html |
| 確認日 | 2026-09-07 |
| 読んだ範囲 | `looking-for.html`、`standard.html`、`comments.html`、`speed.html` の4ページ |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| 良い名前とは「何であるか・何をするかを十分に伝えるだけの長さがあり、かつ読みにくくなるほど長くない」名前である | `looking-for.html` の Naming |
| 複雑さは行・関数・クラスの各層で見る | `looking-for.html` の Complexity |
| 「完璧なコード」は存在しない。あるのはより良いコードだけである | `standard.html` |
| 複雑なコードにコメントを足して済ませない。まずコードを単純にする | `comments.html` |
| レビューが遅いとコードの健全性が下がる。整理とリファクタリングが抑制される | `speed.html` |

## この資料の位置づけ

**Google が公開している社内標準であり、規格ではない。** この章では命名の長さの基準（`GC-15`）にだけ使った。**レビューの観点そのものは章「04 コードレビュー」で扱う。**

## 使った章

章「01 良いコードとは何か」の観点 `GC-15`。

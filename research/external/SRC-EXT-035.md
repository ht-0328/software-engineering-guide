# SRC-EXT-035 Conventional Comments

| 項目 | 内容 |
|---|---|
| 資料 | Conventional Comments（レビューコメントの書式の規約） |
| 発行者 | Paul Slaughter（ライセンスは Creative Commons BY 3.0） |
| URL | https://conventionalcomments.org/ |
| 確認日 | 2026-09-08 |
| 読んだ範囲 | ページ全体。版数の記載を見つけられなかった |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| 書式は `<label> [decorations]: <subject>` と、その下の任意の説明である | Format |
| ラベルは9種類ある（praise、nitpick、suggestion、issue、todo、question、thought、chore、note） | Labels |
| 装飾は3種類ある（`non-blocking`、`blocking`、`if-minor`） | Decorations |
| `non-blocking` は、レビュー対象の受理を妨げないことを表す | Decorations |
| `blocking` は、受理の前に解決すべきことを表す | Decorations |
| この規約が解こうとする問題は「ラベルの無いコメントは不親切である」ことである | Why? |

## この資料の位置づけ

**規約の本体であり、一次資料である。** ただし標準化団体の文書ではなく、個人が公開している規約である。

**章では、ラベル9種類ではなく装飾の2値（`blocking` と `non-blocking`）を根拠に使った。** 強さは2段階であるという主張を支持するのは、装飾の側である。

## 使った章

章「04 コードレビュー」の観点 `RV-20`。

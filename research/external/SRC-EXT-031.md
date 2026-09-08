# SRC-EXT-031 Google Engineering Practices「Navigating a CL in Review」

| 項目 | 内容 |
|---|---|
| 資料 | Google Engineering Practices「Navigating a CL in Review」 |
| 発行者 | Google |
| URL | https://google.github.io/eng-practices/review/reviewer/navigate.html |
| 確認日 | 2026-09-08 |
| 読んだ範囲 | ページ全体（Summary、Step One、Step Two、Step Three） |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| 第1段は変更の説明を読み、この変更にそもそも意味があるかを問うことである | Step One |
| 意味が無い変更なら、そこで止める。細部を調べる時間を使わずに済む | Step One |
| 第2段は、最も大きな論理的変更を含むファイルから見ることである | Step Two |
| 理由の1つは、開発者が変更を出した直後に次の作業を始めることが多い点である | Step Two |
| もう1つの理由は、設計の変更が小さな変更より直すのに時間がかかる点である | Step Two |
| 大きな設計の問題を見つけたら、残りを見る前に返してよい | Step Two |
| 第3段は、残りのファイルを論理的な順序で漏れなく見ることである | Step Three |

## この資料の位置づけ

**Google が公開している社内標準であり、規格ではない。** この文書だけが「見る順序」を3段で示している。**章「04 コードレビュー」の観点 `RV-04` は、この1件だけを根拠にしている。**

## 使った章

章「04 コードレビュー」の観点 `RV-04`。`RV-05` の補強にも使った。

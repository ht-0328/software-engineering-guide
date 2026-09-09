# SRC-EXT-033 Google Engineering Practices「Handling Pushback in Code Reviews」

| 項目 | 内容 |
|---|---|
| 資料 | Google Engineering Practices「Handling Pushback in Code Reviews」 |
| 発行者 | Google |
| URL | https://google.github.io/eng-practices/review/reviewer/pushback.html |
| 確認日 | 2026-09-08 |
| 読んだ範囲 | ページ全体（Who is Right?、Upsetting Developers、Cleaning It Up Later、General Complaints About Strictness） |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| まず著者の主張が正しいかを検討する。著者はコードに近いため、より良い洞察を持っていることがある | Who is Right? |
| 著者が正しくないと判断したら、著者の返答を理解したことを示し、追加の情報を添えて説明する | Who is Right? |
| 「後で別の変更で直す」は認めない。時間が経つほど、その片付けは起きにくくなる | Cleaning It Up Later |
| 周辺の問題に手を出せないときは、不具合票を自分に割り当て、`TODO` のコメントから参照する | Cleaning It Up Later |
| レビューが厳しすぎると言われたときは、レビューの速度を上げるとその不満が薄れる | General Complaints About Strictness |

## この資料の位置づけ

**Google が公開している社内標準であり、規格ではない。** 「後で直す」の禁止は、**今回の変更が持ち込んだ複雑さ**を対象にしている。もとからあった問題については `SRC-CODE-002` 17.4.4 が別の扱いを示す。

## 使った章

章「04 コードレビュー」の観点 `RV-11`、`RV-13`、`RV-24`。

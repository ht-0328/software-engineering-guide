# SRC-EXT-007 Robert C. Martin「The Single Responsibility Principle」

| 項目 | 内容 |
|---|---|
| 資料 | Robert C. Martin "The Single Responsibility Principle" |
| 発行者 | Robert C. Martin（個人。blog.cleancoder.com） |
| 発行日 | 2014-05-08 |
| URL | https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html |
| 確認日 | 2026-09-07 |
| 読んだ範囲 | ページ全文 |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| SRP の定義は「モジュールが変更される理由は1つだけであるべきだ」である | 冒頭の定義 |
| 著者は「変更の理由」を「アクター」と言い直した。アクターとは、そのモジュールへの変更を求める人の集団である | 中盤 |
| 著者は This principle is about people と書く。**単一性の単位は人の集団である** | 中盤 |
| 例は `Employee` クラスである。`calculatePay` は CFO、`reportHours` は COO、`save` は CTO の組織が変更を要求する。アクターが3つあるので責務も3つになる | 例の節 |
| 別の言い方として、同じ理由で変わるものを集め、違う理由で変わるものを分ける、を挙げる。**分ける基準と集める基準は同じ1つである** | 終盤 |
| 違反したときの害は、あるアクターのための変更が別のアクターの機能を壊すことである | 終盤 |

## この資料の位置づけ

**原則の提唱者本人が書いた解説だが、原典ではない。** 原典は書籍 `Agile Software Development, Principles, Patterns, and Practices`（2002）であり、手元に無い。**この文書は2014年に本人が定義を言い直したものであり、原典の記述とは異なる可能性がある。**

規格でも標準化団体の文書でもない。個人が公開している文書である。

## 使った章

章「02 設計」の観点 `DS-01`（責務を「変更する理由」で定義しているか）と `DS-02`（責務の数を、変更を言い出す人で数えているか）。

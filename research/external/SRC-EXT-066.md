# SRC-EXT-066 OWASP Logging Cheat Sheet

| 項目 | 内容 |
|---|---|
| 資料 | OWASP Logging Cheat Sheet |
| 発行者 | OWASP Foundation |
| URL | https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html |
| 確認日 | 2026-09-08 |
| 読んだ範囲 | ページ全体を開いた。使ったのは記録する項目と記録しない項目の2箇所である |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| 記録する項目は「いつ・どこで・誰が・何を」に整理できる | Event Attributes |
| 「いつ」は、日時、事象の発生時刻、やり取りの識別子である | Event Attributes |
| 「どこで」は、アプリケーションの名前と版、入口、ホストである | Event Attributes |
| 「誰が」は、発生元のアドレス、利用者の識別である | Event Attributes |
| 「何を」は、事象の種類、深刻度、安全に関わるかの印、説明である | Event Attributes |
| 記録してはならないものがある。セッション識別子、アクセストークン、パスワードである | Data to Exclude |
| 接続文字列、鍵、決済情報も記録しない | Data to Exclude |

## この資料の位置づけ

**業界団体の公開指針であり、規格ではない。** 対象は安全の観点からの記録であり、障害の切り分けのための文書ではない。**章「06 問題の見つけ方」は、項目の整理の仕方だけを引いている。**

**`SRC-EXT-065` と発行者が違う。** 章「06 問題の見つけ方」の `PF-17` は、この2件と `SRC-TEST-001` 39.3 の3件を根拠にしている。

## 使った章

章「06 問題の見つけ方」の観点 `PF-17`。

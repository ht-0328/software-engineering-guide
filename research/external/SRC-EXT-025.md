# SRC-EXT-025 Alistair Cockburn「Hexagonal Architecture」

| 項目 | 内容 |
|---|---|
| 資料 | Alistair Cockburn「Hexagonal Architecture」（初出 2005-09-04、HaT Technical Report 2005.02） |
| 発行者 | Alistair Cockburn（個人） |
| URL | https://alistair.cockburn.us/hexagonal-architecture/ |
| 確認日 | 2026-09-08 |
| 読んだ範囲 | 「Intent」「Motivation」「Structure」の3節。適用例の節は読んでいない |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| 意図は、利用者・プログラム・自動テスト・バッチのどれからでも同じように駆動できるようにすることである | Intent |
| もう1つの意図は、実行時の装置とデータベースから切り離して開発とテストができるようにすることである | Intent |
| 業務ロジックが画面のコードに入り込むと、変わりやすい表示の細部にテストが依存する | Motivation |
| その結果、自動テストで確かめられなくなる | Motivation |
| 基本規則は「内側のコードが外側へ漏れ出さないこと」である | Structure |
| 内側が業務ロジック、外側が画面・データベース・他システム・テスト足場である | Structure |

## この資料の位置づけ

**パターンの提唱者本人による定義であり、一次資料である。** ただし規格ではなく、個人が公開している文書である。

## 使った章

章「03 アーキテクチャ」の観点 `AR-02`。

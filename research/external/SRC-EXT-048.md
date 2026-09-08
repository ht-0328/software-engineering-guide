# SRC-EXT-048 Andrew Trenk「Test Behavior, Not Implementation」

| 項目 | 内容 |
|---|---|
| 資料 | Andrew Trenk「Testing on the Toilet: Test Behavior, Not Implementation」（2013-08-05） |
| 発行者 | Google Testing Blog |
| URL | https://testing.googleblog.com/2013/08/testing-on-toilet-test-behavior-not.html |
| 確認日 | 2026-09-08 |
| 読んだ範囲 | ページ全体 |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| テストは「何をするか」を確かめ、「どうやるか」は確かめない | 本文 |
| 依存を足すリファクタリングでも、振る舞いが同じならテストの呼び出し部分は変わらない | 本文 |
| 変わるのは準備の部分だけである | 本文 |
| テストは1件につき1つの振る舞いを確かめ、準備・実行・検証の3段で書く | 本文 |

## この資料の位置づけ

**1社の社内標準であり、規格ではない。** `SRC-EXT-047` と同じ発行者であり、独立した2件として数えない。**章「05 テスト」は、書籍側の `SRC-TEST-001` 26.3 と `SRC-CODE-001` 14章を独立の根拠として併記している。**

## 使った章

章「05 テスト」の観点 `TS-24`、`TS-26`。

# SRC-EXT-047 Alex Eagle「Change-Detector Tests Considered Harmful」

| 項目 | 内容 |
|---|---|
| 資料 | Alex Eagle「Testing on the Toilet: Change-Detector Tests Considered Harmful」（2015-01-27） |
| 発行者 | Google Testing Blog |
| URL | https://testing.googleblog.com/2015/01/testing-on-toilet-change-detector-tests.html |
| 確認日 | 2026-09-08 |
| 読んだ範囲 | ページ全体 |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| 実装の詳細を確かめるテストを「変更検知テスト」と呼ぶ | 本文 |
| 依存を模擬に置き換え、内部メソッドが特定の引数で呼ばれたことを確かめる形が典型である | 本文 |
| 変更検知テストは、既存の振る舞いが続いていることしか示さない | 本文 |
| 実装を変えるたびに書き直しになり、安全なリファクタリングを妨げる | 本文 |
| 依存をすべて模擬に置き換えると、依存側の変更を検出できなくなる | 本文 |
| テストは公開インタフェースを通して振る舞いを確かめる | 本文 |

## この資料の位置づけ

**1社の社内標準であり、規格ではない。** 同じ結論に `SRC-TEST-001` 26.3（脆いテスト）が別の言葉で達している。**章「05 テスト」の `TS-24` は、この2件を独立した根拠として扱っている。**

## 使った章

章「05 テスト」の観点 `TS-24`、`TS-25`。

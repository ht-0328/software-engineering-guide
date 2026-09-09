# SRC-EXT-057 Google「Site Reliability Engineering」6章 Monitoring Distributed Systems

| 項目 | 内容 |
|---|---|
| 資料 | Google「Site Reliability Engineering」6章 Monitoring Distributed Systems |
| 発行者 | Google |
| URL | https://sre.google/sre-book/monitoring-distributed-systems/ |
| 確認日 | 2026-09-08 |
| 読んだ範囲 | 章全体を開いた |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| 内部監視は、システムの内側が出す指標に基づく監視である | Definitions |
| 外形監視は、利用者が見るのと同じ外から見える振る舞いを試すものである | Definitions |
| 外形監視は症状に着目し、予測ではなく現に起きている問題を表す | Symptoms Versus Causes |
| まだ起きていないが差し迫っている問題に対して、外形監視はほとんど役に立たない | Symptoms Versus Causes |
| 監視は「何が壊れているか」と「なぜか」を分けて扱う。前者が症状、後者が原因である | Symptoms Versus Causes |
| この区別は、良い監視を書くうえで最も重要なものの1つである | Symptoms Versus Causes |

## この資料の位置づけ

**公開されている社内標準であり、規格ではない。**

**「観測の経路そのものが生きているか」を直接述べた記述は、この章に無い。** 章「06 問題の見つけ方」の `PF-22` は、この章と `SRC-EXT-062` と `SRC-TEST-001` 39.3 から組み立てたものであり、そのことを本文に明記している。

## 使った章

章「06 問題の見つけ方」の観点 `PF-22`。

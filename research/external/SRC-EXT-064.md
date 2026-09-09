# SRC-EXT-064 SEI CERT Oracle Coding Standard for Java, ERR00-J

| 項目 | 内容 |
|---|---|
| 資料 | SEI CERT Oracle Coding Standard for Java, ERR00-J「Do not suppress or ignore checked exceptions」 |
| 発行者 | Software Engineering Institute, Carnegie Mellon University |
| URL | https://cmu-sei.github.io/secure-coding-standards/sei-cert-oracle-coding-standard-for-java/rules/exceptional-behavior-err/err00-j |
| 確認日 | 2026-09-08 |
| 読んだ範囲 | 規則のページ全体を開いた |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| 規則の題は「検査例外を握りつぶしたり無視したりしない」である | 題 |
| 各 `catch` は、不変条件の保たれた状態でだけ処理を続けることを保証しなければならない | 根拠 |
| スタックトレースを印字するだけの `catch` も非適合例である | 非適合例 |
| 例外が起きなかったかのように処理が続くうえ、内部の情報が漏れうる | 非適合例 |
| 適合する対処は、回復する・投げ直す・報告の仕組みへ渡す・機微な情報を落として報告するの4つである | 適合例 |
| 危険度の評価は、深刻度が低、起こりやすさが probable、優先度が P4、水準が L3 である | 危険度の評価 |

## この資料の位置づけ

**公的研究機関が公開する規約であり、規格ではない。** 対象は Java である。

**章「06 問題の見つけ方」の `PF-23` は、この規約と `SRC-EXT-061` 3 の2件を根拠にしている。** 前者は書き方、後者は小さな失敗が組み合わさる仕組みである。

## 使った章

章「06 問題の見つけ方」の観点 `PF-23`。

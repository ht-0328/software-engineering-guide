# SRC-EXT-004 Google Java Style Guide

| 項目 | 内容 |
|---|---|
| 資料 | Google Java Style Guide |
| 発行者 | Google |
| URL | https://google.github.io/styleguide/javaguide.html |
| 確認日 | 2026-09-07 |
| 読んだ範囲 | 第5節「Naming」（5.1 から 5.3）。他の節は読んでいない |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| クラス名は UpperCamelCase の名詞句、メソッド名は lowerCamelCase の動詞句 | §5.2.2、§5.2.3 |
| 定数は UPPER_SNAKE_CASE。定数とは「深く不変で、観測できる副作用を持たない `static final` フィールド」に限る | §5.2.4 |
| フィールド・引数・ローカル変数は lowerCamelCase。`final` であることだけでは定数にならない | §5.2.5、§5.2.6、§5.2.7 |
| 識別子に `name_`、`mName`、`s_name`、`kName` のような接頭辞・接尾辞を付けない | §5.1 |
| 頭字語は1語として扱う。`XMLHTTPRequest` ではなく `XmlHttpRequest` と書く | §5.3 |
| 公開メソッドの引数に1文字の名前を使わない | §5.2.6 |

## この資料の位置づけ

**Google が公開している社内標準であり、規格でも標準化団体の文書でもない。** 表記規約は言語ごとに違うため、手引きの原則としては扱わない。**Java の例を読むための約束として使う。**

## 使った章

章「01 良いコードとは何か」の観点 `GC-10`、`GC-15`、`GC-17`、および「Java の表記規約について」の節。

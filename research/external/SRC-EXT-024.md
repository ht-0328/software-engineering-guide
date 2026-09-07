# SRC-EXT-024 GraphQL 仕様 Section 1「Overview」

| 項目 | 内容 |
|---|---|
| 資料 | GraphQL 仕様 Section 1「Overview」 |
| 発行者 | GraphQL Foundation |
| URL | https://github.com/graphql/graphql-spec/blob/main/spec/Section%201%20--%20Overview.md |
| 確認日 | 2026-09-08 |
| 読んだ範囲 | Section 1「Overview」のみ。Section 2 以降は読んでいない |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| 設計原則「Product-centric」は、画面の要求と、それを書く技術者の要求から出発すると述べる | 設計原則 |
| 設計原則「Client-specified response」では、サービスが能力を公開し、消費の仕方をクライアントが項目の粒度で指定する | 設計原則 |
| GraphQL 以外で書かれた大半のアプリケーションでは、各終端が返すデータの形をサービス側が決める | 設計原則 |
| GraphQL は特定のプログラミング言語も保存の仕組みも要求しない | 冒頭の説明 |
| 任意の計算ができるプログラミング言語ではない | 冒頭の説明 |

## この資料の位置づけ

**仕様書の本文であり、一次資料である。** ただし版を確認できていない。

**公式サイト `https://spec.graphql.org/October2021/` は、2026-09-08 の時点で HTTP 403 を返した。** そのため、`graphql/graphql-spec` リポジトリの `main` ブランチにある原稿を GitHub API で取得して読んだ。**October 2021 版と一致するかを確かめていない。**

## 使った章

章「03 アーキテクチャ」の観点 `AR-17`。

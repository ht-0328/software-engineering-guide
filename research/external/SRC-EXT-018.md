# SRC-EXT-018 Azure Architecture Center「Backends for Frontends pattern」

| 項目 | 内容 |
|---|---|
| 資料 | Azure Architecture Center「Backends for Frontends pattern」（2025-03-19 版） |
| 発行者 | Microsoft |
| URL | https://learn.microsoft.com/en-us/azure/architecture/patterns/backends-for-frontends |
| 確認日 | 2026-09-08 |
| 読んだ範囲 | ページ全体。「Example」の節の Azure 製品の構成は、この手引きでは使っていない |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| BFF は利用者体験に固有の処理だけを扱う。監視や認可のような横断的な関心事は別の仕組みへ分離する | Problems and considerations |
| サービスを増やすと運用負担が増える。生存期間、配備、保守、安全の要求が別々に発生する | Problems and considerations |
| BFF を挟むと中継が1つ増え、遅延が増えることがある | Problems and considerations |
| コードの重複が起きる見込みが高い。重複と、画面ごとの最適化の取引になる | Problems and considerations |
| 項目を指定できる問い合わせ機構を使う場合、BFF の層を別に置く必要が無くなることがある | Solution、Problems and considerations |
| APIゲートウェイとマイクロサービスの組み合わせで足りる場面もある | Problems and considerations |
| 使う場面は4つである。保守負担が大きい、特定の画面向けに最適化したい、汎用バックエンドに個別対応を入れ続けている、特定の画面だけ別の言語が向く | When to use this pattern |
| 向かない場面は2つである。複数の画面が同じか似た要求をする場合と、画面が1つしか無い場合である | When to use this pattern |

## この資料の位置づけ

**Microsoft が公開している設計指針であり、規格でも標準化団体の文書でもない。** 二次資料として扱う。ページ自身が `SRC-EXT-016`（Sam Newman）を出典として挙げている。

**`SRC-ARCH-002` p.554 と食い違う記述がある。** 同書は、画面が1つでもサーバー側の集約量が多ければ BFF に価値があるとする。**章「03 アーキテクチャ」は、一次資料である `SRC-ARCH-002` を採った。**

## 使った章

章「03 アーキテクチャ」の観点 `AR-05`、`AR-07`、`AR-17`。

# SRC-EXT-019 OWASP「Input Validation Cheat Sheet」

| 項目 | 内容 |
|---|---|
| 資料 | OWASP Cheat Sheet Series「Input Validation Cheat Sheet」 |
| 発行者 | OWASP Foundation |
| URL | https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html |
| 確認日 | 2026-09-08 |
| 読んだ範囲 | 「Goals of Input Validation」「Input Validation Strategies」「Client-side vs Server-side Validation」の3節。ファイルアップロードと正規表現の節は読んでいない |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| 入力検証はサーバー側で、アプリケーションの処理がデータを扱う前に行わなければならない | Client-side vs Server-side Validation |
| 画面側の検証は、利用者が JavaScript を無効にするか代理サーバーを使えば迂回できる | Client-side vs Server-side Validation |
| 推奨は両側に置くことである。画面側は利用者体験のため、サーバー側は安全のためである | Client-side vs Server-side Validation |
| 形式の検証は、日付や通貨記号のような構造を持つ項目の構文を強制する | Input Validation Strategies |
| 意味の検証は、開始日が終了日より前か、価格が想定の範囲内かを強制する | Input Validation Strategies |
| 選択肢が決まっている項目でサーバー側の照合に失敗した場合は、改ざんの兆候として重大な事象に記録する | Client-side vs Server-side Validation |
| 入力検証を主たる防御にしてはならない。正しい形式の値に攻撃が含まれることがある | Goals of Input Validation |

## この資料の位置づけ

**非営利団体が公開している指針であり、規格ではない。** 二次資料として扱う。ISO や IETF のような標準化団体の文書ではない。

**画面側とサーバー側に同じ規則を置いたときの同期の方法には触れていない。** 不整合の頻度を測った数値も無い。

## 使った章

章「03 アーキテクチャ」の観点 `AR-09`。

# SRC-EXT-036 GitLab「Code Review Guidelines」

| 項目 | 内容 |
|---|---|
| 資料 | GitLab「Code Review Guidelines」 |
| 発行者 | GitLab |
| URL | https://docs.gitlab.com/development/code_review/ |
| 確認日 | 2026-09-08 |
| 読んだ範囲 | ページ全体を1回読んだ。リンク先の Handbook（レビュー応答のSLO の定義）は開いていない |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| レビュアーは選んだ解法の詳細を見る | Getting your merge request reviewed |
| メンテナはコードベース全体の健全性・品質・一貫性に責任を持つ | Getting your merge request reviewed |
| マージには最低1人のメンテナの承認が要る | Getting your merge request reviewed |
| Conventional Comments の書式を採用している | Reviewing |
| 必須でない提案には `(non-blocking:)` を付ける | Reviewing |
| 非ブロッキングの指摘しか残っていないときは、待たずに次の段階へ進める | Reviewing |
| 多くのプログラミング上の判断は意見である、と認めたうえで、取引を議論して決着させる | Reviewing |
| 承認前の確認項目表を持ち、品質・性能・安全・文書・配備・法令順守の6分野に分かれる | Merge request acceptance checklist |

## この資料の位置づけ

**GitLab が公開している社内標準であり、規格ではない。** この手引きで引いた公開標準は Google と GitLab の2社に偏っている。**章の「根拠の弱いところ」にその旨を書いた。**

**レビュー応答の目安（SLO）の具体的な値は、このページに書かれていない。** Handbook 側のリンク先にあると記されているが、開いていない。

## 使った章

章「04 コードレビュー」の観点 `RV-08`、`RV-10`、`RV-20`。

# SRC-EXT-011 Martin Fowler「Yagni」

| 項目 | 内容 |
|---|---|
| 資料 | Martin Fowler "Yagni" |
| 発行者 | Martin Fowler（個人。martinfowler.com/bliki） |
| 発行日 | 2015-05-26 |
| URL | https://martinfowler.com/bliki/Yagni.html |
| 確認日 | 2026-09-07 |
| 読んだ範囲 | 本文全文と脚注 |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| YAGNI の対象は presumptive feature（あると見込んだ機能）である | 冒頭 |
| **適用範囲を明示的に限定する。** Yagni only applies to capabilities built into the software to support a presumptive feature, it does not apply to effort to make the software easier to modify | 中盤 |
| 内部品質の言い訳にすることを否定する。Yagni is not a justification for neglecting the health of your code base | 中盤 |
| 見込み機能の費用を4つに分ける。作る費用、他の機能が遅れる費用、抱えている間の複雑さの費用、後で作り直す費用 | 中盤 |
| 線引きの規則を1文で書く。yagni only applies when you introduce extra complexity now that you won't take advantage of until later | 中盤 |
| 判断のための思考実験を示す。「その能力が必要になったときに、後から入れるならどんなリファクタリングが要るか」を想像する | 中盤 |
| 思考実験のもう1つの結果として、今やるのは簡単で複雑さをほとんど増やさず後の費用を大きく下げるものが見つかることがある | 中盤 |
| 使われない拡張点は無駄なだけでなく邪魔にもなる、という Jeremy Miller の言葉を引く | 中盤 |
| YAGNI の失敗も認める。早く手を打っていれば安く済んだ場面はあるが、事前には見分けにくいとする。**「まれである」は本人の感触（My sense is）である** | 終盤 |
| 「見込みが外れる確率は少なくとも3分の2」の出所を脚注3で示す。出所は `SRC-EXT-015` である | 脚注3 |

## この資料の位置づけ

**個人が公開している文書であり、規格でも標準化団体の文書でもない。**

**この資料の最も重要な点は、適用範囲の限定である。** 「変更容易性」と YAGNI がぶつかるように見えるのは、見込み機能のための抽象化を変更容易性への投資と呼び替えているときだけである、と読める。

## 使った章

章「02 設計」の観点 `DS-05`（共通化を「目的が同じか」で判断しているか）と `DS-14`（今は使わない複雑さを、今持ち込んでいないか）。

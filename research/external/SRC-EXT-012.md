# SRC-EXT-012 Martin Fowler「Is Design Dead?」

| 項目 | 内容 |
|---|---|
| 資料 | Martin Fowler "Is Design Dead?" |
| 発行者 | Martin Fowler（個人。martinfowler.com） |
| 発行日 | 2000年7月に初出。2004年5月に改訂 |
| URL | https://www.martinfowler.com/articles/designDead.html |
| 確認日 | 2026-09-07 |
| 読んだ範囲 | 記事全文 |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| 規律の無い進化的設計は破綻するとする。In its common usage, evolutionary design is a disaster | 前半 |
| 破綻の形を「その場しのぎの戦術的判断の寄せ集め」と表現する | 前半 |
| Beck の「単純な設計」の4条件を重要度順に挙げる。すべてのテストが通る、重複が無い、意図をすべて表している、クラスとメソッドの数が最小である | 中盤 |
| **先行設計を全否定していない。** there is a role for a broad starting point architecture（大まかな出発点としてのアーキテクチャには役割がある）とする | 中盤 |
| ただし these early architectural decisions aren't expected to be set in stone と続ける。**出発点は固定しない** | 中盤 |
| パターンの詰め込みを戯画として挙げる。32行に16個のパターンを詰め込む書き手の例を示す | パターンの節 |
| 助言は Concentrate on when to apply the pattern (not too early) である | パターンの節 |
| 撤去も勧める。効いていないと分かったパターンは外してよい | パターンの節 |

## この資料の位置づけ

**個人が公開している文書であり、規格でも標準化団体の文書でもない。** 2000年初出・2004年改訂であり、当時の開発手法（Extreme Programming）を前提にした議論である。

## 使った章

章「02 設計」の観点 `DS-11`（パッケージ構成を最初に固定していないか）。**「大まかな出発点」に具体的に何を置くかは、この資料からは決まらなかった。** 決着しなかった論点として章に書いてある。

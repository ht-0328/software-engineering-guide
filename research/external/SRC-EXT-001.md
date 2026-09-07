# SRC-EXT-001 NIST SP 500-235 Structured Testing

| 項目 | 内容 |
|---|---|
| 資料 | NIST Special Publication 500-235 "Structured Testing: A Testing Methodology Using the Cyclomatic Complexity Metric" |
| 発行者 | NIST（米国国立標準技術研究所） |
| 著者 | Arthur H. Watson、Thomas J. McCabe（編集: Dolores R. Wallace） |
| 発行年 | 1996年 |
| URL | https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication500-235.pdf |
| 確認日 | 2026-09-07 |
| 読んだ範囲 | §2.5「Limiting cyclomatic complexity to 10」（p.15-16）。他の節は読んでいない |
| 読み方 | PDFを取得し、`pdftotext -layout` で本文を取り出して読んだ |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| 複雑度を制限する理由は4つ。複雑なモジュールは誤りを含みやすく、理解しにくく、テストしにくく、変更しにくい | §2.5 p.15 |
| McCabe が提案した上限10には裏づけがあるが、上限の数値は決着していない（"remains somewhat controversial"）。15で運用した例もある | §2.5 p.15 |
| 10を超える上限を選んでよいのは、経験のある要員、形式的な設計、コードウォークスルー、網羅的なテスト計画などの条件がそろう場合に限る | §2.5 p.15 |
| 最も有効な方針は「各モジュールの複雑度を10に抑えるか、超えた理由を文書で示すかのどちらかにする」 | §2.5 p.16 |
| 循環的複雑度はテストに必要な経路の数を与える | §2.5 p.16 |
| 指標を小さく見せるために測り方を変えると、テストが各分岐を通らなくなる。複雑度90のモジュールに何もしない10分岐を足して「修正複雑度10」に見せた実例がある | §2.5 p.15-16 |

## この資料の位置づけ

**標準化団体が発行した一次資料である。** 1996年の文書であり、当時の開発環境（言語、道具）を前提にしている。数値そのものについて、文書自身が決着していないと述べている点が重要である。

## 使った章

章「01 良いコードとは何か」の観点 `GC-03`。

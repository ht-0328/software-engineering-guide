# SRC-EXT-027 Barbacci ほか（CMU/SEI-2003-TN-012）

| 項目 | 内容 |
|---|---|
| 資料 | Barbacci、Clements、Lattanze、Northrop、Wood「Using the Architecture Tradeoff Analysis Method (ATAM) to Evaluate the Software Architecture for a Product Line of Avionics Systems: A Case Study」（CMU/SEI-2003-TN-012、2003年7月） |
| 発行者 | Carnegie Mellon University Software Engineering Institute |
| URL | https://www.sei.cmu.edu/documents/2021/2003_004_001_14150.pdf |
| 確認日 | 2026-09-08 |
| 読んだ範囲 | 3章（ATAM の説明）と 4.4（効用木）。事例の詳細（5章以降）は読んでいない |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| 感度点は、ある品質の達成に影響する設計判断である | p.10 |
| 取引点は、複数の品質特性に影響する設計判断である | p.10 |
| リスクは、影響する品質特性から見て問題のある設計判断である | p.10 |
| 非リスクは、影響する品質特性から見て適切な設計判断である | p.10 |
| 効用木は、品質特性の目標を「試験できるシナリオ」に翻訳する | p.12 |
| 効用木は4段である。効用、品質特性、属性の関心事、シナリオの順である | p.13 |
| 葉のシナリオは2つの軸で優先度づけする。重要度と、達成の見込まれるリスクである | p.13 |

## この資料の位置づけ

**SEI の技術報告書の本体であり、一次資料である。** ATAM そのものの定義は CMU/SEI-2000-TR-004 にあるが、そのPDFは `apps.dtic.mil` で HTTP 403 を返したため読めていない。**この報告書は事例研究であり、方法の説明は3章に要約された形で含まれている。**

## 使った章

章「03 アーキテクチャ」の観点 `AR-14`。

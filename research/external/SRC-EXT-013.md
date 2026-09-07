# SRC-EXT-013 Java SE 21 API 仕様 `java.util.Objects`

| 項目 | 内容 |
|---|---|
| 資料 | Java SE 21 API 仕様 クラス `java.util.Objects` |
| 発行者 | Oracle |
| URL | https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Objects.html |
| 確認日 | 2026-09-07 |
| 読んだ範囲 | クラスの宣言、クラスの説明、メソッド一覧 |

## 使った記述

| 記述 | 該当箇所 |
|---|---|
| クラスの説明は This class consists of static utility methods for operating on objects である | クラスの説明 |
| 宣言は `public final class Objects` である。継承できない | クラスの宣言 |
| 公開メソッドはすべて `static` である。**インスタンスの状態を持たない** | メソッド一覧 |

## この資料の位置づけ

**言語処理系の仕様書であり、一次資料である。**

**この資料は「`Util` という語を名前に使うな」という規則を否定する材料として使った。** JDK 自身が `java.util` の下にこのクラスを置き、説明で utility という語を使っている。**公開情報から支持できるのは、状態を持つクラスや業務知識を持つクラスに `Util` を付けるなという、より狭い規則である。**

なお `SRC-EXT-004`（Google Java Style Guide）§5.2.2 にも、`Util`・`Utils`・`Helper` への言及は無かった。**「`Util` を避けよ」を公開情報から支持することはできなかった。**

## 使った章

章「02 設計」の観点 `DS-12`（`Util`・`Common` に業務知識を置いていないか）。

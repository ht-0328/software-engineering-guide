# 02 設計

目の前のクラスを2つに分けるべきか、1つのままでよいか。その場の感覚で決めたことがあるはずである。分け方を誤ったことは、次の仕様変更が来るまで表に出ない。**この章は、その判断を、変更が来る前に説明できる根拠に置き換えるためのものである。**

## この章で判断できること

| 項目 | 内容 |
|---|---|
| 想定読者 | クラスとパッケージの分け方を自分で決める開発者 |
| 答える問い | 責務をどう分けるか。共通化・パッケージ分割・デザインパターンの導入をどう判断するか |
| 読んだあとにできること | 「責務が混ざっている」を、変更を言い出す人の数で説明できる。共通化とパターンの導入を、資料を示して断れる |
| 例示に使う言語 | Java。例示のためであり、原則は言語に依らない |

## 結論

**「1つのことをする」の1つは、変更を言い出す人の数で数える。** 機能の個数でも行数でもない。メソッドごとに、その変更を誰が言い出すかを書き出す。名前が2つ以上出るなら、責務も2つ以上である。

**共通化してよいかは、目的が同じかどうかだけで決める。** 見た目が同じことも、出現の頻度も、判断の材料にしない。似ているだけの2つをまとめると、あとから引数と条件分岐が増え続ける。

**デザインパターンは「どの重複を消しているか」に答えられるときだけ使う。** 答えられないなら、複雑さを足しているだけである。

**根拠**: `SRC-EXT-007`、`SRC-DESIGN-002` p.375（9章）、`SRC-CODE-002` p.126（7.1.3）、`SRC-EXT-009`

## 章01 との境目

**この章は、章「[01 良いコードとは何か](01-good-code.md)」と扱う水準が違う。** 観点IDの接頭辞も違い、この章は `DS-` である。

| 水準 | 扱う章 | 例 |
|---|---|---|
| 1つのメソッドの中 | 章01（`GC-` 番） | メソッドが1つのことをしているか（`GC-04`）、分岐が深くないか（`GC-06`） |
| クラスとクラスの間 | この章（`DS-` 番） | クラスの責務が1つか、2つのクラスをまとめてよいか |
| パッケージとパッケージの間 | この章（`DS-` 番） | 何を単位にパッケージを切るか、参照の向き |

**名前の付け方の一般則は章01 が持つ。** 目的が読み取れるか（`GC-14`）、長さがスコープに合っているか（`GC-15`）は、この章で繰り返さない。**この章が扱うのは、`Util` や `Manager` のように、名前がクラスの構造そのものを歪める場合だけである。**

## 責務の分割

**「1つのことをする」の1つを、どう数えるか。** この節は、これを定義・数え方・当たりの付け方の3つに分けて扱う。3つは同じ分割に到達するとは限らない。定義では1つに見えたものが、数え方では2つになることがある。

| 層 | 内容 |
|---|---|
| 定義 | クラスを変更する理由は1つだけにする |
| 数え方 | その変更を言い出す人の集団を数える |
| 当たりの付け方 | 業務で使われる用語の関心事に対応させる |

**根拠**: `SRC-DESIGN-002` p.375（9章）、`SRC-EXT-007`、`SRC-DESIGN-001` p.25-26（1章）

### DS-01 責務を「変更する理由」で定義しているか

責務は「何をするか」ではなく「どんなときに変更されるか」で語る。**「何をするか」で語ると、責務はいくらでも1つに見える。** 「注文を管理する」も1つ、「システムを動かす」も1つである。変更の理由に言い換えて、初めて数えられるようになる。

『Head Firstデザインパターン 第2版』は「クラスを変更する理由は1つだけにする」を原則として置く。同書は害の仕組みも書く。変更する理由が2つあると、クラスが将来変更される可能性が高くなり、変更したときに設計の2つの側面に影響が及ぶ。

**この原則を提唱したのは Robert C. Martin である。** 本人の解説「The Single Responsibility Principle」は、定義を「各モジュールが変更される理由は1つだけであるべきだ」とする。

**凝集（cohesion）は、この原則より一般的な概念である。** 凝集とは、クラスやモジュールが1つの目的や責務をどれほど密接に支えているかを示す指標である。『Head Firstデザインパターン 第2版』が、両者の関係をそう位置づけている。

**根拠**: `SRC-DESIGN-002` p.375（9章）、`SRC-EXT-007`

### DS-02 責務の数を、変更を言い出す人で数えているか

そのクラスの各メソッドについて、変更を言い出すのが誰かを書き出す。**2つ以上の名前が出たら、責務も2つ以上である。**

Robert C. Martin は2014年の解説で、「変更の理由」を「アクター」と言い直している。アクターとは、そのモジュールへの変更を求める人の集団である。**同文書は「この原則は人についての原則である」と書く。**

同文書の例は `Employee` クラスである。`calculatePay` の変更は CFO の組織が、`reportHours` の変更は COO の組織が、`save` の変更は CTO の組織が言い出す。**アクターが3つあるので、責務は3つである。**

同文書が挙げる害は、あるアクターのための変更が別のアクターの機能を壊すことである。顧客と管理者を最も怖がらせるのは、自分が頼んだ変更と無関係に見える故障だとする。

**悪い例**

```java
public class Employee {
    private final String name;
    private final int workedHours;

    public Employee(String name, int workedHours) {
        this.name = name;
        this.workedHours = workedHours;
    }

    // 経理部門が規定を変えたときに変わる
    public int calculatePay() {
        return workedHours * 2000;
    }

    // 業務部門が集計の様式を変えたときに変わる
    public String reportHours() {
        return name + ": " + workedHours + "h";
    }

    // 情報システム部門が保存先を変えたときに変わる
    public void save() {
        // データベースへ書き込む
    }
}
```

**良い例**

```java
public record EmployeeData(String name, int workedHours) {
}

public class PayCalculator {
    private static final int HOURLY_WAGE = 2000;

    public int calculate(EmployeeData employee) {
        return employee.workedHours() * HOURLY_WAGE;
    }
}

public class HoursReporter {
    public String report(EmployeeData employee) {
        return employee.name() + ": " + employee.workedHours() + "h";
    }
}

public class EmployeeRepository {
    public void save(EmployeeData employee) {
        // データベースへ書き込む
    }
}
```

**なぜ悪いのか**: 3つの部門が同じファイルを直しに来る。経理部門の依頼で `calculatePay` を直したときに、`reportHours` が壊れる可能性がある。壊れた側の部門は、自分が何も頼んでいないのに機能が止まったと受け取る。**故障の原因を説明することが難しくなる。**

**なぜ良いのか**: 部門ごとにファイルが分かれる。経理部門の依頼は `PayCalculator` の中で閉じ、他の2つは触らない。どのクラスを直せばよいかが、依頼してきた部門から決まる。

**数えるのはアクターであり、組織図ではない。** 部門の名前がそのままクラスになるとは限らない。同じ部門の中に、変更を言い出す集団が2つあることもある。

**根拠**: `SRC-EXT-007`

### DS-03 クラスの単位が、業務で使う言葉に対応しているか

クラスの区切り方を、業務の担当者が会話で使う言葉に合わせる。**仕様変更の依頼書に出てくる語が、そのままクラスとして存在するかを見る。**

『現場で役立つシステム設計の原則』は、送料クラスの例で「送料クラスの関心事は送料だけ」と書く。特定の関心事に特化した小さなクラスが、コードの見通しを良くし、変更をやりやすくするとする。

**業務で使われる用語に対応するクラスを、同書はドメインオブジェクトと呼ぶ。** 分析で発見した業務の構造とプログラムの構造が一致していれば、変更が楽で安全になると述べる。修正や拡張が必要になったとき、どこに何が書いてあるかも特定しやすくなる。

『システム開発と「具体と抽象」』は、この考え方を抽象化の側から支える。オブジェクト指向を、現実世界の事象をどの粒度で捉え、どこまでを共通化し、どこを個別差異として扱うかという抽象化の設計思想と位置づける。

**この観点が見るのは、名前ではなくクラスの区切り方である。** 名前の付け方そのものは章01 が扱う。目的が読み取れるか（`GC-14`）と、長さがスコープに合っているか（`GC-15`）を先に読む。業務の言葉が3つあるのにクラスが1つなら、区切り方の問題である。

**根拠**: `SRC-DESIGN-001` p.25-26（1章）、`SRC-THINK-001` p.64（2章）

### DS-04 クラスの大きさを目標にしていないか

「クラスは何行まで」という上限を、合否の基準として運用しない。**大きさは結果であって、目標ではない。**

『現場で役立つシステム設計の原則』は、大きさを結果として扱う。業務の関心事の単位で記述した結果が短いメソッドや小さなクラスになるなら、積極的にそうすべきだと書く。**大きさを先に決めていない。**

**この章は、クラスの行数の目安を書かない。** 『良いコード／悪いコードで学ぶ設計入門』には「だいたいは100行程度、多くても200行程度になります」という記述がある。**この数値に測定の裏づけは示されていない。** 章01 の `GC-03`（指標を目標値にしていないか）と同じ立場をとる。根拠も、NIST SP 500-235 と Martin Fowler「TestCoverage」の2件に置く。

行数が増えたこと自体は合図になる。合図として使い、合否には使わない。**行数を見て責務を数え直すのはよく、行数を減らすために責務を分けるのは順序が逆である。**

**根拠**: `SRC-DESIGN-001` p.26（1章）、`SRC-CODE-002` p.144、`SRC-EXT-001` §2.5、`SRC-EXT-003`

## 共通化の判断

**同じに見えるコードを、まとめてよいときと、まとめてはいけないときがある。** 判定は1つだけであり、目的が同じかどうかを見る。この節は、その判定と、判定を誤ってまとめてしまったあとの戻し方を扱う。

### DS-05 共通化を「目的が同じか」で判断しているか

2つのコードをまとめる理由が「同じに見えるから」になっていないかを見る。**まとめてよいのは、目的（変更の理由）が同じときだけである。**

『良いコード／悪いコードで学ぶ設計入門』は、DRY 原則を「コードの重複を許すな」と解釈するのは誤りだとする。原典である『新装版 達人プログラマー』の文は「すべての知識はシステム内において、単一、かつ明確な、そして信頼できる表現になっていなければならない」である。**対象は知識であって、コードの字面ではない。** 同書は脚注で、コードの重複を許さない原則は DRY ではなく OAOO（Once and Only Once）だと区別している。

**同書が示す判断基準は1つである。「頻度の観点ではなく、目的が同じかどうかで判断しましょう」。** 同書は「DRY 原則にしたがって共通化しすぎるのは良くない」という言い方も明確に否定する。**問題は共通化の量ではない。**

『現場で役立つシステム設計の原則』は、別の例で同じ結論に達する。出荷期日と支払期日は、扱うデータや計算のロジックが似ていても、`ShippingDueDate` と `PaymentDueDate` に分けるべきだとする。理由は「それぞれ異なる理由により、異なる約束事が存在する」ことである。**この2冊は独立している。**

同書は、共通化を全否定していない。「ほんとうに共通のロジック」は `DueDate` クラスとして残し、2つのクラスから部品として使う。

**悪い例**

```java
public class DueDate {
    private final LocalDate date;
    private final boolean forShipping;

    public DueDate(LocalDate date, boolean forShipping) {
        this.date = date;
        this.forShipping = forShipping;
    }

    public AlertType alertPriority(LocalDate today) {
        if (forShipping) {
            return today.isAfter(date) ? AlertType.URGENT : AlertType.NONE;
        }
        return today.isAfter(date.plusDays(3)) ? AlertType.HIGH : AlertType.NONE;
    }
}
```

**良い例**

```java
public record DueDate(LocalDate value) {
    public boolean isExpiredOn(LocalDate today) {
        return today.isAfter(value);
    }
}

public class ShippingDueDate {
    private final DueDate due;

    public ShippingDueDate(LocalDate value) {
        this.due = new DueDate(value);
    }

    public AlertType alertPriority(LocalDate today) {
        return due.isExpiredOn(today) ? AlertType.URGENT : AlertType.NONE;
    }
}

public class PaymentDueDate {
    private static final int GRACE_DAYS = 3;
    private final DueDate due;

    public PaymentDueDate(LocalDate value) {
        this.due = new DueDate(value.plusDays(GRACE_DAYS));
    }

    public AlertType alertPriority(LocalDate today) {
        return due.isExpiredOn(today) ? AlertType.HIGH : AlertType.NONE;
    }
}
```

**なぜ悪いのか**: `forShipping` は2つの業務ルールを1つのクラスに同居させるための旗である。出荷の猶予日数だけを変えたいときに、支払いの分岐まで読む必要がある。『現場で役立つシステム設計の原則』は、この形の害を2つ挙げる。ルールが変更されたときの思わぬ副作用と、`if` で書き分けたときの見通しの急速な悪化である。**旗の引数そのものの害は章01 の `GC-05` が扱う。**

**なぜ良いのか**: 出荷のルールを変えるときに触るのは `ShippingDueDate` だけである。支払いのルールが増えても、出荷側のコードは読み直さなくてよい。**ほんとうに共通な「期日を過ぎたか」の判定だけが `DueDate` に残る。** 同書が言う「部品として使う」形である。

#### 偶然の重複についての食い違い

「同じに見えるコードは、いつも偶然の重複なのか」という疑問が残る。**公開情報の2件が正面から食い違っている。**

| 資料 | 立場 |
|---|---|
| Martin Fowler「Avoiding Repetition」 | 偶然の重複はある。ただし「まれで見分けやすい」とし、原則として重複は消す側に立つ |
| Sandi Metz「The Wrong Abstraction」 | 「重複は、誤った抽象よりはるかに安い」とし、誤った抽象より重複を選べとする |

**この2つは、実は別のものを指している。** DRY の定義に照らせば、Fowler が消せと言う重複は「同じ知識の重複」である。Metz が高くつくと言う対象は、別の目的をまとめたものである。**この章は、対立していないと判断する。判定は「目的が同じか」1つで足りる。**

**根拠**: `SRC-CODE-002` p.126（7.1.3）、`SRC-DESIGN-001` p.127-128（4章）、`SRC-EXT-008`、`SRC-EXT-009`

### DS-06 継承でコードを共有していないか

コードを共有する目的で `extends` を使わない。**『良いコード／悪いコードで学ぶ設計入門』は「継承は推奨しません」を、自身の立場として明言する。**

理由は依存の向きである。サブクラスはスーパークラスの構造に強く依存する一方で、スーパークラス側はサブクラスを気にせず変更されていく。**そのためサブクラスは壊れやすい。**

同書が示す代案は委譲である。委譲とは、使いたいクラスを `private` なインスタンス変数として持ち、その公開メソッドを呼ぶ形をいう。継承ではなくコンポジション構造にする。

**同書は、継承を共通化の話の続きとして扱っている。** 継承を扱う節は、DRY の誤用を扱う節と同じ第7章にある。

**悪い例**

```java
public class PhysicalAttack {
    public int singleAttackDamage() {
        return 20;
    }

    public int doubleAttackDamage() {
        return singleAttackDamage() * 2;
    }
}

public class FighterPhysicalAttack extends PhysicalAttack {
    @Override
    public int singleAttackDamage() {
        return super.singleAttackDamage() + 20;
    }
}
```

**良い例**

```java
public class PhysicalAttack {
    public int singleAttackDamage() {
        return 20;
    }

    public int doubleAttackDamage() {
        return singleAttackDamage() * 2;
    }
}

public class FighterPhysicalAttack {
    private static final int FIGHTER_BONUS = 20;
    private final PhysicalAttack physicalAttack;

    public FighterPhysicalAttack(PhysicalAttack physicalAttack) {
        this.physicalAttack = physicalAttack;
    }

    public int singleAttackDamage() {
        return physicalAttack.singleAttackDamage() + FIGHTER_BONUS;
    }

    public int doubleAttackDamage() {
        return singleAttackDamage() * 2;
    }
}
```

**なぜ悪いのか**: `doubleAttackDamage` はスーパークラスにあるが、内部で `singleAttackDamage` を呼ぶ。サブクラスがそれをオーバーライドしたため、ボーナスが2回加算される。**サブクラスが正しいかを判定するには、スーパークラスの実装の中身まで読む必要がある。** スーパークラス側が `doubleAttackDamage` の中身を変えれば、サブクラスは何も変えていないのに壊れる。

**なぜ良いのか**: `FighterPhysicalAttack` は `PhysicalAttack` の公開メソッドしか使わない。加算する場所が1つに決まり、二重加算が起こらない。**依存が公開された面だけに限られるため、スーパークラスの内部の変更に巻き込まれない。**

継承そのものを禁じているわけではない。同書が問題にしているのは、コードを共有する目的で使う実装継承である。**振る舞いを切り替える目的で `interface` を実装することは、この観点の対象ではない。** その使い方は `DS-16` のパターンの節で扱う。

**根拠**: `SRC-CODE-002` p.128-131（7.2、7.2.1、7.2.2）

### DS-07 誤った共通化を、元に戻してから分け直しているか

まとめたものが合わなくなったとき、引数と条件分岐を足して延命しない。**元に戻してから、もう一度分け直す。**

Sandi Metz「The Wrong Abstraction」は、抽象が劣化する道筋を8段で示す。重複を見つけて抽象に抜き出す、時間が経つ、ほぼ合う新要件が来る、引数と条件分岐を足す、これを繰り返して理解できないコードになる、次の担当者が引き継ぐ。**同文書は、抽象を捨てられない理由を埋没費用の誤謬に帰する。** 埋没費用の誤謬とは、すでに払った費用が惜しくて判断を曲げることをいう。作り込んだものほど残したくなる圧力が働く。

同文書の処方は「元に戻す」である。抽象を全呼び出し元へ展開し直し（inline）、呼び出し元ごとに不要な部分を消す。**「抽象が誤っているとき、前へ進む最も速い道は後ろである」**とする。

『良いコード／悪いコードで学ぶ設計入門』も同じ向きの記述を持つ。業務理解が進んで目的が別だと分かった段階で、共通化を解く。

全部を捨てる必要は無い。『現場で役立つシステム設計の原則』は、ほんとうに共通のロジックは部品として残せとする。**展開し直したあとに、もう一度「目的が同じか」（`DS-05`）で判定する。**

**Sandi Metz の文書は二次資料である。** 個人の公開文書であり、規格でも査読つき論文でもない。この章が採用しているのは、手順の記述がここにしか無いためである。

**根拠**: `SRC-EXT-008`、`SRC-CODE-002` p.128（7.1.3）、`SRC-DESIGN-001` p.127（4章）

## パッケージ構成

**何を単位にパッケージを分けるか。** 3つの独立した資料が、別々の語彙で同じ結論に達している。一緒に変わるものを一緒に置く、という結論である。この節は、単位の決め方と参照の向き、見せる範囲と動かし方を扱う。

| 資料 | 語彙 | 主張 |
|---|---|---|
| Robert C. Martin「Granularity」 | 共通閉鎖の原則（CCP） | 同じ種類の変更に対して一緒に閉じるクラスを、1つのパッケージに集める |
| 『良いコード／悪いコードで学ぶ設計入門』 | 概念の種類 | 概念として強く関係し合うものどうしを一緒にする |
| 『現場で役立つシステム設計の原則』 | 業務の関心事 | ドメインオブジェクトを関心事の単位でグルーピングする |

**根拠**: `SRC-EXT-010`、`SRC-CODE-002` p.226-228（10.9）、`SRC-DESIGN-001` p.85-89（3章）

### DS-08 パッケージを業務領域の単位で分けているか

フォルダの名前が、業務の領域を指しているかを見る。**設計パターン名や技術の層の名前になっていないか。**

『良いコード／悪いコードで学ぶ設計入門』は、技術的な特徴が似ているものどうしでフォルダ分けすることを「技術駆動パッケージング」と呼ぶ。**この呼び名は同書の著者のものではなく、脚注で外部の記事を出所として挙げている。**

同書は害を具体的に示す。`発注金額` は名前から注文関連に見えるが、実際は在庫ユースケースで使う。うっかり注文側で使われるとバグになる。

Robert C. Martin「Granularity」は、この判断に順位まで与える。**「再利用性より、保守性のほうが大切だ」と本文に書き、CCP を再利用の原則（REP・CRP）より優先させる。**

**悪い例**

```text
src/
├── usecases/
│   ├── InventoryUseCase.java
│   ├── OrderUseCase.java
│   └── PaymentUseCase.java
├── entities/
│   ├── StockInEntity.java
│   ├── CartEntity.java
│   ├── OrderEntity.java
│   └── InvoiceEntity.java
└── valueobjects/
    ├── SafetyStockQuantity.java
    ├── PurchaseAmount.java
    ├── InvoiceAmount.java
    └── CreditCardNumber.java
```

**良い例**

```text
src/
├── inventory/
│   ├── InventoryUseCase.java
│   ├── StockInEntity.java
│   ├── SafetyStockQuantity.java
│   └── PurchaseAmount.java
├── order/
│   ├── OrderUseCase.java
│   ├── CartEntity.java
│   └── OrderEntity.java
└── payment/
    ├── PaymentUseCase.java
    ├── InvoiceEntity.java
    ├── InvoiceAmount.java
    └── CreditCardNumber.java
```

**なぜ悪いのか**: 在庫の仕様を1つ変えるだけで、3つのフォルダを開くことになる。`PurchaseAmount`（発注金額）は `valueobjects/` に置かれ、注文に関係しそうな名前のまま注文の担当者の目に触れる。CCP に照らすと、一緒に変わるものが別のパッケージに散っている。**変更のたびに3つのパッケージをリリースし直すことになる。**

**なぜ良いのか**: 在庫の仕様変更は `inventory/` の中で閉じる。`PurchaseAmount` が在庫のものであることが、置き場所から分かる。『良いコード／悪いコードで学ぶ設計入門』が示す形である。

層で分けることが正当な場合はある。同じ記事の共通再利用の原則（CRP）は「1つのパッケージのクラスは一緒に再利用される」とする。**外部へライブラリとして出す部品は、再利用の単位で切る。** ただし業務アプリケーションの中では、同記事の順位づけにより保守性が優先する。

**業務ロジックと画面やデータベースを層で分ける話は、この章の範囲外である。** 章「03 アーキテクチャ」が扱う。

**根拠**: `SRC-CODE-002` p.226-228（10.9）、`SRC-EXT-010`

### DS-09 パッケージ間の参照が一方向か

パッケージどうしの参照に、逆向きや循環が無いかを見る。**参照は一方向にそろえる。**

『現場で役立つシステム設計の原則』は、業務アプリケーションのパッケージの参照関係が基本的に時間軸に沿った関係になるとする。例は注文の流れである。まず顧客と商品があり、注文が発生し、出荷し、請求し、入金を確認する。**顧客パッケージのオブジェクトは、注文パッケージのオブジェクトを参照してはいけない。** 逆に、注文パッケージの注文オブジェクトは、顧客と商品を知っている必要がある。

Robert C. Martin「Granularity」は、より一般の形で同じことを述べる。非循環依存の原則（ADP）であり、パッケージ間の依存構造は有向非巡回グラフでなければならないとする。有向非巡回グラフとは、矢印をたどっても出発点へ戻らない図をいう。

時間軸に沿うのは業務アプリケーションの場合である。『現場で役立つシステム設計の原則』は、その条件を「業務アプリケーションでは」と明示している。**業務の流れが無い領域では、この目安は当たらない。** 当たらない場合も、ADP の「循環させない」だけは残る。

**根拠**: `SRC-DESIGN-001` p.88-89（3章）、`SRC-EXT-010`

### DS-10 パッケージの外へ見せるものを絞っているか

パッケージの中のクラスとメソッドを、必要も無いのに `public` にしない。**外から呼ぶものだけを `public` にする。**

『現場で役立つシステム設計の原則』は、クラスとメソッドのスコープをパッケージスコープに寄せよとする。パッケージスコープとは、同じパッケージの中からだけ見える範囲をいう。理由は「`public` なクラスやメソッドが少ないほど、変更の影響範囲をパッケージに閉じ込めやすくなる」ことである。

**この観点は `DS-11` と組みになっている。** 外へ見せているものが少ないほど、パッケージ構成を後から動かせる。

**悪い例**

```java
package inventory;

public class SafetyStockQuantity {
    public int value;

    public SafetyStockQuantity(int value) {
        this.value = value;
    }

    public int calculateReorderPoint(int leadTimeDays, int dailyUsage) {
        return value + leadTimeDays * dailyUsage;
    }
}
```

**良い例**

```java
package inventory;

class SafetyStockQuantity {
    private final int value;

    SafetyStockQuantity(int value) {
        this.value = value;
    }

    int calculateReorderPoint(int leadTimeDays, int dailyUsage) {
        return value + leadTimeDays * dailyUsage;
    }
}
```

**なぜ悪いのか**: `public` にした瞬間、どのパッケージからでも参照できる。安全在庫量が在庫以外の用途で使われても、コンパイラは止めない。『良いコード／悪いコードで学ぶ設計入門』が挙げる「本来の用途以外のものと結び付いてロジックが混乱する」状態が起きる。**参照している場所を全部見つけないと、このクラスを動かせなくなる。**

**なぜ良いのか**: `inventory` パッケージの外からは見えない。クラスを別のパッケージへ移すときに、影響がパッケージの中だけで済む。**外へ出すものを増やすのは、必要になったときでよい。**

フレームワークが `public` を要求することがある。**その場合は `public` にする。この観点は、必要も無く `public` にすることを見ている。** Google Java Style Guide は可視性の既定値を定めておらず、この点の判断は言語と枠組みに委ねられている。

**根拠**: `SRC-DESIGN-001` p.85（3章）、`SRC-CODE-002` p.227（10.9）、`SRC-EXT-004` §5.2.2

### DS-11 パッケージ構成を最初に固定していないか

開発の初期に決めたフォルダ構成を、変えてはいけないものとして扱わない。**構成は動かし続けるものである。**

Robert C. Martin「Granularity」は明言する。**「パッケージ構造はトップダウンには設計できない」。** 多くのクラスを設計したあとに決まり、その後も流動し続ける。同記事は理由も書く。パッケージ依存図は機能の説明ではなく「アプリケーションをビルドする地図」であり、ビルドするものが無い着手時には要らない。

『現場で役立つシステム設計の原則』も独立に同じことを述べる。「開発初期のパッケージ構造は、少ない情報をもとに浅い理解で設計したものがほとんど」である。名前の変更、クラスのパッケージ間の移動、パッケージの移動を続けよとする。同書は参照関係についても「最初からこのような関係をすべて厳密に定義できるわけではありません」と書く。

**では最初に何を置くか。** Martin Fowler「Is Design Dead?」は、大まかな出発点としてのアーキテクチャに役割があるとする。続けて「これら初期の判断が石に刻まれることは期待されていない」と書く。**中身までは示していない。**

動かし続けるための手段が `DS-10` である。`public` を絞っておくと、後からクラスを移せる。**構成を動かす前提で作るなら、可視性を先に絞る。**

**根拠**: `SRC-EXT-010`、`SRC-DESIGN-001` p.85-89（3章）、`SRC-EXT-012`

## 名前が構造を歪めるとき

**名前の付け方の一般則は章01 が持つ（`GC-14` から `GC-17`）。** この節が扱うのは、名前がクラスの構造そのものを歪める2つの型だけである。1つは、何でも置いてよいと読ませる名前である。もう1つは、意味が広すぎて中身を絞れない名前である。

### DS-12 `Util`・`Common` に業務知識を置いていないか

共通処理クラスに置かれているものが、業務のルールや計算になっていないかを見る。**業務の知識は、業務のクラスへ移す。**

『良いコード／悪いコードで学ぶ設計入門』は、問題を名前が読み手に与える示唆に求める。**「共通利用したいロジックは `Common` クラスに置けばいいんだ」と読み手に感じさせる可能性がとても高い。** 同書が挙げる実例は、`Common` クラスに税込み金額計算・退会済み判定・注文・電話番号検証が並んだものである。

『現場で役立つシステム設計の原則』は、同じ現象を名前ではなく力学で説明する。共通ライブラリの失敗の型は2つある。

| 型 | 何が起きるか |
|---|---|
| 汎用的な共通関数 | 引数にフラグやオプションを増やして汎用化する。使う側は関係のない引数まで理解することになり、結局だれも使わない |
| 用途ごとに細分化した共通関数 | メソッド数が膨れ上がる。似たメソッドから自分に合うものを探すのが大変になり、やはり使われない |

**同書の結論は「共通ライブラリ方式では、コードの重複を防げない」である。** 共通化のために作ったものが、共通化を達成しない。

**この章は「`Util` という語を使うな」とは書かない。** JDK 自身が `java.util.Objects` を持つ。Java SE 21 API 仕様は、このクラスを「オブジェクトを操作するための `static` なユーティリティメソッドから成る」と説明する。宣言は `public final class` であり、メソッドはすべて `static` である。**状態を持たない。**

判定は2つである。

| 判定 | 置いてよいもの | 置いてはいけないもの |
|---|---|---|
| 何を置くか | 横断的関心事（ログ出力、エラー検出、例外処理、キャッシュ、同期処理） | 業務のルール、計算、判定 |
| 状態を持つか | 状態を持たないもの | インスタンスの状態に依存するもの |

1つ目の判定は『良いコード／悪いコードで学ぶ設計入門』による。**同書は横断的関心事を例外として明示し、`Logger` を `static` メソッドとして設計してよい例に挙げる。** 2つ目は `java.util.Objects` の形による。

**悪い例**

```java
public class Common {
    // 税込み金額を計算する
    public static BigDecimal calcAmountIncludingTax(
            BigDecimal amountExcludingTax, BigDecimal taxRate) {
        return amountExcludingTax.multiply(BigDecimal.ONE.add(taxRate));
    }

    // 退会済みならtrue
    public static boolean hasResigned(User user) {
        return user.getResignedAt() != null;
    }

    // 有効な電話番号ならtrue
    public static boolean isValidPhoneNumber(String phoneNumber) {
        return phoneNumber != null && phoneNumber.matches("[0-9-]{10,13}");
    }
}
```

**良い例**

```java
public record TaxRate(BigDecimal value) {
}

public record AmountExcludingTax(BigDecimal value) {
}

public class AmountIncludingTax {
    private final BigDecimal value;

    public AmountIncludingTax(AmountExcludingTax amount, TaxRate taxRate) {
        this.value = amount.value().multiply(BigDecimal.ONE.add(taxRate.value()));
    }

    public BigDecimal value() {
        return value;
    }
}
```

**なぜ悪いのか**: 税の計算、退会の判定、電話番号の検証には、何のつながりも無い。それぞれ変更を言い出す人が違う（`DS-02`）。`Common` という名前が、次のロジックを足してよいと読み手に思わせるため、無関係なものが集まり続ける。**どの業務を変えるときにこのファイルを開くのか、名前からは決まらない。**

**なぜ良いのか**: 税込み金額の計算が `AmountIncludingTax` に閉じる。税率の仕様が変わったときに開くファイルが1つに決まる。『良いコード／悪いコードで学ぶ設計入門』が示す形である。**退会の判定と電話番号の検証は、それぞれの業務のクラスへ移る。**

`java.util.Objects` のようなクラスを自分で作ってよいか。**そのクラスに何を足してよいかを1文で言えるなら、作ってよい。** 言えないなら、置き場所がまだ決まっていない。Google Engineering Practices は、レビューで「この変更は自分たちのコードベースに属するのか、ライブラリに属するのか」を問えとする。**`Util` に入れたくなったものは、置き場所の問題である。**

**根拠**: `SRC-CODE-002` p.89-91（5.4.1-5.4.3）、`SRC-DESIGN-001` p.73-74（3章）、`SRC-EXT-013`、`SRC-EXT-006`

### DS-13 `Manager`・`Processor`・`Controller` を分解しているか

「管理する」「処理する」という語を含むクラスに、関係の無いロジックが集まっていないかを見る。**代案は名前の言い換えではなく分解である。**

『良いコード／悪いコードで学ぶ設計入門』は、原因を「`Manager` という言葉の意味が広すぎてあいまい」なことに求める。**「`Manager` と名付けると何でもできそうに感じてしまう。」**

同書の例は `MemberManager` である。ヒットポイントの取得から始まり、歩行アニメーション、能力値の CSV 出力、敵の生存判定、BGM 再生まで足される。**最後の2つはメンバーにすら関係しない。**

同書は、`Manager` の仲間として `Processor` と `Controller` も挙げる。MVC の `Controller` は、受け取ったパラメータを他のクラスへ渡す責任にとどめるべきだとする。

**同書は、自分の例示コードが同じ誤りを犯していることを脚注で認めている。** 本書には `DiscountManager` や `OrderManager` が多く登場するが、あれらは良くない名前だ、と書く。

同書が示す手順は分解である。中にどんな概念が混在しているかを1つずつ分析し、ヒットポイントに責任を持つ `HitPoint` クラス、歩行アニメーションに責任を持つ `WalkAnimation` クラスとして設計せよとする。

**悪い例**

```java
public class MemberManager {
    public int getHitPoint(int memberId) { ... }

    public int getMagicPoint(int memberId) { ... }

    public void startWalkAnimation(int memberId) { ... }

    public void exportParamsToCsv() { ... }

    public boolean enemyIsAlive(int enemyId) { ... }

    public void playBgm(String bgmName) { ... }
}
```

**良い例**

```java
public record HitPoint(int value) {
    public HitPoint damaged(int amount) {
        return new HitPoint(Math.max(0, value - amount));
    }
}

public class WalkAnimation {
    private final String spriteSheetName;

    public WalkAnimation(String spriteSheetName) {
        this.spriteSheetName = spriteSheetName;
    }

    public void start() { ... }
}

public class MemberParameterCsvExporter {
    public void export(List<HitPoint> hitPoints) { ... }
}
```

**なぜ悪いのか**: 6つのメソッドの関心事がすべて違う。ヒットポイント、アニメーション、ファイル出力、敵の状態、音楽である。**メンバーの仕様が変わるたびに「とりあえず `MemberManager` に足す」判断になり、行数が増え続ける。** 同じクラスの中ではどのメンバーからもどのメンバーへもアクセスできるため、クラス全体がグローバル変数のような性質を帯びる（同書 p.242 のコラム）。

**なぜ良いのか**: 概念ごとにクラスが分かれ、変更を言い出す人と対応する（`DS-02`）。BGM と敵の生存判定は、そもそもメンバーの話ではないため、別のクラスへ移る。**`HitPoint` は値として不変にできるようになり、章01 の `GC-08` も同時に満たす。**

`Controller` は枠組みが要求する名前でもある。同書は、名前を変えろとは言っていない。**中身を「受け取ったパラメータを他のクラスへ渡す」だけに絞れとしている。** 金額計算や可否判定がそこにあるなら、分解する。

**根拠**: `SRC-CODE-002` p.259-262（11.5.3）、p.242

## 変更容易性と YAGNI

**「将来の変更に備えた抽象化」と「今必要ないものは作らない」は、原典の定義では正面からぶつかっていない。** YAGNI は「You Aren't Gonna Need It」の略であり、今は要らないものを作るなという意味である。

Martin Fowler「Yagni」は、適用範囲を明示的に限定する。**YAGNI は、見込み機能を支えるために組み込む能力に当てはまる。** 見込み機能（presumptive feature）とは、今の利用者が求めておらず、将来使うかもしれないと考えている機能をいう。**ソフトウェアを変更しやすくする努力には当てはまらない。** 同文書は「YAGNI は、コードベースの健全さをおろそかにする言い訳ではない。YAGNI は、変えやすいコードを必要とし、また可能にする」とも書く。

**ぶつかっているように見えるのは、見込み機能のための抽象化を「変更容易性のための投資」と呼び替えているときである。**

判定は2段である。

| 段 | 問い |
|---|---|
| 作ってよいか | 今は使わない複雑さを、今持ち込むことになるか |
| どこに作るか | 作ると決めたなら、最も変化する可能性が高い部分はどこか |

**根拠**: `SRC-EXT-011`、`SRC-DESIGN-002` p.121-122（3章）

### DS-14 今は使わない複雑さを、今持ち込んでいないか

その拡張点・引数・抽象の層が、今動いている機能のどれかに使われているかを見る。**使われていないなら、今は作らない。**

Martin Fowler「Yagni」は、線引きの規則を1文で書く。**「YAGNI が当てはまるのは、後になるまで使わない余分な複雑さを、今持ち込むときだけである。」** 同記事はこう続ける。将来の必要に応えて何かを足しても、複雑さが実際には増えないなら、YAGNI を持ち出す理由は無い。

同文書は判断のための思考実験も示す。**「その能力が必要になったときに、後から入れるとしたらどんなリファクタリングが要るか」を想像する。** 多くの場合、それだけで後から足しても大して高くつかないと分かる。同じ想像のもう1つの結果として、「今やるのは簡単で、複雑さをほとんど増やさず、後の費用を大きく下げるもの」が見つかることがある。同文書の例は、エラーメッセージを直書きせずルックアップ表にすることである。

『良いコード／悪いコードで学ぶ設計入門』は、害の連鎖を4つ挙げる。予測が外れてデッドコードになる、あやふやな予測が入り込んでロジックが複雑になる、可読性が下がる、変更をきっかけに実行されるとバグになる。**最後に置く理由は「先回りでつくったロジックは、現実には存在しない不確実な仕様にもとづいている」ことである。**

Google Engineering Practices も同じ向きである。開発者には、今解く必要があると分かっている問題を解かせ、将来必要になるかもしれないと推測している問題は解かせない。**将来の問題は、それが到来して実際の形と要件が見えてから解く。**

**悪い例**

```java
public interface DiscountPolicy {
    int apply(int price);
}

public class RegularDiscountPolicy implements DiscountPolicy {
    @Override
    public int apply(int price) {
        return price - 400;
    }
}

public class DiscountPolicyFactory {
    // 実装は RegularDiscountPolicy の1つだけである
    public DiscountPolicy create(String policyName) {
        if ("regular".equals(policyName)) {
            return new RegularDiscountPolicy();
        }
        throw new IllegalArgumentException("未対応の割引: " + policyName);
    }
}
```

**良い例**

```java
public class RegularDiscountedPrice {
    private static final int DISCOUNT_AMOUNT = 400;
    private static final int MIN_AMOUNT = 0;
    private final int amount;

    public RegularDiscountedPrice(int price) {
        this.amount = Math.max(MIN_AMOUNT, price - DISCOUNT_AMOUNT);
    }

    public int amount() {
        return amount;
    }
}
```

**なぜ悪いのか**: 実装が1つしか無いのに、`interface` と工場クラスと文字列の鍵が増えている。割引額を400から500へ変えるだけでも、読み手は3つのファイルをたどる。「Yagni」の言う「今は使わない余分な複雑さ」そのものである。**同文書は、使われることのない拡張点は無駄なだけでなく邪魔にもなる、という Jeremy Miller の言葉を引く。**

**なぜ良いのか**: 割引の仕様を変えるときに開くファイルが1つになる。2つ目の割引が現れたときに `interface` を切り出せばよく、そのリファクタリングは大きくない（同文書の思考実験）。

「今やるのは簡単で複雑さをほとんど増やさないもの」は作ってよい。同文書はこれを明示している。**判定は「複雑さが今増えるか」であって「将来使うか」ではない。** 定数に名前を付けること（章01 の `GC-17`）や、時刻を引数で受けること（`GC-11`）は、複雑さを増やさずに後の費用を下げる。

**根拠**: `SRC-EXT-011`、`SRC-CODE-002` p.212（10.2）、`SRC-EXT-006`

### DS-15 抽象化を、最も変化しやすい部分に絞っているか

拡張できる形（`interface`、抽象クラス、設定ファイル）を、変わりそうな部分だけに置く。**設計の全面には置かない。**

『Head Firstデザインパターン 第2版』は、開放/閉鎖原則について「設計のすべての部分を完全に制限することはできませんし、それはおそらく無駄でしょう」と述べる。開放/閉鎖原則とは、拡張には開いていて修正には閉じている設計を求める原則をいう。同書は理由も明記する。**「通常、開放/閉鎖原則に従うと新しいレベルの抽象化が導入され、コードが複雑になります。」** 抽象化には代価がある。

**同書が示す判断は「設計の中で最も変化する可能性が高い部分に注意を向け、その部分にこの原則を適用します」である。** 全面適用でも全面不適用でもない。

**同書は、その見分け方が方法論では与えられないと認めている。** 「これはいくぶん OO システム設計に対する経験の問題であり、また、みなさんが関わっている分野を理解しているかどうかの問題でもあります。」

『システム開発と「具体と抽象」』は、判定の時期を示す。良い抽象は、後から新しい種類が追加されても既存の仕組みを大きく変えずに済む。**「良い抽象は変化に強く、悪い抽象はすぐに破綻します。」判定は追加が起きたときに初めて下る。**

**`DS-14` が「作ってよいか」、`DS-15` が「どこに作るか」である。** 2つの順序を取り違えない。`DS-14` を通らなかったものに `DS-15` を適用しても、置き場所が良いだけの余分な抽象になる。

**経験が足りないときは、`DS-14` の思考実験を代わりに使う。** 『Head Firstデザインパターン 第2版』が「経験の問題」と認めていることが、Martin Fowler「Yagni」の思考実験の価値を上げる。

**根拠**: `SRC-DESIGN-002` p.121-122（3章）、`SRC-THINK-001` p.64（2章）、`SRC-EXT-011`

## デザインパターンの使いどころ

**この節は、パターンの一覧ではない。** 「どんな症状が出ているときに効くか」を先に書く。

『Head Firstデザインパターン 第2版』は、デザインパターンの定義を「パターンは、あるコンテキストにおける問題の解決策である」とする。コンテキストとは適用される状況であり、**繰り返し起こる状況である必要がある。** 問題はその状況で達成したい目的と制約であり、解決策は誰もが適用できる一般的な設計である。

同書の第1の設計原則は「アプリケーション内の変化する部分を特定し、不変な部分と分離する」である。**同書はこれを「ほとんどすべてのデザインパターンの基礎」と位置づける。**

**根拠**: `SRC-DESIGN-002` p.44（1章）、p.600（13章）

### DS-16 パターンが、どの重複を消しているかを言えるか

そのパターンを入れる理由を、観測できる症状で言えるかを見る。**言えないなら、入れない。**

Martin Fowler「Avoiding Repetition」は、判定を1つの問いに落としている。**パターンを使うと言い張るときは「これはどの繰り返しを消しているのか」と自問せよ。** 繰り返しを消しているなら、そのパターンはうまく効いている。答えられないなら、使わないほうがよい。

同文書は、パターンの過剰適用を明確に害とする。パターンを読んだばかりの人は、それを使うと言い張り、結果としてより複雑な設計になることが多い。同文書は、パターンを覚えている効用を「早く着く」ことに限定する。重複を消そうとすれば同じ構造には自力でも到達でき、パターンを知っていると早く着くだけだとする。

『Head Firstデザインパターン 第2版』は、同じ趣旨を強い言い方で置く。**「パターンを使う必要がないなら、決して使うでないぞ。」** 出発点は原則であり、必要な機能を提供する最も単純なコードを先に書けとする。

同書が挙げる導入の合図は2つである。設計上の問題を解くために必要だと確信したとき、および、将来の要件変更に応えるために必要だと確信したときである。

同書は害も明示する。パターンを使うと複雑になることがあり、必要のない複雑さを持ち込みたくはない、と書く。

同書は初心者の型を名指しする。**「初心者は『パターンを多く使うほど、よい設計になる』と考えます。」** 実際に拡張性が必要となる場合にのみ、複雑さを伴うパターンを使うべきだとする。

同書の言う「確信したとき」は、判断の主体を述べているだけで、判定の方法を与えていない。**この章は「どの繰り返しを消しているのか」の問いを判定の中心に置く。** 症状で言えないものは入れない。

**根拠**: `SRC-EXT-009`、`SRC-DESIGN-002` p.617（13章）

### 4つのパターンと、それが効く症状

**この章が扱うのは4つである。Strategy、State、Observer、Decorator である。**

選んだ基準は3つである。**この基準はどの資料にも書かれておらず、調査の議論で決めたものである。**

1. 症状を10行から25行の Java で示せる。
2. 少なくとも1冊が、パターンの側からではなく症状の側から導入している。
3. 章01 の観点（`GC-01` から `GC-17`）と重ならない。

| パターン | 効く症状 | 根拠の冊数 |
|---|---|---|
| Strategy | 同じ条件式の分岐が、複数のメソッドに書かれている | 2冊 |
| State | 状態による分岐が、複数のメソッドに散らばっている | 1冊 |
| Observer | 状態が変わったことを複数の相手へ知らせたいが、送り手が受け手を直接知っている | 1冊 |
| Decorator | 機能の組み合わせのために、サブクラスが増え続けている | 1冊 |

**Factory Method は落とした。** 『Head Firstデザインパターン 第2版』に定義はあるが、同書の例は材料の族を伴うため、症状を25行以内で示せない。**証拠が足りないためではない。**

#### Strategy が効く症状

**Strategy が効くのは、同じ条件式の `switch` や `if` が複数のメソッドに繰り返し現れているときである。** 分類を1つ足すたびに、すべての分岐に手を入れることになる。

『良いコード／悪いコードで学ぶ設計入門』は、`switch` 文の重複問題の解決手段としてストラテジパターンを導入する。**問題の側から入っており、パターンの側から入っていない。** 同書は、ストラテジの効果を「条件分岐を削減し、ロジックを単純化する」と書く。

『Head Firstデザインパターン 第2版』の定義は次のとおりである。アルゴリズムのファミリを定義し、各アルゴリズムをカプセル化し、交換できるようにする。**Strategy パターンを使うと、アルゴリズムを利用するクライアントとは独立してアルゴリズムを変更できる。**

**悪い例**

```java
public class Magic {
    public int costMagicPoint(MagicType type) {
        switch (type) {
            case FIRE: return 2;
            case SHIDEN: return 5;
            default: throw new IllegalArgumentException();
        }
    }

    public int attackPower(MagicType type) {
        switch (type) {
            case FIRE: return 20;
            case SHIDEN: return 50;
            default: throw new IllegalArgumentException();
        }
    }
}
```

**良い例**

```java
public interface Magic {
    int costMagicPoint();
    int attackPower();
}

public class Fire implements Magic {
    @Override
    public int costMagicPoint() {
        return 2;
    }

    @Override
    public int attackPower() {
        return 20;
    }
}

public class Shiden implements Magic {
    @Override
    public int costMagicPoint() {
        return 5;
    }

    @Override
    public int attackPower() {
        return 50;
    }
}
```

**なぜ悪いのか**: 魔法を1つ足すと、`switch` を2か所とも直すことになる。片方を直し忘れてもコンパイルは通り、`default` の例外が実行時に出る。**「同じ条件式が2回書かれている」が、Martin Fowler の言う消すべき繰り返しである。**

**なぜ良いのか**: 魔法を足すときに書くのは新しいクラス1つだけである。既存のファイルは開かない。消費魔法力と攻撃力が1つのクラスに並ぶため、その魔法の仕様が1か所で読める。

**根拠**: `SRC-CODE-002` p.165・p.171（8.2.7）、p.57（表3.2）、`SRC-DESIGN-002` p.59（1章）、`SRC-EXT-009`

#### State が効く症状

**State が効くのは、状態を表すフラグや列挙型を見て分岐する処理が、複数のメソッドに散らばっているときである。** 状態を1つ足すと、すべてのメソッドを見直すことになる。

『Head Firstデザインパターン 第2版』の定義は次のとおりである。State パターンでは、オブジェクトの内部状態が変化した際にオブジェクトが振る舞いを変更できる。オブジェクトはそのクラスを変更したように見える。

**同書は、State と Strategy の構造がほぼ同じで目的が違うと明言する。** Strategy は交換可能なアルゴリズムであり、State は内部状態による振る舞いの制御である。

**悪い例**

```java
public class GumballMachine {
    private State state = State.NO_QUARTER;
    private int count;

    public void insertQuarter() {
        if (state == State.NO_QUARTER) {
            state = State.HAS_QUARTER;
        } else if (state == State.SOLD_OUT) {
            throw new IllegalStateException("売り切れである");
        }
    }

    public void turnCrank() {
        if (state == State.HAS_QUARTER) {
            count -= 1;
            state = (count == 0) ? State.SOLD_OUT : State.NO_QUARTER;
        } else if (state == State.NO_QUARTER) {
            throw new IllegalStateException("硬貨が入っていない");
        }
    }
}
```

**良い例**

```java
public interface GumballState {
    GumballState insertQuarter();
    GumballState turnCrank();
}

public class NoQuarterState implements GumballState {
    @Override
    public GumballState insertQuarter() {
        return new HasQuarterState();
    }

    @Override
    public GumballState turnCrank() {
        throw new IllegalStateException("硬貨が入っていない");
    }
}

public class HasQuarterState implements GumballState {
    @Override
    public GumballState insertQuarter() {
        throw new IllegalStateException("硬貨は投入ずみである");
    }

    @Override
    public GumballState turnCrank() {
        return new NoQuarterState();
    }
}
```

**なぜ悪いのか**: 状態を1つ足すと、`insertQuarter` と `turnCrank` の両方に分岐を足す。**ある状態のときの振る舞いを知るには、すべてのメソッドを読んで分岐を拾い集めることになる。** 状態遷移の全体像がコードのどこにも現れない。

**なぜ良いのか**: 1つの状態の振る舞いが1つのクラスに集まる。「硬貨が入っていないときに何ができるか」は `NoQuarterState` を読めば分かる。状態を足すときはクラスを1つ足すだけで、既存の状態は開かない。**戻り値が次の状態であるため、遷移が型に現れる。**

**この形は `DS-05` とつながっている。** 状態ごとに変更を言い出す人が違うなら、分けたほうがよい（`DS-02`）。

**根拠**: `SRC-DESIGN-002` p.19、p.441（10章）

#### Observer が効く症状

**Observer が効くのは、値が変わったことを複数の相手へ知らせたいのに、知らせる側が相手のクラスを直接持っているときである。** 相手を1つ足すたびに、知らせる側を直すことになる。

『Head Firstデザインパターン 第2版』の定義は次のとおりである。Observer パターンは、オブジェクト間に1対多の依存関係を定義する。あるオブジェクトの状態が変わると、それに依存するすべてのオブジェクトへ通知が届き、更新される。

**悪い例**

```java
public class WeatherData {
    private final CurrentConditionsDisplay currentDisplay;
    private final StatisticsDisplay statisticsDisplay;

    public WeatherData(CurrentConditionsDisplay currentDisplay,
                       StatisticsDisplay statisticsDisplay) {
        this.currentDisplay = currentDisplay;
        this.statisticsDisplay = statisticsDisplay;
    }

    public void measurementsChanged(float temperature) {
        currentDisplay.update(temperature);
        statisticsDisplay.update(temperature);
    }
}
```

**良い例**

```java
public interface WeatherObserver {
    void update(float temperature);
}

public class WeatherData {
    private final List<WeatherObserver> observers = new ArrayList<>();

    public void register(WeatherObserver observer) {
        observers.add(observer);
    }

    public void unregister(WeatherObserver observer) {
        observers.remove(observer);
    }

    public void measurementsChanged(float temperature) {
        for (WeatherObserver observer : observers) {
            observer.update(temperature);
        }
    }
}
```

**なぜ悪いのか**: 表示を1つ足すたびに `WeatherData` のフィールドとコンストラクタと `measurementsChanged` を直す。**気象データのクラスが、表示のクラスを知っている。** 表示側の都合で気象データ側が変わるため、変更を言い出す人が2種類になる（`DS-02`）。

**なぜ良いのか**: `WeatherData` は `WeatherObserver` という約束だけを知る。表示を足すときに `WeatherData` は開かない。実行中に登録と解除ができるようになる。**知らせる側と知らされる側が、互いの実装を知らずに済む。**

相手が1つしか無いなら、この形は複雑さを足すだけである。「どの繰り返しを消しているのか」の問いに答えられない。**`DS-16` に戻る。**

**根拠**: `SRC-DESIGN-002` p.86（2章）、`SRC-EXT-009`

#### Decorator が効く症状

**Decorator が効くのは、機能の組み合わせを表すためにサブクラスを作り続けているときである。** 組み合わせが増えると、クラスの数が掛け算で増える。

『Head Firstデザインパターン 第2版』の定義は次のとおりである。Decorator パターンはオブジェクトに追加の責務を動的に付与する。**デコレータは、サブクラス化の代替となる、柔軟な機能拡張手段を備えている。**

**同書は欠点も書く。** デコレータを導入すると、コンポーネントをインスタンス化するのに必要なコードの複雑さが増す。数えきれないほど多くのデコレータでコンポーネントをラップすることになる。

**悪い例**

```java
public abstract class Beverage {
    public abstract int cost();
}

public class DarkRoast extends Beverage {
    @Override
    public int cost() {
        return 400;
    }
}

public class DarkRoastWithMocha extends DarkRoast {
    @Override
    public int cost() {
        return super.cost() + 50;
    }
}

public class DarkRoastWithMochaAndWhip extends DarkRoastWithMocha {
    @Override
    public int cost() {
        return super.cost() + 30;
    }
}
```

**良い例**

```java
public interface Beverage {
    int cost();
}

public class DarkRoast implements Beverage {
    @Override
    public int cost() {
        return 400;
    }
}

public class Mocha implements Beverage {
    private static final int PRICE = 50;
    private final Beverage base;

    public Mocha(Beverage base) {
        this.base = base;
    }

    @Override
    public int cost() {
        return base.cost() + PRICE;
    }
}

// 呼び出し側
Beverage drink = new Mocha(new DarkRoast());
```

**なぜ悪いのか**: 飲み物とトッピングの組み合わせごとにクラスが要る。トッピングが5種類あれば、組み合わせは32通りである。**トッピングの値段を変えるには、そのトッピングを含むすべてのクラスを探すことになる。** 継承でコードを共有しているため、`DS-06` にも反する。

**なぜ良いのか**: トッピング1つにつきクラスが1つで済む。組み合わせは実行時に作る。モカの値段を変えるときに開くのは `Mocha` だけである。

組み合わせが2通りしか無いなら、この形は複雑さを足すだけである。同書が挙げる欠点（インスタンス化のコードが複雑になる）が先に来る。**組み合わせの数が掛け算で増えているかを、先に確かめる。**

**根拠**: `SRC-DESIGN-002` p.126、p.139（3章）
## この章で扱わないこと

**範囲の外にあるものと、その理由を書く。**

| 扱わないもの | 理由 | 代わりに読むもの |
|---|---|---|
| フロントエンド・BFF・API の責務分担 | プロセスをまたぐ分割であり、クラスとパッケージの水準では判断できない | 章「03 アーキテクチャ」 |
| 業務ロジックと画面・データベースの層の分離 | 同上 | 章「03 アーキテクチャ」 |
| サービス分割（マイクロサービスの境界） | 同上 | 章「03 アーキテクチャ」 |
| 品質特性とアーキテクチャ上のトレードオフ | システム全体の非機能要件の話である | 章「03 アーキテクチャ」 |
| データベースのスキーマ設計 | 永続化の都合はクラスの分割とは別の力学で決まる | 章「03 アーキテクチャ」 |
| 1つのメソッドが1つのことをしているか | メソッドの中の話であり、この章はクラスとクラスの間を扱う | 章01 の `GC-04` |
| 名前から目的が読み取れるか | 名前の一般則である | 章01 の `GC-14` から `GC-17` |
| フラグ引数そのものの害 | 1つのメソッドの読みやすさの話である | 章01 の `GC-05` |
| 4つ以外のデザインパターン | 症状を短い例で示せないものを外した。一覧を作ることが目的ではない | `SRC-DESIGN-002` |
| Java の言語仕様と作法 | この手引きは特定の言語の使い方を書かない | Java の公式文書 |
| リファクタリングの手順 | 設計の判断ではなく、変更のやり方である | この手引きでは未着手 |

**Java は例示のための言語である。** この章の原則は言語に依らない。`record`、`package private`、`interface` は Java の表記である。示している考え方は「変更を言い出す人ごとに分ける」「目的が同じものだけをまとめる」「見せるものを絞る」である。

## 決着していないこと

**次の3点は、調査の段階で決着しなかった。決着したように書かない。**

### 変更容易性と YAGNI の2つの規則が同じものか

2つの規則が並んでいる。`SRC-EXT-011` は「今は使わない複雑さを今持ち込むときだけ YAGNI が当てはまる」とする。`SRC-DESIGN-002` p.122 は「最も変化する可能性が高い部分にだけ適用する」とする。**この2つが同じ1つの規則なのか、別の2つの規則なのかは決着しなかった。**

議論では、司会が「別の2つ（作ってよいか、どこに作るか）」とし、Antigravity が「本質的に同一」とした。**どちらの読み方が正しいかを判定できる資料は見つかっていない。**

**この章は、どちらの立場でも実務の手順が変わらないため、2つの問いとして書いている**（`DS-14` と `DS-15`）。決着させるには、両者を同じ場面に当てはめて結果が分かれる例を作る必要がある。

### 抽象化への投資が、いつ、どれだけ回収されるか

**測定が1つも見つからなかった。**

`SRC-EXT-014`（Martin Fowler「DesignStaminaHypothesis」）は、設計への投資が報われるまでの時間を「普通は数か月ではなく数週間」と見積もる。**ただし本人が、これは仮説であって証明ではないと明言している。** 生産性も設計品質も測れないためだとする。**この章は、この数値を書かない。**

測定として存在するのは別のものである。`SRC-EXT-015` は Kohavi ほか「Online Experimentation at Microsoft」（2009年）である。同報告 §5.1 は、Microsoft の対照実験を評価した。対象は、主要な指標を改善するために設計され、設計と実行の手続きを満たしたものである。**実際にその指標を改善したのは約3分の1だった。**

**この数値を、抽象化の話へ当てはめてはいけない。** 測っているのは Web 製品の機能案が指標を改善するかであり、設計の抽象化ではない。**この章は、この数値を観点の根拠に使っていない。**

書籍4冊にも数値は無い。`SRC-CODE-002` p.212 も `SRC-DESIGN-002` p.122 も、根拠は設計論と経験である。

### パッケージの「大まかな出発点」に何を置くか

`SRC-EXT-012` は、大まかな出発点としてのアーキテクチャに役割があると述べるが、**中身を示していない。** `SRC-DESIGN-001` p.85 も「開発初期の構造は浅い理解による」とだけ述べる。**最初にいくつパッケージを切るか、何を基準に切るかは、どの資料にも書かれていない。**

この章が書けるのは、`DS-11`（固定しない）と `DS-10`（`public` を絞って動かせるようにしておく）までである。

## この章の根拠の弱いところ

**読者が根拠の重みを判断できるように、弱い点を挙げる。**

| 弱い点 | 内容 |
|---|---|
| 議論が2者 | この章のもとになった議論は、Claude と Antigravity の2者で行った。codex は利用上限で参加できなかった |
| 2章が続けて2者 | 章01 も同じ弱点を持つ。2章が連続して2者で書かれている |
| 公開情報の突き合わせが薄い | 公開情報13件のうち、他者が独立に読んだのは `SRC-EXT-011` の1件だけである。残り12件は司会しか読んでいない |
| `DS-04` の根拠が1冊 | 「クラスの大きさは結果である」は `SRC-DESIGN-001` p.26 だけを根拠にしている |
| `DS-10` の根拠が1冊 | 「パッケージスコープに絞る」は `SRC-DESIGN-001` p.85 だけを根拠にしている |
| State・Observer・Decorator の根拠が1冊 | 3つとも `SRC-DESIGN-002` だけを根拠にしている。Strategy だけが2冊で裏づけられている |
| `DS-02` の手順が組み立て | 「メソッドごとに変更を言い出す人を書き出す」という手順の形は、どの資料にもそのままは書かれていない。`SRC-EXT-007` の例、`SRC-CODE-002` p.308 の見直し手順、`SRC-DESIGN-002` p.375 の兆候の話を、調査の議論で組み合わせたものである |
| パターンの選定基準が組み立て | 4つを選んだ3つの基準は、どの資料にも書かれていない。調査の議論で決めたものである |
| SRP の原典が未読 | `SRC-EXT-007` は提唱者本人による2014年の解説であり、原典の書籍ではない。`Agile Software Development`（2002）は手元に無い |
| 凝集度の原典が未読 | 凝集度と結合度の原典は Stevens・Myers・Constantine「Structured Design」（IBM Systems Journal 13(2)、1974）である。ACM Digital Library の該当ページが 2026-09-07 の時点で HTTP 403 を返し、本体を読めていない |

調査の記録は `research/orchestration/design/` にある。**論点と決着は `40-debate.md` に、失敗した系統は `00-plan.md` に書いてある。**

## 観点の一覧

**この章の観点を引くための索引である。** レビューの指摘やチェックリストから、観点IDで一意に指せる。

| 観点ID | 見るもの | 強さ | 出典 |
|---|---|---|---|
| `DS-01` | 責務を「変更する理由」で定義しているか | 必須 | `SRC-DESIGN-002` 9章、`SRC-EXT-007` |
| `DS-02` | 責務の数を、変更を言い出す人で数えているか | 必須 | `SRC-EXT-007` |
| `DS-03` | クラスの単位が、業務で使う言葉に対応しているか | 必須 | `SRC-DESIGN-001` 1章 |
| `DS-04` | クラスの大きさを目標にしていないか | 推奨 | `SRC-DESIGN-001` 1章 |
| `DS-05` | 共通化を「目的が同じか」で判断しているか | 必須 | `SRC-CODE-002` 7.1.3、`SRC-DESIGN-001` 4章 |
| `DS-06` | 継承でコードを共有していないか | 必須 | `SRC-CODE-002` 7.2 |
| `DS-07` | 誤った共通化を、元に戻してから分け直しているか | 推奨 | `SRC-EXT-008`、`SRC-CODE-002` 7.1.3 |
| `DS-08` | パッケージを業務領域の単位で分けているか | 必須 | `SRC-CODE-002` 10.9、`SRC-EXT-010` |
| `DS-09` | パッケージ間の参照が一方向か | 推奨 | `SRC-DESIGN-001` 3章、`SRC-EXT-010` |
| `DS-10` | パッケージの外へ見せるものを絞っているか | 推奨 | `SRC-DESIGN-001` 3章 |
| `DS-11` | パッケージ構成を最初に固定していないか | 必須 | `SRC-EXT-010`、`SRC-DESIGN-001` 3章 |
| `DS-12` | `Util`・`Common` に業務知識を置いていないか | 必須 | `SRC-CODE-002` 5.4、`SRC-DESIGN-001` 3章 |
| `DS-13` | `Manager`・`Processor`・`Controller` を分解しているか | 必須 | `SRC-CODE-002` 11.5.3 |
| `DS-14` | 今は使わない複雑さを、今持ち込んでいないか | 必須 | `SRC-EXT-011`、`SRC-CODE-002` 10.2 |
| `DS-15` | 抽象化を、最も変化しやすい部分に絞っているか | 必須 | `SRC-DESIGN-002` 3章 |
| `DS-16` | パターンが、どの重複を消しているかを言えるか | 必須 | `SRC-EXT-009`、`SRC-DESIGN-002` 13章 |

## 出典

**この章が使った出典と該当箇所を挙げる。** 出典IDの一覧は [出典カタログ](../research/sources.md) にある。

| 出典ID | 書名・資料名 | 使った箇所 | 支持する観点 |
|---|---|---|---|
| `SRC-CODE-002` | 改訂新版 良いコード／悪いコードで学ぶ設計入門 | 5.4、7.1.3、7.2、8.2.7、10.2、10.9、11.5.3、表3.2 | `DS-05`、`DS-06`、`DS-07`、`DS-08`、`DS-12`、`DS-13`、`DS-14`、`DS-16` |
| `SRC-DESIGN-001` | 現場で役立つシステム設計の原則 | 1章、3章、4章 | `DS-03`、`DS-04`、`DS-05`、`DS-09`、`DS-10`、`DS-11`、`DS-12` |
| `SRC-DESIGN-002` | Head Firstデザインパターン 第2版 | 1章、3章、9章、10章、13章 | `DS-01`、`DS-15`、`DS-16` |
| `SRC-THINK-001` | システム開発と「具体と抽象」 | 2章 | `DS-03`、`DS-15` |
| `SRC-EXT-004` | Google Java Style Guide | §5.2.2 | `DS-10` |
| `SRC-EXT-006` | Google Engineering Practices | レビューで見るもの | `DS-12`、`DS-14` |
| `SRC-EXT-007` | Robert C. Martin「The Single Responsibility Principle」 | 全体 | `DS-01`、`DS-02` |
| `SRC-EXT-008` | Sandi Metz「The Wrong Abstraction」 | 全体 | `DS-05`、`DS-07` |
| `SRC-EXT-009` | Martin Fowler「Avoiding Repetition」 | IEEE Software 2001年1-2月号 p.97-99 | `DS-05`、`DS-16` |
| `SRC-EXT-010` | Robert C. Martin「Granularity」 | The C++ Report 1996年11-12月号 | `DS-08`、`DS-09`、`DS-11` |
| `SRC-EXT-011` | Martin Fowler「Yagni」 | 全体 | `DS-05`、`DS-14` |
| `SRC-EXT-012` | Martin Fowler「Is Design Dead?」 | 全体 | `DS-11` |
| `SRC-EXT-013` | Java SE 21 API 仕様 | `java.util.Objects` のクラス説明 | `DS-12` |
| `SRC-EXT-014` | Martin Fowler「DesignStaminaHypothesis」 | 全体 | 観点を支持しない。「決着していないこと」で言及 |
| `SRC-EXT-015` | Kohavi ほか「Online Experimentation at Microsoft」（2009年） | §5.1 | 観点を支持しない。「決着していないこと」で言及 |

**1冊または1件にしか根拠が無い観点を挙げる。** `DS-04` と `DS-10` は `SRC-DESIGN-001` だけ、`DS-01` の凝集の定義は `SRC-DESIGN-002` だけ、`DS-02` は `SRC-EXT-007` だけ、`DS-07` の手順は `SRC-EXT-008` だけを根拠にしている。**複数の資料が支持する観点と、重みが違う。**

`DS-05`（共通化の判断）と `DS-08`（パッケージの分け方）は、独立した複数の資料が支持している。**この章の中では最も根拠が厚い。**

## 文書情報

| 項目 | 内容 |
|---|---|
| 作成者 | Claude（Opus 5） |
| 機密区分 | 公開可 |
| 保守責任者 | このリポジトリの保守担当 |
| 最終確認日 | 2026-09-09 |

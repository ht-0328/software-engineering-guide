---
name: writing-docs-to-standard
description: 姉妹リポジトリ engineering-docs-standard の規則に沿って docs/ の文書を書き、doc_lint とサイト生成を通し、zensical.toml の nav と CHANGELOG.md まで更新する。手引きに章を足すとき、既存の文書を直すとき、検査で落ちた文書を通るようにするとき、ADRを書くときに使う。research/ に置く調査の中間成果物には使わない。中間成果物は writing-interim-artifacts が扱う。
---

# 標準に沿った文書の執筆

## 使う場面

`docs/` に置く文書を書くとき、直すとき、検査を通すとき。

**規則の本体はサブモジュール `engineering-docs-standard/` にある。この手引きに写さない。** 同じ規則を2か所に持つと、直したそばから食い違う。ここに書くのは、手順と、検査で落ちやすい点への対処だけである。

## 手順

写して、終わったものに印を付ける。

```text
- [ ] 手順1: 型を選ぶ
- [ ] 手順2: 冒頭のメタ情報を埋める
- [ ] 手順3: 本文を書く
- [ ] 手順4: 検査を通す
- [ ] 手順5: 一覧と nav と CHANGELOG を直す
- [ ] 手順6: サイトが作れることを確かめる
```

### 手順1 型を選ぶ

| 書くもの | 使う型 |
|---|---|
| 手引きの章 | [templates/chapter.md](../../../templates/chapter.md) |
| このリポジトリ自身の決定記録 | [engineering-docs-standard/templates/adr.md](../../../engineering-docs-standard/templates/adr.md) |
| 調査の報告 | [engineering-docs-standard/templates/research-report.md](../../../engineering-docs-standard/templates/research-report.md) |
| 設計の文書 | [engineering-docs-standard/templates/design-doc.md](../../../engineering-docs-standard/templates/design-doc.md) |

型の中の説明文（`>` で始まる行）は写さない。**枠だけを使う。**

### 手順2 冒頭のメタ情報を埋める

`docs/index.md`、`docs/adr/`、`templates/`、`README.md` は、冒頭40行以内に次の5項目を持たなければ検査が落ちる。

```text
作成者 / 機密区分 / 保守責任者 / 最終確認日 / 想定読者
```

**`docs/` の章の本文は、全体で1つの文書として扱う。** 章ごとのメタ情報は要らず、`docs/index.md` が代表して持つ。

### 手順3 本文を書く

主張には出典IDと該当箇所を添える。出典が無い記述には「出典なし・私見」と書く。根拠は `research/orchestration/<題材>/40-debate.md` の決着から採る。

**決着しなかった論点を、決着したように書かない。** 「この点は決着していない」と書き、条件の違いを示す。

検査で落ちやすい点は [reference/lint-failures.md](reference/lint-failures.md) にある。**書き終えてから読むのではなく、書きながら開いておく。**

### 手順4 検査を通す

**変更した文書は、返す前に必ず検査する。**

```bash
docker run --rm --user "$(id -u):$(id -g)" -v "$PWD:/w" -w /w guide-tools \
  python tools/doc_lint.py
```

`error` が0件なら終了コード0を返す。`warning` では失敗しない。**`warning` を無視してよいとは限らない。** 一文の長さや段落の文数は、目安であって違反ではないため `warning` にしてある。読み直して、直す価値があるかを判断する。

落ちたときの直し方は [reference/lint-failures.md](reference/lint-failures.md) にある。

### 手順5 一覧と nav と CHANGELOG を直す

章を足したなら、[docs/index.md](../../../docs/index.md) の「章の一覧」の表で、その章の「状態」を書き換える。**この表は読者が進み具合を知る唯一の場所である。**

**章を足したら [zensical.toml](../../../zensical.toml) の `nav` にも足す。** 足さないと公開サイトのサイドバーに出ない。検査では見つからない。

[CHANGELOG.md](../../../CHANGELOG.md) に版と変更を書く。版の上げ方は、章を足したなら副版（`0.2.0` から `0.3.0`）、字句の修正なら修正版（`0.2.1`）とする。

### 手順6 サイトが作れることを確かめる

**`docs/` を直したら、返す前にこれも通す。** リンク切れは `doc_lint.py` と `build_site.py` の両方が見る。見る範囲が違うため、両方を通す。

```bash
docker run --rm --user "$(id -u):$(id -g)" -v "$PWD:/w" -w /w guide-tools \
  python tools/build_site.py --strict
```

Mermaidを取得していない環境では、先に1回だけ次を実行する。

```bash
bash engineering-docs-standard/tools/fetch_vendor.sh
```

## 確かめること

- [ ] 主張ごとに出典IDと該当箇所がある
- [ ] 出典の無い記述に「出典なし・私見」と書いてある
- [ ] `doc_lint.py` が `error` 0件で通る
- [ ] `build_site.py --strict` が通る
- [ ] 章を足したなら `docs/index.md` の「章の一覧」の状態が新しい
- [ ] 章を足したなら `zensical.toml` の `nav` に入っている
- [ ] `CHANGELOG.md` に版と変更がある
- [ ] `TBD` `FIXME` の印が無い

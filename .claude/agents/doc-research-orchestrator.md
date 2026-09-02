---
name: doc-research-orchestrator
description: 題材を受け取り、公開情報の調査・書籍の調査・codex・Antigravity の4系統を走らせ、3者で議論させ、決着をもとに標準に沿った文書を1本書き上げる。「〜についてのドキュメントを作って」「〜の章を書いて」「〜を調べて手引きにまとめて」と頼まれたときに使う。根拠を集める段階から書き上げまでを通しで行うため、題材が決まっていれば途中の指示は要らない。既にある文書の字句を直すだけの作業、出典を1つ確かめるだけの作業には使わない。この進め方は外部AIの実行を含み、10分以上かかるため割に合わない。
tools: Bash, Read, Write, Edit, Glob, Grep, WebSearch, WebFetch, Skill, TodoWrite
model: opus
---

# 文書づくりの指揮

## 役割

題材から文書1本までを通しで進める。**自分で書くのは司会の仕事だけである。** 各段の作法はスキルが持つ。

| 段 | 使うスキル |
|---|---|
| 中間成果物の書式 | `writing-interim-artifacts` |
| 公開情報の調査 | `researching-public-sources` |
| 書籍の調査 | `researching-book-sources` |
| 議論 | `running-multi-ai-debate` |
| 最終文書 | `writing-docs-to-standard` |

**規則を写して持たない。** 各段に入る前に、その段のスキルを読む。

## 全体の流れ

`TodoWrite` に写して進める。

```text
- [ ] 手順1: 題材を問いに変え、00-plan.md を書く
- [ ] 手順2: 外部AIを2つ、背景で走らせる
- [ ] 手順3: 待つ間に自分で公開情報と書籍を調べる
- [ ] 手順4: 外部AIの結果を回収する
- [ ] 手順5: 3者で1往復の議論をする
- [ ] 手順6: 決着をもとに最終文書を書く
- [ ] 手順7: 検査とサイト生成を通す
```

### 手順1 題材を問いに変え、00-plan.md を書く

先に [docs/index.md](../../docs/index.md) の「章の一覧」を見る。題材がそこの章に当たるなら、**新しい文書を作らず、その章として書く。** 一覧に無いなら、どこに置くかを決めて `00-plan.md` に書く。

題材を、答えられる問いに分ける。**3個から6個にする。** 少なすぎると議論が起きず、多すぎると4系統の答えがそろわない。

`research/orchestration/<題材のスラッグ>/00-plan.md` を書く。スラッグは英語の小文字とハイフンで付ける。

```markdown
# <題材> の調査計画

| 項目 | 内容 |
|---|---|
| 題材 | |
| 最終的に書く文書 | （例: `docs/04-review.md`） |
| 始めた日 | |

## 答える問い

| 問い | 内容 | 主に答える系統 |
|---|---|---|
| `Q1` | | 書籍 |
| `Q2` | | 公開情報 |

## 参加した系統

（手順4で埋める。失敗した系統もここに書く）
```

**問いは4系統すべてに同じものを渡す。** 系統ごとに問いを変えると、議論の段階で答えを並べられない。「主に答える系統」は重み付けであり、担当の分割ではない。

### 手順2 外部AIを2つ、背景で走らせる

**先に投げる。** どちらも数分から十数分かかる。待っている間に自分の調査を進める。

依頼文は2者で同一にする。`00-plan.md` の中身をプロンプトに直接入れる。

**書式の規則を依頼文に写さない。** 2者とも [AGENTS.md](../../AGENTS.md) と [.agents/skills/](../../.agents/skills/) を読む。依頼文には、どのスキルに従うかと、この作業に固有のことだけを書く。

```bash
TOPIC_DIR=research/orchestration/<スラッグ>
WORK=$(mktemp -d) && echo "作業ディレクトリ: $WORK"
{
  echo "あなたは技術文書の調査者である。次の問いに答えよ。"
  echo "書式は .agents/skills/writing-interim-artifacts/SKILL.md に従う。"
  echo "書籍から調べるときは .agents/skills/searching-book-extracts/SKILL.md に従う。"
  echo "出力は Markdown の表だけとし、前置きと後書きを書かない。"
  cat "$TOPIC_DIR/00-plan.md"
} > "$WORK/research-prompt.txt"
```

**2つを別々のBash実行として、どちらも背景で起動する**（`run_in_background` を真にする）。1つの実行にまとめて `wait` で待たない。Bashの既定の待ち時間は2分であり、外部AIの調査は3分から15分かかるため、前面で待つと打ち切られる。

**`$TOPIC_DIR` と `$WORK` は展開した実際のパスで書く。** 背景の実行はシェルの変数を引き継がない。

codex は [.codex/config.toml](../../.codex/config.toml) を読み、読み取りのみで動く。止めているコマンドは [.codex/rules/repository.rules](../../.codex/rules/repository.rules) にある。

```bash
codex exec --cd "$PWD" --skip-git-repo-check \
  -o "$TOPIC_DIR/30-codex.md" \
  "$(cat "$WORK/research-prompt.txt")
主張IDの接頭辞は C- とする。" \
  > "$WORK/codex.log" 2>&1
```

Antigravity は [tools/agy.sh](../../tools/agy.sh) 経由で起動する。**`agy` を直に呼ばない。** 素の `agy` はヘッドレスで `read_file` と `read_url` を拒否するため、何も返さない。起動スクリプトが [.agents/permissions.json](../../.agents/permissions.json) の許可リストを渡す。

```bash
bash tools/agy.sh --output-format text --print-timeout 15m \
  --print "$(cat "$WORK/research-prompt.txt")
主張IDの接頭辞は A- とする。" \
  > "$TOPIC_DIR/31-antigravity.md" 2> "$WORK/agy.log"
```

2つを起動したら、待たずに手順3へ進む。**終了は通知で受け取る。回収は手順4で行う。**

### 手順3 待つ間に自分で公開情報と書籍を調べる

`researching-public-sources` を読み、`10-web.md` を書く。続けて `researching-book-sources` を読み、`20-books.md` を書く。

**書籍の調査を省かない。** 外部AIも抽出テキストを読めるが、読むのは検索で当たった範囲だけである。どの本を選ぶかの判断は司会が持つ。

### 手順4 外部AIの結果を回収する

背景の実行が終わったかを確かめ、結果を検分する。

| 見るもの | 落ちていたときの扱い |
|---|---|
| ファイルが空でないか | 空なら失敗として記録する |
| 標準エラーに `auto-denied` が無いか | あれば、拒否された道具名を記録する |
| 表の形になっているか | 崩れていても書き換えない。そのまま残す |
| 3文以上の転載が無いか | あれば、その行を要約に置き換え、置き換えたと注記する |

**転載の確認は省かない。** `research/orchestration/` はGitで追跡するため、外部AIが書籍の本文を写していると、複製が公開範囲に出る。

`00-plan.md` の「参加した系統」に、参加できた系統と、できなかった系統の理由を書く。**失敗を隠さない。** 2系統で書いた文書は、4系統で書いたものより根拠が薄い。

### 手順5 3者で1往復の議論をする

`running-multi-ai-debate` を読み、そのとおりに進める。`40-debate.md` ができたら次へ進む。

### 手順6 決着をもとに最終文書を書く

`writing-docs-to-standard` を読み、そのとおりに進める。

**根拠は `40-debate.md` の決着から採る。** 調査の成果物から直接採らない。決着を経ていない主張は、他者の批評を受けていない。

決着しなかった論点は、決着しなかったと書く。

### 手順7 検査とサイト生成を通す

`doc_lint.py` と `build_site.py --strict` の両方を通す。`zensical.toml` の `nav` と `CHANGELOG.md` も直す。手順は `writing-docs-to-standard` にある。

## 途中で止まったときの扱い

**やり直しは、止まった手順から始める。** `research/orchestration/<スラッグ>/` に、そこまでの成果物が残っている。すでにあるファイルを作り直さない。

外部AIが2つとも失敗した場合は、**文書を書かずに報告する。** 議論が成立していないためである。判断は依頼した人に返す。

## 返すときに書くこと

- 作った文書のパス
- 参加した系統と、できなかった系統
- 決着しなかった論点の数と、その一覧
- 検査とサイト生成の結果

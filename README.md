# システム開発の進め方の手引き

| 項目 | 内容 |
|---|---|
| これは何か | コードレビュー、テスト、設計、問題の見つけ方を、出典つきで整理するリポジトリ |
| 本文 | [docs/index.md](docs/index.md) |
| 版 | 0.1.0（[変更履歴](CHANGELOG.md)） |
| 作成者 | Claude（Opus 5） |
| 機密区分 | 社内限り |
| 想定読者 | システム開発でコードを書き、レビューし、テストし、設計する人 |
| 読んだあとできること | この手引きに章を足せる。根拠のたどり方が分かる |
| 保守責任者 | このリポジトリの保守担当 |
| 最終確認日 | 2026-09-02 |

## 3行で

1. **開発の現場で繰り返し必要になる判断を、根拠つきの観点に変える。** 扱う範囲は [docs/index.md](docs/index.md) の章の一覧にある。
2. **根拠は手元の書籍22冊と、公開されている規格や標準である。** 主張には出典IDと該当箇所を添える。
3. **文書の書き方は姉妹リポジトリの標準に従う。** 規則を2か所に持たない。

## いまどこまで進んでいるか

**0.1.0 は初回セットアップである。本文はまだ無い。** できているのは、置き場所と出典の一覧、そして書くときの規則と検査の道具である。

| できているもの | 場所 |
|---|---|
| 出典カタログ（書籍22冊、出典IDつき） | [research/sources.md](research/sources.md) |
| 章の予定と書式 | [docs/index.md](docs/index.md) |
| 構成と規則の決定記録 | [docs/adr/ADR-001-repository-structure.md](docs/adr/ADR-001-repository-structure.md) |
| 文書の検査 | [tools/doc_lint.py](tools/doc_lint.py) |
| PDFからの本文抽出 | [tools/extract_pdf.py](tools/extract_pdf.py) |

## フォルダ構成

```text
docs/                     手引きの本文（Markdown が正本）
docs/adr/                 このリポジトリ自身の決定記録
research/sources.md       出典カタログ。出典IDの採番はここが一次情報
research/notes/           書籍から抽出した一次ノート（出典ID1件につき1ファイル）
research/external/        公開情報の調査結果（URLと確認日つき）
research/extracted/       PDFから取り出した本文（Git管理外）
templates/                章と観点の書式
tools/                    検査と抽出の入口。中身はサブモジュールが持つ
references/               参考書のPDF（Git管理外）
engineering-docs-standard/  文書の書き方の標準（サブモジュール）
```

## 使い方

道具はすべてDockerの中で動かす。**必要なものはDockerとGitだけである。**

### 取得する

サブモジュールに、文書の書き方の標準と、検査・抽出のスクリプトが入っている。**これが無いと道具は動かない。**

```bash
git clone --recurse-submodules <このリポジトリのURL>
```

クローンずみの場合は、次のコマンドで取得する。

```bash
git submodule update --init --recursive
```

### 作業用のイメージを作る

道具はすべてDockerの中で動かす。**ホストには何も入れない。** 最初に1回だけ実行する。

```bash
docker build -t edocs-tools -f engineering-docs-standard/tools/Dockerfile engineering-docs-standard/tools/
```

**成功したとき**: `docker images edocs-tools` が版を表示する。

### 文書を検査する

```bash
docker run --rm --user "$(id -u):$(id -g)" -v "$PWD:/w" -w /w edocs-tools python tools/doc_lint.py
```

**終了コード**: `error` が0件なら `0`、1件以上あれば `1` を返す。`warning` では失敗しない。

検査する対象は [.doclint.yml](.doclint.yml) に書いてある。**ルールの本体はサブモジュール側にあり、このファイルは差分だけを持つ。**

特定のファイルだけを検査する場合は、パスを渡す。

```bash
docker run --rm --user "$(id -u):$(id -g)" -v "$PWD:/w" -w /w edocs-tools python tools/doc_lint.py docs/index.md
```

**検査を通ったことは品質の証明ではない。** 根拠が正しいか、読者に合っているかは機械では判定できない。

### 参考書から本文を取り出す

`references/` のPDFから本文を取り出し、`research/extracted/` に置く。**出力はGit管理外である。**

```bash
docker run --rm --user "$(id -u):$(id -g)" -v "$PWD:/w" -w /w edocs-tools python tools/extract_pdf.py good-code-bad-code.pdf
```

引数を省略すると22冊すべてを処理する。**出力先のファイル名は出典IDになる。** 対応は [research/sources.md](research/sources.md) が持つ。

## 書くときの規則

1. **主張には出典IDと該当箇所を添える。** 出典が無い記述は「出典なし・私見」と明記する。
2. **1冊だけを読んで章を書かない。** 2冊以上を突き合わせ、共通点と食い違いを先に記録する。
3. **数値は目安として書く。** 出典の文脈から離れると、合否の基準に見えてしまう。
4. **書籍の本文を長く転載しない。** 要約と、ページを指す出典IDを残す。
5. **文書の書き方は [姉妹リポジトリの標準](engineering-docs-standard/docs/index.md) に従う。**

章の足し方の手順は [ADR-001](docs/adr/ADR-001-repository-structure.md) にある。

## 制約

- 参考書のPDFは購入者ウォーターマーク（メールアドレス）を含むため、Gitに入れない。
- `research/extracted/` は原本の複製にあたるため、Gitに入れない。
- 出典の無い主張は書かない。私見を書く場合は「出典なし・私見」と明記する。

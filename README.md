# システム開発の進め方の手引き

| 項目 | 内容 |
|---|---|
| これは何か | コードレビュー、テスト、設計、問題の見つけ方を、出典つきで整理するリポジトリ |
| 本文 | [docs/index.md](docs/index.md) |
| Webで読む | [公開サイト](https://ht-0328.github.io/software-engineering-guide/)（検索・目次つき） |
| 版 | 0.9.0（[変更履歴](CHANGELOG.md)） |
| 作成者 | Claude（Opus 5） |
| 機密区分 | 公開可 |
| 想定読者 | システム開発でコードを書き、レビューし、テストし、設計する人 |
| 読んだあとできること | この手引きに章を足せる。根拠のたどり方が分かる |
| 保守責任者 | このリポジトリの保守担当 |
| 最終確認日 | 2026-09-08 |

## 3行で

1. **開発の現場で繰り返し必要になる判断を、根拠つきの観点に変える。** 扱う範囲は [docs/index.md](docs/index.md) の章の一覧にある。
2. **根拠は手元の書籍22冊と、公開されている規格や標準である。** 主張には出典IDと該当箇所を添える。
3. **文書の書き方は姉妹リポジトリの標準に従う。** 規則を2か所に持たない。

## いまどこまで進んでいるか

**0.9.0 の時点で本文があるのは5章である。** 残りの3章は予定である。

| できているもの | 場所 |
|---|---|
| 本文 01 良いコードとは何か（観点17件） | [docs/01-good-code.md](docs/01-good-code.md) |
| 本文 02 設計（観点16件） | [docs/02-design.md](docs/02-design.md) |
| 本文 03 アーキテクチャ（観点18件） | [docs/03-architecture.md](docs/03-architecture.md) |
| 本文 04 コードレビュー（観点25件） | [docs/04-review.md](docs/04-review.md) |
| 本文 05 テスト（観点28件） | [docs/05-test.md](docs/05-test.md) |
| 出典カタログ（書籍22冊、出典IDつき） | [research/sources.md](research/sources.md) |
| 章の予定と書式 | [docs/index.md](docs/index.md) |
| 構成と規則の決定記録 | [docs/adr/ADR-001-repository-structure.md](docs/adr/ADR-001-repository-structure.md) |
| 文書の検査 | [tools/doc_lint.py](tools/doc_lint.py) |
| PDFからの本文抽出 | [tools/extract_pdf.py](tools/extract_pdf.py) |
| サイトの生成と公開 | [tools/build_site.py](tools/build_site.py)、[.github/workflows/pages.yml](.github/workflows/pages.yml) |
| 調査から文書までの進め方 | [指揮役のエージェント](.claude/agents/doc-research-orchestrator.md)と5つのスキル |

## フォルダ構成

```text
docs/                     手引きの本文（Markdown が正本）
docs/adr/                 このリポジトリ自身の決定記録
AGENTS.md                 codex と Antigravity 向けの指示書
.agents/                  3者が共有するスキルと、Antigravity の設定
.codex/                   codex の設定と、禁止コマンドの一覧
research/sources.md       出典カタログ。出典IDの採番はここが一次情報
research/notes/           書籍から抽出した一次ノート（出典ID1件につき1ファイル）
research/cross-reference.md  原則と出典の対応。共通点と食い違いを記録する
research/external/        公開情報の調査結果（URLと確認日つき）
research/orchestration/   調査から文書までの中間成果物。題材ごとに1ディレクトリ
research/extracted/       PDFから取り出した本文（Git管理外）
templates/                章と観点の書式
tools/                    検査と抽出の入口。中身はサブモジュールが持つ
references/               参考書のPDF（Git管理外）
engineering-docs-standard/  文書の書き方の標準（サブモジュール）
.github/workflows/        検査と公開の自動実行
zensical.toml             公開サイトの設定。章を足したら nav も直す
build/zensical/           サイト生成の下ごしらえ（生成物・Git管理外）
site/                     生成したHTML（生成物・Git管理外）
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
docker build -t guide-tools -f tools/Dockerfile tools/
```

**成功したとき**: `docker images guide-tools` が版を表示する。

### 文書を検査する

```bash
docker run --rm --user "$(id -u):$(id -g)" -v "$PWD:/w" -w /w guide-tools python tools/doc_lint.py
```

**終了コード**: `error` が0件なら `0`、1件以上あれば `1` を返す。`warning` では失敗しない。

検査する対象は [.doclint.yml](.doclint.yml) に書いてある。**ルールの本体はサブモジュール側にあり、このファイルは差分だけを持つ。**

特定のファイルだけを検査する場合は、パスを渡す。

```bash
docker run --rm --user "$(id -u):$(id -g)" -v "$PWD:/w" -w /w guide-tools python tools/doc_lint.py docs/index.md
```

**検査を通ったことは品質の証明ではない。** 根拠が正しいか、読者に合っているかは機械では判定できない。

### 参考書から本文を取り出す

`references/` のPDFから本文を取り出し、`research/extracted/` に置く。**出力はGit管理外である。**

```bash
docker run --rm --user "$(id -u):$(id -g)" -v "$PWD:/w" -w /w guide-tools python tools/extract_pdf.py good-code-bad-code.pdf
```

引数を省略すると22冊すべてを処理する。**出力先のファイル名は出典IDになる。** 対応は [research/sources.md](research/sources.md) が持つ。

### サイトを作って見る

**公開ずみのサイトを見るだけなら、この手順は要らない。** [公開サイト](https://ht-0328.github.io/software-engineering-guide/) が `master` の内容をそのまま出している。手元で作るのは、公開前の変更を確かめるときである。

図の描画に使うMermaidを先に取得する。クローン直後に一度だけ実行する。

```bash
bash engineering-docs-standard/tools/fetch_vendor.sh
```

そのうえでサイトを作る。`--strict` を付けると、リンク切れなどの警告1件で失敗する。

```bash
docker run --rm --user "$(id -u):$(id -g)" -v "$PWD:/w" -w /w guide-tools python tools/build_site.py --strict
```

**期待される出力**（末尾の3行）

```text
下ごしらえしたページ: 6
生成したページ: 6
出力先: /w/site
```

**決定記録（`docs/adr/`）は公開サイトに出ない。** このリポジトリ自身の構成を決めた記録であり、手引きの読者向けではないためである。除いているのは [tools/build_site.py](tools/build_site.py) の `UNPUBLISHED` であり、そこへ向いたリンクは GitHub の URL に差し替わる。**記録そのものはリポジトリに残る。**

開くときもDockerを使う。ブラウザで `http://127.0.0.1:8788/` を開く。止めるときは `Ctrl+C` を押す。

```bash
docker run --rm -p 8788:8788 -v "$PWD/site:/site:ro" -w /site guide-tools python -m http.server 8788 --bind 0.0.0.0
```

**生成したサイトは外部への通信を行わない。** そのために、閲覧時ではなくビルド前にMermaidを取得している。書体も読み込ませていない。

### 公開のしくみ

`master` に push すると [pages.yml](.github/workflows/pages.yml) が動く。検査とサイト生成を通ったものを GitHub Pages へ配る。プルリクエストでは [docs.yml](.github/workflows/docs.yml) が同じ検査と生成を行い、公開はしない。

**最初の公開の前に、リポジトリの設定を1つ変える。** Settings > Pages の Source を「GitHub Actions」にする。設定しないと配信の段階で失敗する。決めた理由は [ADR-002](docs/adr/ADR-002-publish-with-zensical.md) にある。

## 書くときの規則

1. **主張には出典IDと該当箇所を添える。** 出典が無い記述は「出典なし・私見」と明記する。
2. **1冊だけを読んで章を書かない。** 2冊以上を突き合わせ、共通点と食い違いを先に記録する。
3. **数値は目安として書く。** 出典の文脈から離れると、合否の基準に見えてしまう。
4. **書籍の本文を長く転載しない。** 要約と、ページを指す出典IDを残す。
5. **文書の書き方は [姉妹リポジトリの標準](engineering-docs-standard/docs/index.md) に従う。**
6. **章を足したら [zensical.toml](zensical.toml) の `nav` にも足す。** 足さないと、サイドバーに出ない。**決定記録は足さない。** 公開サイトには出さないためである。

章の足し方の手順は [ADR-001](docs/adr/ADR-001-repository-structure.md) にある。

## 制約

- 参考書のPDFは購入者ウォーターマーク（メールアドレス）を含むため、Gitに入れない。
- `research/extracted/` は原本の複製にあたるため、Gitに入れない。
- 出典の無い主張は書かない。私見を書く場合は「出典なし・私見」と明記する。

# このリポジトリで作業するときの指示

このリポジトリは、システム開発の進め方を書籍とWebの情報から整理して手引きにする。扱う範囲は [docs/index.md](docs/index.md) の章の一覧にある。

**本文は日本語で書き、ファイル名は英語の小文字とハイフンで付ける。**

先に次の3つを読む。

1. [README.md](README.md)
2. [docs/index.md](docs/index.md)
3. [ADR-001 リポジトリの構成](docs/adr/ADR-001-repository-structure.md)

## 守ること

1. **主張には出典IDと該当箇所を添える。** 出典が無い記述は「出典なし・私見」と明記する。出典IDの一覧は [research/sources.md](research/sources.md) にある。
2. **1冊だけを読んで章を書かない。** 2冊以上のノートを突き合わせ、共通点と食い違いを `research/cross-reference.md` に記録してから書く。
3. **書籍の本文を長く転載しない。** 要約と、章・節を指す出典IDを残す。
4. **参考書のPDFと `research/extracted/` をGitに入れない。** PDFは購入者ウォーターマーク（メールアドレス）を含む。
5. **文書の書き方は [サブモジュールの標準](engineering-docs-standard/docs/index.md) に従う。** 規則をこのリポジトリに写さない。
6. **未解決の印（「TBD」「FIXME」）を残さない。** 決まっていないことは、決まっていないと書く。
7. **章を足したら [zensical.toml](zensical.toml) の `nav` にも足す。** 足さないと公開サイトのサイドバーに出ない。

## 章を足す手順

1. `tools/extract_pdf.py` で本文を `research/extracted/` に取り出す。
2. `research/notes/<出典ID>.md` にノートを書く。**冒頭に、どこまで読んだかを書く。** 書式は [templates/research-note.md](templates/research-note.md) にある。
3. `research/cross-reference.md` に、原則と出典の対応を書く。
4. `docs/` に章を書く。書式は [templates/chapter.md](templates/chapter.md) にある。
5. 検査を通し、[docs/index.md](docs/index.md) の章の一覧の状態を更新する。
6. [zensical.toml](zensical.toml) の `nav` に章を足し、サイトが作れることを確かめる。
7. [CHANGELOG.md](CHANGELOG.md) に版と変更を書く。

## 道具の動かし方

道具はすべてDockerの中で動かす。**ホストには何も入れない。** イメージは最初に1回だけ作る。

```bash
docker build -t guide-tools -f tools/Dockerfile tools/
```

文書を検査する。**変更した文書は、返す前に必ず検査する。**

```bash
docker run --rm --user "$(id -u):$(id -g)" -v "$PWD:/w" -w /w guide-tools python tools/doc_lint.py
```

参考書から本文を取り出す。引数はPDFのファイル名である。

```bash
docker run --rm --user "$(id -u):$(id -g)" -v "$PWD:/w" -w /w guide-tools python tools/extract_pdf.py good-code-bad-code.pdf
```

公開サイトを作る。**`docs/` を直したら、返す前にこれも通す。** 先に `bash engineering-docs-standard/tools/fetch_vendor.sh` を1回だけ実行する。

```bash
docker run --rm --user "$(id -u):$(id -g)" -v "$PWD:/w" -w /w guide-tools python tools/build_site.py --strict
```

## 書き方の要点

**規則の本体はサブモジュールにある。** ここには、検査で落ちやすい点だけを挙げる。

| 点 | 内容 |
|---|---|
| 文体 | 常体（である）でそろえる |
| 曖昧な語 | 「適宜」「可能な限り」などを使わず、数値と固有名詞で書く |
| 時点に依存する語 | 「今後」「最新の」などを使わず、日付と版数で書く |
| 見出し | h1は1つ。階層は4段まで |
| 見出しの直後 | 本文を置く。見出しを続けない |
| 表 | 1セルは2文まで。長くなるなら別の形式にする |
| リンク | 「こちら」ではなく、行き先が分かる文字列にする |

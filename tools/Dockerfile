# このリポジトリの作業用イメージ。ホストには何もインストールしない。
#
#   docker build -t guide-tools -f tools/Dockerfile tools/
#
# 用途は3つある。文書の検査、参考書PDFからの本文抽出、公開サイトの生成である。
#
# 道具の中身はサブモジュール engineering-docs-standard が持つ（ADR-001）。
# ここが持つのは、その道具が動く環境だけである。サブモジュールは用途ごとに
# イメージを2つに分けているが、このリポジトリは1つにまとめる。理由は ADR-002 にある。
FROM python:3.14-slim-trixie

# poppler-utils は pdftotext を提供する。日本語PDFのレイアウト保持抽出に使う。
# poppler-data は Adobe-Japan1 などのCJK用CIDマッピングを提供する。これが無いと
# 日本語PDFの本文がCID番号のまま出力され、文字化けする。
RUN apt-get update \
 && apt-get install -y --no-install-recommends poppler-utils poppler-data \
 && rm -rf /var/lib/apt/lists/*

# 版を固定する。上げるときは、この行と README の記述を同時に書き換える。
# zensical は 0.0.57 時点で Alpha である（PyPI の分類が Development Status :: 3）。
RUN pip install --no-cache-dir \
      pypdf==6.1.1 \
      PyYAML==6.0.2 \
      zensical==0.0.57

WORKDIR /w

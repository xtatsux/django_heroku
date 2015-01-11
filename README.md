# About

HerokuにデプロイするためのDjangoのサンプルコードです。
以下の記事より参照しています。

[DjangoをHerokuにデプロイ - Qiita](http://qiita.com/xtatsux/items/0eb69fca7fa39df61cf3)

# Setup

開発環境構築

* 前提
   * [direnv](https://github.com/zimbatm/direnv)を利用
   * python 3環境

    $ cp .envrc.template .envrc
    $ vim .envrc  # Edit for your development environment.
    $ direnv allow .
    $ pip install -r requirements.txt

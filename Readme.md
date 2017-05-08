# 使い方

## 準備

* Dockerのインストール
    * こちらからダウンロードしてインストール https://www.docker.com/community-edition
* Dockerfileやサンプルコードのダウンロード
```bash
git clone https://github.com/yasutomo57jp/alcon2017prmu
```

## Dockerのインストール



## コンテナの作成

Dockerfileのあるディレクトリで以下のコマンドを実行

```bash
sudo docker build -t alcon .
```

少し時間がかかりますが，環境が構築されます．

## 実行 (Python)

* アルコンのサンプルコードとデータセットを置いたディレクトリで，以下のコマンドを実行するとコンテナが起動します

```bash
sudo docker run --rm -it -v `pwd`:/alcon /bin/bash
```

* /alcon にマウントされているので，以下のようにして実行します

```bash
cd /alcon/python
python main.py 1 ../dataset
```

## 実行 (C++)

* アルコンのサンプルコードとデータセットを置いたディレクトリで，以下のコマンドを実行するとコンテナが起動します

```bash
sudo docker run --rm -it -v `pwd`:/alcon /bin/bash
```

* /alcon にマウントされているので，以下のようにして実行します

```bash
cd /alcon/cpp
make
./main 1 ../dataset
```



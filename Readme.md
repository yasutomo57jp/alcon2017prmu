# 使い方

## 準備

* Dockerのインストール
    * こちらからダウンロードしてインストール https://www.docker.com/community-edition
    * GPUを使う場合は nvidia-docker をインストール https://github.com/NVIDIA/nvidia-docker
* Dockerfileやサンプルコードのダウンロード
```bash
git clone https://github.com/yasutomo57jp/alcon2017prmu
```

## コンテナの作成（GPUなし版）

Dockerfileのあるディレクトリで以下のコマンドを実行

```bash
sudo docker build -t alcon -f Dockerfile .
```

少し時間がかかりますが，環境が構築されます．

## コンテナの作成（GPUあり版）

GPUが刺さった計算機の場合，こちらを実行すると，GPUを利用した計算が可能になります．

Dockerfileのあるディレクトリで以下のコマンドを実行

```bash
sudo docker build -t alcon_gpu -f Dockerfile_gpu .
```

少し時間がかかりますが，環境が構築されます．

## 実行 (Python)

* アルコンのサンプルコードとデータセットを置いたディレクトリで，以下のコマンドを実行するとコンテナが起動します

```bash
sudo docker run --rm -it -v `pwd`:/alcon alcon /bin/bash
```

* GPUを使う場合，以下のコマンドを実行してコンテナを起動させます

```bash
sudo nvidia-docker run --rm -it -v `pwd`:/alcon alcon_gpu /bin/bash
```

* /alcon にマウントされているので，以下のようにして実行します

```bash
cd /alcon/python
python main.py 1 ../dataset
```

## 実行 (C++)

* アルコンのサンプルコードとデータセットを置いたディレクトリで，以下のコマンドを実行するとコンテナが起動します

```bash
sudo docker run --rm -it -v `pwd`:/alcon alcon /bin/bash
```

* GPUを使う場合，以下のコマンドを実行してコンテナを起動させます

```bash
sudo nvidia-docker run --rm -it -v `pwd`:/alcon alcon_gpu /bin/bash
```

* /alcon にマウントされているので，以下のようにして実行します

```bash
cd /alcon/cpp
make
./main 1 ../dataset
```



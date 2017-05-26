このページに間違い等があれば，ぜひプルリクエストを送ってください！
また，Dockerfileもこうしたら良いとかこのライブラリを足してほしいとかあればぜひプルリクエストしてください．

# 使い方

## 準備

* Dockerのインストール
    * こちらからダウンロードしてインストール https://www.docker.com/community-edition
    * GPUを使う場合は nvidia-docker をインストール https://github.com/NVIDIA/nvidia-docker
* Dockerfileやサンプルコードのダウンロード
```bash
git clone https://github.com/yasutomo57jp/alcon2017prmu
```
* Datasetの準備
    * 以下のページからデータセットをダウンロード
         https://github.com/tomomiyazaki/alcon2017prmu_dataset


## 実行 (Python)

* アルコンのサンプルコードとデータセットを置いたディレクトリで，以下のコマンドを実行するとコンテナが起動します

```bash
sudo docker run --rm -it -v `pwd`:/alcon yasutomo57jp/alcon:cpu /bin/bash
```

* GPUを使う場合，以下のコマンドを実行してコンテナを起動させます

```bash
sudo nvidia-docker run --rm -it -v `pwd`:/alcon yasutomo57jp/alcon:gpu /bin/bash
```

* /alcon にマウントされているので，以下のようにして実行します
   * まず学習を行います．
```bash
cd /alcon/python
python train.py ../dataset 1
```
   * その後，実行します．
```bash
cd /alcon/python
python main.py ../dataset 1
```

## 実行 (C++)

* アルコンのサンプルコードとデータセットを置いたディレクトリで，以下のコマンドを実行するとコンテナが起動します

```bash
sudo docker run --rm -it -v `pwd`:/alcon yasutomo57jp/alcon:cpu /bin/bash
```

* GPUを使う場合，以下のコマンドを実行してコンテナを起動させます

```bash
sudo nvidia-docker run --rm -it -v `pwd`:/alcon yasutomo57jp/alcon:gpu /bin/bash
```

* /alcon にマウントされているので，以下のようにして実行します

```bash
cd /alcon/cpp
make
./main ../dataset 1
```

## コンテナの作成（GPUなし版：応用編）

ダウンロードせずにDockerfileから自前でコンテナを作りたい人向けです

Dockerfileのあるディレクトリで以下のコマンドを実行

```bash
sudo docker build -t alcon:cpu -f Dockerfile .
```

少し時間がかかりますが，環境が構築されます．
なお，この方法で作成した場合，以下のように実行します．
```bash
sudo docker run --rm -it -v `pwd`:/alcon alcon:cpu /bin/bash
```


## コンテナの作成（GPUあり版：応用編）

ダウンロードせずにDockerfileから自前でコンテナを作りたい人向けです

GPUが刺さった計算機の場合，こちらを実行すると，GPUを利用した計算が可能になります．

Dockerfileのあるディレクトリで以下のコマンドを実行

```bash
sudo docker build -t alcon:gpu -f Dockerfile_gpu .
```

少し時間がかかりますが，環境が構築されます．
なお，この方法で作成した場合，以下のように実行します．
```bash
sudo nvidia-docker run --rm -it -v `pwd`:/alcon alcon:gpu /bin/bash
```


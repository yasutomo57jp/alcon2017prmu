# -*- coding: utf-8 -*-
"""
このMyAlgorithmを編集し，
自前のアルゴリズムを実装してください．

ただし，関数の入出力は変更しないでください．

1つのテストデータに対する処理は，
predict関数を編集してください．
他のメンバ関数の追加は自由です．

学習済みデータの読み込み等は自由に行って構いませんが，
読み込むファイルはuser_function.pyと同じディレクトリ
もしくはサブディレクトリに置いてください．
"""

import os.path
import cv2
from sklearn.externals import joblib


class MyAlgorithm(object):
    """
    アルゴリズム
    """
    def __init__(self, datasetdir):
        self.datasetdir = datasetdir

        # もし学習済み識別器等を読み込む必要があればここで
        #trained_file = os.path.join(datasetdir, "model.pkl")
        trained_file = "./model.pkl"
        self.classes, self.classifier = joblib.load(trained_file)

        
    def predict(self, full_img, bbox):
        """
        認識処理を記述する関数
        :param numpy.ndarray full_img: 1ページ全体の画像
        :param tuple[int] bbox: 対象となる領域のbounding box (x, y, w, h)
        :rtype list[str]
        :return ユニコードを表す文字列の配列 <-- レベル1は1つのunicode、レベル2は3つのunicode、レベル3は3つ以上のunicodeです
        """
        # 対象領域を切り出す
        x, y, w, h = bbox
        target_img = full_img[y:y+h, x:x+w, :]

        # 画像から特徴抽出
        feature = self.feature_extraction(target_img)

        # 識別器にかける
        recog_result = self.classifier.predict([feature])

        codes = []
        for res in recog_result:
            codes.append(self.classes[res])

        return codes


    @classmethod
    def feature_extraction(cls, img):
        """
        特徴抽出のサンプル（画像を引き伸ばしてベクトル化しているだけ）
        """
        img_ = cv2.resize(img, (32, 32))
        return img_.reshape(-1)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
第21回PRMUアルゴリズムコンテスト評価用コード
以下の様に実行してください
（path/to/datasetdir は，データセットの場所）

    python main.py path/to/datasetdir 1

"""

import sys
import os.path
import cv2
from user_function import MyAlgorithm
from alcon_utils import AlconUtils


def main(datasetdir, lv):
    """
    評価コードのメイン
    :param datasetdir データセットを格納したディレクトリへのパス
    """

    # 初期化
    alcon = AlconUtils(datasetdir)
    myalgorithm = MyAlgorithm(datasetdir)

    # ターゲットの読み込み
    fn = "target_lv" + lv + "_test_5.csv"
    alcon.load_annotations_target(fn)

    
    results = {}
    prev = None
    # １ターゲットずつ認識していくループ
    for bb_id, target in alcon.targets.items():
        img_file_id, *bb = target
        img_filename = os.path.join(datasetdir, "images", img_file_id+".jpg")
        
        if prev != img_filename:
            # ページ全体の画像
            full_img = cv2.imread(img_filename)
            prev = img_filename

        # 認識処理（ここで各自のアルゴリズムを呼び出します）
        result = myalgorithm.predict(full_img, bb)

        # boundingbox id と紐付けて保存
        results[bb_id] = result

        
    # 評価
    fnGround = "groundtruth_lv" + lv + "_test_5.csv"
    alcon.load_annotations_ground(fnGround)
    alcon.evaluation( results )

    # ファイルに結果を書き込む
    alcon.write_results( results )
    
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python main.py datasetdir lv", file=sys.stderr)
        quit()

    main( sys.argv[1], sys.argv[2] )


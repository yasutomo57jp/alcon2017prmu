#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import os.path
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib
from user_function import MyAlgorithm
from alcon_utils import AlconUtils
import numpy as np
import cv2


def main(datasetdir,lv):

    # 初期化
    alcon = AlconUtils(datasetdir)

    # アノテーションの読み込み
    fn = "target_lv" + lv + "_samp_5.csv"
    alcon.load_annotations_target(fn)

    fn = "groundtruth_lv" + lv + "_samp_5.csv"
    alcon.load_annotations_ground(fn)

    
    # KNNモデルの作成
    dataset = {}
    for bb_id, target in alcon.targets.items():
        img_filename = alcon.get_filename_char( bb_id )
        code = alcon.ground_truth[bb_id][0]
        if code not in dataset:
            dataset[code] = []
        if len(dataset[code]) == 5:
            continue
        img = cv2.imread( img_filename )
        feature = MyAlgorithm.feature_extraction(img)
        dataset[code].append(feature)

    labels = []
    data = []
    classes = sorted(dataset.keys())
    for label, values in dataset.items():
        labels += [classes.index(label)] * len(values)
        data += values

    data = np.asarray(data, dtype=np.float)
    labels = np.asarray(labels, dtype=np.int)

    classifier = KNeighborsClassifier()
    classifier.fit(data, labels)

    outputfile = "./model.pkl"
    joblib.dump((classes, classifier), outputfile)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python train.py datasetdir lv", file=sys.stderr)
        quit()

    main(sys.argv[1], sys.argv[2])

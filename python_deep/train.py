#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import os.path
from sklearn.externals import joblib
from user_function import MyAlgorithm
from alcon_utils import AlconUtils
import numpy as np
import cv2
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
import keras


def main(datasetdir,lv):
    input_shape = (64, 64, 3)

    # 初期化
    alcon = AlconUtils(datasetdir)

    # アノテーションの読み込み
    fn = "target_lv" + lv + "_samp_0.9.csv"
    alcon.load_annotations_target(fn)

    fn = "groundtruth_lv" + lv + "_samp_0.9.csv"
    alcon.load_annotations_ground(fn)

    # CNNモデルの作成
    dataset = {}
    for bb_id, target in alcon.targets.items():
        img_filename = alcon.get_filename_char( bb_id )
        code = alcon.ground_truth[bb_id][0]
        if code not in dataset:
            dataset[code] = []
        img = cv2.imread( img_filename )
        img = cv2.resize(img, (input_shape[0], input_shape[1]))
        img = np.asarray(img, dtype=np.float) / np.max(img)
        dataset[code].append(img)

    labels = []
    data = []
    classes = sorted(dataset.keys())
    for label, values in dataset.items():
        labels += [classes.index(label)] * len(values)
        data += values

    data = np.asarray(data, dtype=np.float)
    labels = np.asarray(labels, dtype=np.int)
    labels_c = keras.utils.to_categorical(labels)
    print(len(data), len(labels))
    quit()

    # ネットワークの学習
    model = Sequential()
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu', input_shape=input_shape))
    model.add(MaxPooling2D(pool_size=(3, 3)))
    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(3, 3)))
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(len(classes), activation='softmax'))

    model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer=keras.optimizers.Adam(),
                  metrics=['accuracy'])

    model.fit(data, labels_c, batch_size=100, epochs=100, verbose=1)

    outputfile = os.path.join(datasetdir, "model.h5")
    classfile = os.path.join(datasetdir, "classes.pkl")
    model.save(outputfile)
    joblib.dump(classes, classfile)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python train.py datasetdir lv", file=sys.stderr)
        quit()

    main(sys.argv[1], sys.argv[2])

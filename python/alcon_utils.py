# -*- coding: utf-8 -*-
import os.path
import sys

class AlconUtils(object):
    """
    便利なフレンド（関数）たち
    """
    
    def __init__(self, datasetdir ):
        self.datasetdir = datasetdir
        self.targets = {}
        self.ground_truth = {}

               
    def evaluation(self, results):
        """
        評価を行う関数
        :param results 認識結果の配列
        """

        all_count = 0
        count = 0
        for bb_id, grounds in self.ground_truth.items():
            nG = len(grounds)
            nR = len(results[bb_id])
            all_count += nG

            if nR >= nG:
                n = nG
            else:
                n = nR

            for i in range(n):
                if grounds[i] == results[bb_id][i]:
                    count += 1
            
        print("results: %d / %d" % (count, all_count))
        print("score: %f" % (1.0 * count / all_count))
        return count, all_count


    def load_annotations_target(self, fn ):
        """
        ターゲットのアノテーションファイルを読み込みます
        Usage: load_annotations_target( "target-lv1.csv" )
        """
        target_file = os.path.join(self.datasetdir, "annotations", fn)
        with open(target_file, "r") as fin:
            next(fin) # 一行目をとばす #tomo
            for line in fin:
                bb_id, img_file_id, x, y, w, h, = line.strip().split(",")
                x, y, w, h = map(int, (x, y, w, h))
                self.targets[bb_id] = (img_file_id, x, y, w, h)

                
    def load_annotations_ground(self, fn ):
        """
        Groundtruthのアノテーションファイルを読み込みます
        Usage: load_annotations_ground( "groundtruth-lv1.csv" )
        """
        gt_file = os.path.join(self.datasetdir, "annotations", fn)
        with open(gt_file, "r") as fin:
            next(fin) # 一行目をとばす #tomo
            for line in fin:
                bb_id, *unicodes = line.strip().split(",") 
                self.ground_truth[bb_id] = unicodes

                
    # bb_idの文字画像ファイル名を取得する。パス付き。
    def get_filename_char(self, bb_id):
        target = self.targets[bb_id]
        ground = self.ground_truth[bb_id]
        fn =  ground[0] + "_" + target[0] + \
              "_X" + '{0:04d}'.format(target[1]) + \
              "_Y" + '{0:04d}'.format(target[2]) + ".jpg"
        fn = os.path.join(self.datasetdir, "characters", ground[0], fn)
        return fn

    
    # 認識結果をファイルに書き込む
    def write_results(self, results):
        fn = "./myResults.csv"
        f = open(fn,"w")
        f.write("ID,Unicode\n")
        for bb_id, codes in results.items():
            str1 = bb_id + "," + ",".join(codes) + "\n"
            f.write( str1 )
        f.close()
    
        

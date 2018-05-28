# -*- coding: utf-8 -*-
"""
Created on Sun May 27 03:07:56 2018
"""

import cv2
import numpy as np
import os
import re
import matplotlib.pyplot as plt
import glob
import codecs
% matplotlib inline

# 分類されたデータセットになる画像フォルダへのディレクトリを指定
dir = 'C:/Users/Desktop/data_picture/coin'
files = os.listdir(dir)# ファイルのリストを取得
count = 0
for file in files:# ファイルの数だけループ
    # ここではjpg,JPG,pngの物だけ考える
    index_jpg = re.search('.jpg', file)
    index_png = re.search('.png', file)
    index_JPG = re.search('.JPG', file)
    if index_jpg:
        count += 1
    if index_png:
        count += 1
    if index_JPG:
        count += 1

# cv2.imreadのpath指定だとなぜかエラーになるので関数を作る
def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None
# 元になるxmlのpathを指定する
sample = minidom.parse("C:/Users/Desktop/data_picture/coin/coin_annotation/coin (1).xml")
# 出来たxmlを保存するフォルダを作るのでpathを指定
edited_dir = 'C:/Users/Desktop/data_picture/coin/test/'
os.makedirs(edited_dir, exist_ok=True)

for i in range(1,count+1):
    xdoc = sample # 一応分けておく
    folder = dir.split('/')[-1]# annotationのオブジェクト名にしたい物が入っているフォルダ名
    img_path = dir+'/'+files[i-1]# imageのpathを指定
    print(img_path)
    img = imread(imgs[i-1])# imageの読み込み
    img_size = img.shape# imageの大きさを得る
    width = img_size[1]
    height = img_size[0]
    depth = img_size[2]
    
    #元になるxmlのfolder,filename,path,width,height,xmin,ymin,xmax,ymax,nameを変更する
    element = xdoc.getElementsByTagName("folder")[0]
    element.childNodes[0].data = folder
    element = xdoc.getElementsByTagName("filename")[0]
    element.childNodes[0].data = files[i-1]
    element = xdoc.getElementsByTagName("path")[0]
    element.childNodes[0].data = img_path
    element = xdoc.getElementsByTagName("width")[0]
    element.childNodes[0].data = width
    element = xdoc.getElementsByTagName("height")[0]
    element.childNodes[0].data = height
    element = xdoc.getElementsByTagName("depth")[0]
    element.childNodes[0].data = depth
    element = xdoc.getElementsByTagName("xmin")[0]
    element.childNodes[0].data = 0
    element = xdoc.getElementsByTagName("ymin")[0]
    element.childNodes[0].data = 0
    element = xdoc.getElementsByTagName("xmax")[0]
    element.childNodes[0].data = width
    element = xdoc.getElementsByTagName("ymax")[0]
    element.childNodes[0].data = height
    element = xdoc.getElementsByTagName("name")[0]
    element.childNodes[0].data = folder
    
    # xmlを保存する
    f = codecs.open('edited_dir' + 'annotation_{0}.xml'.format(files[i-1][:-4]), 'w', 'utf-8')
    xdoc.writexml(writer=f, encoding='UTF-8', newl='\n', addindent='\t')
    f.close()

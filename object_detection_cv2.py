# -*- coding: utf-8 -*-
"""
Created on Sat May 26 23:10:34 2018

"""

import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt

def object_detection(path):
    
    def threshold(path):
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #pixelをNxNで結合し、その平均値を表す 要するにぼかす
        img_gaussian = cv2.GaussianBlur(img, (15, 15), 0)
        #グレースケールにする
        img_gray = cv2.cvtColor(img_gaussian, cv2.COLOR_RGB2GRAY)
        min_n = 150
        max_n = 255
        # 閾値処理
        _, img_threshold = cv2.threshold(img_gray, min_n, max_n, cv2.THRESH_BINARY)#数値を変える
        img_g = cv2.cvtColor(img_threshold, cv2.COLOR_GRAY2RGB)
        plt.imshow(img_g)
        
        return img_threshold
    
    # 画像の読み込み
    img = cv2.imread(path)
    # 閾値処理
    img_threshold = threshold(path)
    img_bitwise = cv2.bitwise_not(img_threshold)
    # 輪郭検出
    im2, contours, hierarchy = cv2.findContours(img_bitwise, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    detected_list = []
    img_size = img.shape
    for i in contours:
        # 検出した物体が小さければ次に検出した物体へ移る
        if cv2.contourArea(i) < int(img_size[0]*0.1 + 0.1*img_size[1]):
            continue
        
        # 輪郭がギリギリなので周囲に余白がほしい
        x, y, w, h = cv2.boundingRect(i)
        if(x<20 and y>=20):
            x, y, w, h = x, y-20, w, h
        elif(y<20 and x>=20):
            x, y, w, h = x-20, y, w, h
        else:
            x-20, y-20, w, h
            
        # 検出できたもの
        img_detected = img[y:(y + h), x:(x + w)]
        img_detected = cv2.cvtColor(img_detected, cv2.COLOR_RGB2BGR)
        # 一行目がNoneだったら飛ばす
        if img_detected is None:
            continue
        detected_list.append(img_detected)

    return detected_list



file_path = 'coin.jpg'# pathを入力
sample = object_detection(file_path)
print(len(sample))
#for i in range(8):
#    plt.subplot(3,3,i+1), plt.imshow(sample[i])
img = cv2.imread(file_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.subplot(5,5,25), plt.imshow(img)
for i in range(len(sample)):
    plt.subplot(5,5,i+1), plt.imshow(sample[i])

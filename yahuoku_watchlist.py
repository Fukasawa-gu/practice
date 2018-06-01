# -*- coding: utf-8 -*-
"""
Created on Mon May 28 21:10:47 2018
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import WebDriverException

import re
import time


try:
    chro = webdriver.Chrome()
except:
    chro = webdriver.Chrome('C:/selenium/chromedriver')# 自分のchromedriverのpathを通しておく

account_id = "taro"

#ログイン
print("{}でログイン".format(account_id))
name = account_id
chro.get('https://auctions.yahoo.co.jp/')

chro.find_element_by_link_text('ログイン').click()
time.sleep(1)

input = chro.find_element_by_id('username')
time.sleep(1)

input.send_keys("{}".format(account_id))
time.sleep(1)

btn = chro.find_element_by_name('btnNext')
time.sleep(1)

btn.click()
time.sleep(1)

input = chro.find_element_by_id('passwd')
time.sleep(1)

input.send_keys('watashihataro')
time.sleep(1)

btnpass =chro.find_element_by_name('btnSubmit')
time.sleep(1)

btnpass.click()
time.sleep(1)

# ログインしているアカウント以外のリストを作る
other_seller = ['jiro', 'saburo']
other_seller.remove('taro')
print(other_seller)

# アカウントを一つずつ見ていく
for seller in other_seller:
    cnt = 1
    print("{}の商品を見ていきます".format(seller))
    # sellerの商品一覧の1ページ目に移る
    print('https://auctions.yahoo.co.jp/seller/'+seller+'&b='+str(cnt))
    running = True
    chro.get('https://auctions.yahoo.co.jp/seller/'+seller+'&b='+str(cnt))

    # ウォッチリスト登録が終わったid数をカウントする
    lots_count = 0
    while(running):
        
        # 商品IDを得る
        ids = chro.find_elements_by_xpath('//*[@id]')
        time.sleep(1)
        lots_id = []
        for i in ids:
            id_before = i.get_attribute('id')
            if ":" in id_before:
                id_before = id_before.split(':')
                lots_id.append(id_before[0])
        # すでにウォッチリスト登録が終わったものをリストから除く
        lots_id = lots_id[lots_count:]
        try :
            print('このページは残り{}個'.format(len(lots_id)))
            # 商品ページに飛ぶ
            url_id = 'https://page.auctions.yahoo.co.jp/jp/auction/' + str(lots_id[0])
            print(url_id)
            chro.get(url_id)
            time.sleep(1)

            try:
                # 広告が開かれたら閉じる
                ad_close = chro.find_element_by_link_text("閉じる")
                print('ad 発見')
                time.sleep(1)
                ad_close.click()
                time.sleep(1)
                print('ad 閉じた')
                # ウォッチリスト登録
                watch = chro.find_element_by_xpath('//*[@id="l-sub"]/div[1]/ul/li[1]/div/ul/li[3]/a')
                time.sleep(1)
                watch.click()
                time.sleep(1)
                print("{} をウォッチリストに登録しました".format(lots_id[0]))
                # 商品一覧に戻る
                chro.back()
                time.sleep(1)
                chro.back()
                time.sleep(1)


            except:
                # ウォッチリスト登録
                watch = chro.find_element_by_xpath('//*[@id="l-sub"]/div[1]/ul/li[1]/div/ul/li[3]/a')
                time.sleep(1)
                watch.click()
                time.sleep(1)
                print("{} をウォッチリストに登録しました".format(lots_id[0]))
                # 商品一覧に戻る
                chro.back()
                time.sleep(1)
                chro.back()
                time.sleep(1)
            # ウォッチリスト登録が一つ終わったのでlots_countに1を加える
            lots_count += 1

        except Exception as e:

            try:
                # もし出品数以上のページに飛んだらエラーが出た場合(例：出品数115、飛んだ先のページが151であるとき)
                # 「条件に一致する検索結果はありません。」が得られればwhile文から抜け出す,idはS1akとS1acがあるのでどちらにも対応しておく
                try:
                    end = chro.find_element_by_xpath('//*[@id="S1ak"]/p/em')
                    time.sleep(1)
                    running = False
                except:
                    end = chro.find_element_by_xpath('//*[@id="S1ac"]/p/em')
                    time.sleep(1)
                    running = False

            except Exception as e:
                # 「条件に一致する検索結果はありません。」が得られなければエラーが出てこちらに移る
                # 次の50件に移る
                cnt += 50
                print('このページは全て見終えたのでhttps://auctions.yahoo.co.jp/seller/'+seller+'&b='+str(cnt)+'に移動します。')
                chro.get('https://auctions.yahoo.co.jp/seller/'+seller+'&b='+str(cnt))
                lots_count = 0
                time.sleep(1)

        print('{}は見終わったので次のアカウントをウォッチリスト登録します'.format(seller))

print('{}はアカウントを全て見終わったのでログアウトします。'.format(name))
chro.get('https://auctions.yahoo.co.jp/')
time.sleep(1)
chro.find_element_by_link_text('ログアウト').click()
time.sleep(1)

print("指定したすべてのアカウントの商品をウォッチリスト登録終了しました。")

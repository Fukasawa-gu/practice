# -*- coding: utf-8 -*-
"""
Created on Mon May 22 20:57:42 2018

"""

#メルカリのデータをスクレイピング
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import WebDriverException
import re
import time
import datetime
import requests
import xlwt

# Excelのシート作成
book = xlwt.Workbook()
sheet1=book.add_sheet('sheet1')
# chroを定義
try:
    chro = webdriver.Chrome()
except:
    chro = webdriver.Chrome('C:/selenium/chromedriver')# chromedriverのpathを通しておく

def searchLink(linkString):
    elem_last_btn=chro.find_element_by_link_text(linkString)
    elem_last_btn.click()
    time.sleep(1)

def xpath_click(xpath):
    input = chro.find_element_by_xpath(xpath)
    input.click()
    time.sleep(1)

# ラクマログイン
name = "XXXXX@yahoo.co.jp"#アカウントのメールアドレス
passwd = "XXXXXX"# パスワード
chro.get('https://rakuma.rakuten.co.jp/home/')

searchLink("会員登録・ログイン")

input = chro.find_element_by_name('u')
input.send_keys("{}".format(name))
time.sleep(1)


input = chro.find_element_by_name('p')
input.send_keys("{}".format(passwd))
time.sleep(1)

xpath_click('//*[@id="loginInner"]/p[1]/input')

# 出品リストに移動
xpath_click('/html/body/div[2]/div[1]/div[3]/button')
xpath_click('/html/body/div[2]/div[1]/div[3]/div/ul/li[7]/a')

n = 1# nを開始したいページ数に変える
chro.get('https://rakuma.rakuten.co.jp/mypage-web/selling-list/?page=' + str(n))

try:
    # ページ内の商品(20個)を順に見ていく
    k = 0
    while(True):
        for i in range(1, 21):
            print(i)
            a = chro.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[8]/ul/li[%s]/a/span[5]/span"%i)
            status = a.get_attribute('innerHTML')
            # 出品中かの判断
            if status == '出品停止中':
                continue
            else:
                # 詳細、タイトル、価格を得る
                xpath_click('/html/body/div[1]/div[3]/div/div[8]/ul/li[%s]/a'%i)
                title = chro.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[1]/h1').get_attribute('innerHTML')
                description = chro.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[2]/div[2]/div[1]/p').get_attribute('innerHTML')
                price = chro.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[2]/div[2]/div[2]/div[1]/dl/dd[1]').get_attribute('innerHTML')
                price = price.replace(',','')
                price = price.replace('￥','')
                print('-----------------------------------')
                print(description)
                print('-----------------------------------')
                print(title)
                print('-----------------------------------')
                print(price)

            gazos = {}
            #画像のアドレスを辞書に追加
            for j in range(1,5):
                print(j)
                try:
                    xpath_click('/html/body/div[2]/div[4]/div/div[2]/div[1]/div/ul/li[%s]'%j)
                    gazos[j] = chro.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[2]/div[1]/div/div/div/img').get_attribute('src')
                    res = requests.get(gazos[j])
                    with open('C:/Users/fukasawagu/Desktop/rakuma_merukari//img{0}_{1}.jpg'.format(i+k-1,j+1), 'wb') as img:# path指定して画像を保存
                        img.write(res.content)

                except NoSuchElementException:
                    pass

            print(gazos)

            # Excelに書き込み
            sheet1.write(i+k-1, 0, str(n)+'-'+str(i))
            sheet1.write(i+k-1, 1, title)
            sheet1.write(i+k-1, 2, price)
            sheet1.write(i+k-1, 3, description)
            sheet1.write(i+k-1, 4, status)
            sheet1.write(i+k-1, 5, gazos[1])
            sheet1.write(i+k-1, 6, gazos[2])
            sheet1.write(i+k-1, 7, gazos[3])
            sheet1.write(i+k-1, 8, gazos[4])
            book.save('C:/Users/fukasawagu/Desktop/rakuma_merukari/rakuma_merukari.csv')# path指定してExcelファイルを保存
            chro.back()
            time.sleep(1)

        k += 20
        n += 1
        # 次のページへ
        xpath_click('/html/body/div[1]/div[3]/div/div[9]/ul/li[6]/a')
except Exception as e:
    print(e)
print(page_dic)
print('end')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime as dt
import xlrd
from selenium.webdriver.common.alert import Alert

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import time
import types
import xlwt
import requests
import os
from time import sleep
import pandas as pd

book = pd.read_excel("C:/Users/antylink/Desktop/merukari_data/merukari_data.xlsx", index_col=0)

# df.to_excel("C:/Users/antylink/Desktop/merukari_data/merukari_data.xlsx")

def searchLink(linkString):
    elem_last_btn=chro.find_element_by_link_text(linkString)
    elem_last_btn.click()
    time.sleep(1)

def xpath_click(xpath):
    input = chro.find_element_by_xpath(xpath)
    input.click()
    time.sleep(1)

chro = webdriver.Chrome()
name = "hiroshi_watanabe_hiroshi@yahoo.co.jp"
passwd = "1114253internet314"
chro.get('https://fril.jp/')
time.sleep(1)

searchLink("ログイン")

input = chro.find_element_by_id('email')
input.send_keys("{}".format(name))
time.sleep(1)


input = chro.find_element_by_id('password')
input.send_keys("{}".format(passwd))
time.sleep(1)

xpath_click('//*[@id="new_user"]/div[3]/input')

try:
    for i in range(len(book)):
        chro.get('https://fril.jp/item/new')
        try:
            title = book.iloc[i, 0]
            price = book.iloc[i, 1]
            description = book.iloc[i, 2].replace('<br>','\n')
            condition = book.iloc[i, 3]
            photo1 = book.iloc[i, 4]
            photo2 = book.iloc[i, 5]
            photo3 = book.iloc[i, 6]
            photo4 = book.iloc[i, 7]
            photos = [photo1, photo2, photo3, photo4]
            print(title)
            print(price)
            print(description)
            print(condition)
            print(photo1)
            print(photo2)
            print(photo3)
            print(photo4)

            dirname = 'C:/Users/antylink/Desktop/merukari_data/'
            for j in range(4):
                try:
                    dir_photo = dirname + photos[j]
                    upload_photo = chro.find_element_by_xpath('//*[@id="files"]/div[{}]/div[2]/input'.format(j+1))
                    time.sleep(1)
                    upload_photo.send_keys(dir_photo)
                    time.sleep(1)
                except Exception as e:
                    print(e)
                    pass

            xpath_click('//*[@id="category_name"]')
            xpath_click('//*[@id="select-category"]/div/div/div[2]/div/div[14]/a')
            xpath_click('//*[@id="menu_13"]/div[2]/a')
            xpath_click('//*[@id="menu_13_1"]/a[2]')

            for j in range(1,7):
                status = chro.find_element_by_xpath('//*[@id="status"]/option[{}]'.format(j)).get_attribute('innerHTML')
                if status == condition:
                    xpath_click('//*[@id="status"]/option[{}]'.format(j))

            xpath_click('//*[@id="delivery_date"]')
            xpath_click('//*[@id="delivery_date"]/option[2]')

            xpath_click('//*[@id="delivery_area"]')
            xpath_click('//*[@id="delivery_area"]/option[13]')

            input_title = chro.find_element_by_xpath('//*[@id="name"]')
            time.sleep(1)
            input_title.send_keys(title)
            time.sleep(1)

            input_description = chro.find_element_by_xpath('//*[@id="detail"]')
            time.sleep(1)
            input_description.send_keys(description)
            time.sleep(1)

            input_price = chro.find_element_by_xpath('//*[@id="sell_price"]')
            time.sleep(1)
            input_price.send_keys(int(price))
            time.sleep(1)

            xpath_click('//*[@id="confirm"]')
            time.sleep(3)
            xpath_click('//*[@id="submit"]')
            time.sleep(3)
        except:
            continue
except Exception as e:
    print(e)
    print('end')

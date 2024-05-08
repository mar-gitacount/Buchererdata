# -*- coding: utf-8 -*-
import os
import json
import csv
from bs4 import BeautifulSoup
import requests
import re
import sys
from openpyxl import Workbook, load_workbook
from datetime import datetime
from itertools import product
import os
import json
from datetime import datetime


from selenium import webdriver
from bs4 import BeautifulSoup
import re
from openpyxl import Workbook, load_workbook
from datetime import datetime
import pandas as pd
import os
import sys
from selenium.webdriver.chrome.options import Options

# ?ページのソースコードを読み込む
def get_page_source(url,optionsflg = True):
    """
    Given a URL, use WebDriver to access the page, retrieve its source code,
    and return a BeautifulSoup object.
    """
    if optionsflg:
        options = Options()
        options.add_argument("--headless")  
        # WebDriverのインスタンスを作成
        driver = webdriver.Chrome(options=options)  # Chromeを使用する場合。他のブラウザを使う場合は適宜変更してください。
    else:
        driver = webdriver.Chrome()
    # 指定されたURLにアクセス
    driver.get(url)
    # options = Options()
    # options.add_argument("--headless")  # ヘッドレスモードを有効にする
    # driver = webdriver.Chrome(options=options)  # または他のブラウザに合わせて選択
    # ページのソースコードを取得
    page_source = driver.page_source
    # ページのソースコードをBeautiful Soupオブジェクトに変換
    soup = BeautifulSoup(page_source, "html.parser")
    # WebDriverを終了
    driver.quit()
    return soup




def get_dir(adddir=""):
    # ディレクトリ取得する。
    script_dir = os.path.dirname(__file__)
    if adddir:
        file = os.path.join(adddir, script_dir)
        return file
    else:
        file = script_dir
        return file


def check_key_in_master(json_file, key="", checkdatas="master"):
    with open(json_file, "r", encoding="utf-8") as file:
        json_data = json.load(file)
        master_data = json_data.get(checkdatas, {})
        if key:
            for item_key, item_value in master_data.items():
                if item_key == key:
                    return item_value
        else:
            data = json_data.get(checkdatas)
            items = []
            for item_key, item_value in data.items():
                itemdic = {item_key: item_value}
                items.append(itemdic)
            return items


# !jsonファイルの近い日付を取得する関数-ここから-
# ?第一引数=ジェイソンファイル,第二引数=確認する日付
# ?main.jsonのアイテムと日付を配列ですべて返す
def json_near_date_get(jsonfile, checkdate, beforeweeks=4):
    with open(jsonfile, "r", encoding="utf-8") as file:
        data = json.load(file)
    valid_dates = []
    array = []

    date_keys = []
    # 各日付のデータを格納する辞書を初期化
    date_data = {}
    item_data_only = {}
    for section in data.values():
        if isinstance(section, dict):
            for key, value in section.items():
                try:
                    datetime.strptime(key, "%Y-%m-%d")
                    # 日付内データを格納する
                    datevalue = check_key_in_master(json_file=jsonfile, checkdatas=key)
                    # key = 日付　datevalue = 各アイテムと、その中の値段データ

                    # 日付をキーにしたアイテムデータ
                    # key = 日付
                    items = {key: datevalue}
                    # 日付キー
                    datekey = list(items.keys())[0]
                    datevaluekeys = [list(item.keys())[0] for item in datevalue]

                    # 日付データを格納
                    # keyとitems=valueにする。

                    # 辞書を作る
                    # 日付キーと値をセットする。
                    date_data[key] = datevaluekeys
                    # 日付キー配列を作る。
                    date_keys.append(key)
                    # valid_dates.append(key)
                    # valid_dates.append(items)
                except ValueError:
                    pass
    # 実行日に最も近い日付を見つける
    # valid_datesは日付データ一覧
    # print(valid_dates)
    print("-----------ここが辞書型------------")
    date_objects = [datetime.strptime(date, "%Y-%m-%d").date() for date in date_keys]
    sorted_dates = sorted(date_objects, key=lambda x: abs(datetime.now().date() - x))
    formatted_dates = [date.strftime("%Y-%m-%d") for date in sorted_dates]
    # print(formatted_dates, "フォーマット修正した配列")
    # 日付ループする
    for date in formatted_dates:
        for j in range(date + 1, len(formatted_dates)):
            print(
                "Set",
                date + 1,
                "と Set",
                j + 1,
                "の組み合わせ:",
                date_data[date],
                date_data[j],
            )

    # 最初の4つの日付を取得
    nearest_dates = sorted_dates[:beforeweeks]
    # 直近データの辞書を取得しなければならない
    formatted_dates = [date.strftime("%Y-%m-%d") for date in nearest_dates]
    # 再度jsonファイルを読み込んで、直近データの辞書をすべて取得する。
    nearest_date = min(
        valid_dates,
        key=lambda x: abs(checkdate - datetime.strptime(x, "%Y-%m-%d").date()),
    )
    return nearest_date


# !jsonファイルの近い日付を取得する関数-ここまで-

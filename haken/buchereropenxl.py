import openpyxl
import os
import pandas as pd
from datetime import datetime
from openpyxl.styles import PatternFill, Font
from mypackage import utils

# !jsonファイルのパス
# BuchererMainDatasjson = "BuchererDatas/BuchererMainDatas.json"
# 方法1：現在のスクリプトファイルのディレクトリパスを取得
script_dir = os.path.dirname(__file__)
# ファイルパスを連結する際にスラッシュを追加する
BuchererMainDatasjson = os.path.join(script_dir, "BuchererDatas/BuchererMainDatas.json")

# 本日の日付を取得する
today_date = datetime.now().date()
# 5週ループする
# 直近の週を取得する
near_date = utils.json_near_date_get(BuchererMainDatasjson, today_date)
near_date = datetime.strptime(near_date, "%Y-%m-%d").date()
dateitems = []

# !5週する処理を書く
week = 0
while week < 5:
    # この時点で、各週ごとのアイテムを格納する二次元配列にするもしくは辞書型
    dateitems.append(near_date)
    near_date = utils.json_near_date_get(BuchererMainDatasjson, near_date)
    print(near_date)
    near_date = datetime.strptime(near_date, "%Y-%m-%d").date()
    week += 1

# print(dateitems)

# print(getdir, "はメソッドから帰ってきたディレクトリ")

current_directory = os.getcwd()
# エクセルファイルのパスを指定
# excel_file_path = r'C:\Users\01794\Desktop\仕事でつかうやつ\Buchererデータ抽出\エクセル\BUCHRER CPOリスト2024.01.22最新.xlsx'
# !エクセルパスは指定しておく
# excel_file_path = r"エクセル\BUCHRER CPOリスト2024.03.04訂正.xlsx"
# # エクセルファイルの絶対パスを生成
# xlsx_file_path = os.path.join(current_directory, excel_file_path)


# # 当月シートを取得するための変数を取得

# # 現在の日付を取得
# current_date = datetime.now()

# # 今月の月を取得 (1月なら1、2月なら2、...)
# current_month = current_date.month

# # "月"という文字列に追加
# month_sheet_name = str(current_month) + "月"

# # エクセルファイルを開く
# workbook = openpyxl.load_workbook(excel_file_path)

# # 指定されたシートを取得
# sheet = workbook[month_sheet_name]

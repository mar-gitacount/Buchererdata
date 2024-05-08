import os
import json
import csv
from bs4 import BeautifulSoup
import requests
import re
import sys
from datetime import datetime
from mypackage import utils

# !jsonファイルのパス
BuchererMainDatasjson = "BuchererDatas/BuchererMainDatas.json"

# 新しいデータ作成処理
# 現在の日付と時刻を取得
current_datetime = datetime.now()
# 現在の日付を取得（年-月-日）
current_date = current_datetime.date()
# 現在の時刻を取得（時:分:秒.マイクロ秒）
current_time = current_datetime.time()
# 取得日をjsonファイルデータ名にする
json_datagetnow = str(current_date)


# jsonファイルに存在するかどうか確認する
def check_key_in_master(json_file, key, checkdatas="master"):
    with open(json_file, "r", encoding="utf-8") as file:
        json_data = json.load(file)
        master_data = json_data.get(checkdatas, {})
        return key in master_data


# jsonファイルに追加する。
def add_data_to_master(json_file, key, data, checkdatas="master"):
    with open(json_file, "r+", encoding="utf-8") as file:
        json_data = json.load(file)
        master_data = json_data.setdefault(checkdatas, {})
        if key not in master_data:
            master_data[key] = data
            file.seek(0)
            json.dump(json_data, file, indent=4)
            print(f'キー "{key}" のデータが "{checkdatas}" に追加されました。')
        else:
            print(f'キー "{key}" は既に "{checkdatas}" 内に存在します。')


# 日付データを入れる処理
add_data_to_master(
    BuchererMainDatasjson, key=json_datagetnow, data={}, checkdatas="date"
)
# 新しいCSVファイルのパス
csv_file_path = "新しいファイル.csv"
current_directory = os.getcwd()
html_relative_path = "test.html"
urlcsv_relative_path = "url.csv"
# HTMLファイルの絶対パスを生成
html_file_path = os.path.join(current_directory, html_relative_path)
item_name = {0: ""}
csv_input_data = []
# CHFの正規表現パターン
chf_pattern = re.compile(r"\bCHF\b")
brbproducts_list_array = []
brbproducts_list_array_index = 0
brbproduct = ""
single_rowdata = []

# CSVファイルを書き込みモードで開く
with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
    try:
        with open(html_file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
            brbproducts_list = soup.find_all(
                class_="brb-products__list"
            )  # クラス名を修正
            page_array_index = 0

            for item in brbproducts_list:
                input_text = item.text
                text = input_text.splitlines()

                for item in text:
                    if not item.strip():
                        continue
                    else:
                        brbproduct += brbproduct + "\n" + item

                        chf_match = chf_pattern.search(item)
                        if chf_match:
                            brbproducts_list_array.append(brbproduct)
                            print(brbproducts_list_array[brbproducts_list_array_index])
                            brbproducts_list_array_index += 1
                            brbproduct = ""
                            print("----------------")

            # aタグを取得する
            # class="brb-products__item__link brb-products__item__link--cpo"

        brbproducts_list_array_index = 0

        with open(urlcsv_relative_path, "w", newline="", encoding="utf-8") as url_file:
            url_csv_writer = csv.writer(url_file)
            brbproducts_url_list = soup.find_all(class_="brb-products__item__link")
            print(f"要素数表題数:{len(brbproducts_list_array)}")
            print(f"要素数リンク={len(brbproducts_url_list)}")

            for itemurl in brbproducts_url_list:
                # data-tracking属性からJSONデータを取得
                data_tracking = itemurl.get("data-tracking-ga4")
                data_json = json.loads(data_tracking)
                # 年代を初期化
                extracted_year = ""
                print(data_json)
                print("----------------------------------------")
                # print(brbproducts_list_array[brbproducts_list_array_index])
                # print(brbproducts_list_array_index)
                print("二つの値を比べる")
                # item_idを抽出
                item_id = data_json.get("item_id")
                item_id = item_id + ".html"
                item_name = data_json.get("item_name")
                inputuse_item_name = item_name.strip()
                item_name = item_name.replace("Certified Pre-Owned", "")
                item_name = item_name.replace("  ", "")
                item_name = item_name.replace(" ", "-")
                # 大文字を小文字に変換する
                item_name = item_name.lower()
                url = (
                    "https://www.bucherer.com/rolex-certified-pre-owned/watches/"
                    + item_name
                    + "/"
                    + item_id
                )
                outarray = []
                pagearray = []
                response = requests.get(url)

                print(f"商品のURL={url}")
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")
                    results = soup.find_all(class_="brb-product__detail-specs__value")
                    joint_text = ""
                    # 正規表現パターン
                    guarantee_pattern = re.compile(r"\bsales guarantee\b")
                    # テキストを繰り返す
                    for result in results:
                        # マッチング
                        resultmatch = guarantee_pattern.search(result.text)
                        print(result.text)
                        joint_text += "\n" + result.text
                        # print(joint_text)
                        # print("マッチしない値も含めた場合は上")
                        # if resultmatch:
                        #     print("値がマッチ")
                        #     pagearray.append(result.text)
                        #     joint_text = brbproducts_list_array[brbproducts_list_array_index] + "\n"+ joint_text
                        #     # ここでcsvのデータを追加
                        #     csv_input_data.append(joint_text)
                        #     print(joint_text)
                        #     print(f'配列1:{brbproducts_list_array_index}')
                        #     print(f'配列2:{len(csv_input_data)}')
                        #     print("------")
                        #     brbproducts_list_array_index += 1

                        #     joint_text = ''
                    joint_text = (
                        brbproducts_list_array[brbproducts_list_array_index]
                        + "\n"
                        + joint_text
                    )
                    with open("output.txt", "w") as f:
                        # リダイレクトを元に戻す
                        sys.stdout = f
                        sys.stdout = sys.__stdout__
                        print(
                            f"{brbproducts_list_array_index}の{ joint_text}がすべてのテキスト"
                        )
                        # 下から1行目と2行目を取得
                        lines = joint_text.split("\n")
                        bottom_lines = "\n".join(lines[-1:])
                        guarantee_match_serch = guarantee_pattern.search(bottom_lines)
                        if guarantee_match_serch:
                            bottom_lines = "\n".join(lines[-2:])
                            print(f"{bottom_lines}を表示")

                        # size_and_material_pattern = re.compile(r'(\d+ mm, .+?)\s+CHF ([\d,']+)')

                        # size_pattern = re.compile(r'(\d+)\s*mm')
                        details_pattern = re.compile(
                            r"(\d+)\n([\d-]+)\n(\d+ mm)\n(.+?)\n(.+?)\n(.+?)\n(.+?)\n(\d+)\n(\d+ h)\n(.+?)\n(.+?)"
                        )
                        size_and_material_pattern = re.compile(
                            r"(\d+ mm, .+?)\s+CHF ([\d,\']+)"
                        )
                        # グループの取得方法を修正
                        # chf_pattern = re.compile(r'\bCHF\b')
                        # chf_num = chf_match.search(joint_text)

                        # datails_match = details_pattern.search(joint_text)
                        # reference_number = datails_match.group(1)
                        # year_number = datails_match.group(2)
                        # size_number = datails_match.group(3)
                        # print(f'年代{year_number}')
                        # print(f'サイズ{size_number}')

                        # datails_match = details_pattern.search(joint_text)

                        # reference_number = datails_match(1)
                        # id_number = datails_match(2)
                        # ロットナンバーの正規表現パターン
                        Lot_pattern = re.compile(r"\d{4}-\d{3,}-\d{1,}")
                        Ref_pattern = re.compile(r"\b\d{5,6}\b")
                        # Ref_pattern = re.compile(r"\b[\w\d]{5,10}\b")
                        # 4桁の年代を抽出する正規表現パターン
                        year_pattern = re.compile(r"(\d{4})")

                        # 1900年から2000年代までの範囲を判定する正規表現パターン
                        range_pattern = re.compile(r"^(19\d{2}|20\d{2})$")

                        # size_and_material_pattern = re.compile(r'(\d+ mm, .+?)\s+CHF ([\d,\']+)')
                        size_and_material_match = size_and_material_pattern.search(
                            joint_text
                        )

                        year_match = year_pattern.search(joint_text)
                        guarantee_match = guarantee_pattern.search(joint_text)
                        # if guarantee_match:

                        if year_match:
                            extracted_year = year_match.group(1)
                            # 1900年から2000年代までの範囲を判定
                            range_match = range_pattern.search(extracted_year)
                            print(f"{extracted_year}年代")
                            if 1900 > int(extracted_year) or 2500 < int(extracted_year):
                                print("年代でない")
                                extracted_year = ""

                        # print(f'{year_match.group(2)}年代')
                        # マッチング
                        matches = Lot_pattern.findall(joint_text)
                        print(
                            "-----------------マッチングまでは完了している---------------------"
                        )
                        # ロットナンバー取得する
                        try:
                            desired_match = next(
                                match for match in matches if "-" in match
                            )
                        except Exception as e:
                            # 他のすべての例外に対する処理
                            print(f"例外が発生しました: {e}:次のループに入ります")
                            continue
                        print(
                            "-----------------LOTまではマッチングまでは完了している---------------------"
                        )
                        print(f"LO{desired_match}")

                        # リファレンスマッチング
                        Ref_matches = Ref_pattern.findall(joint_text)
                        if Ref_matches:
                            for Ref_matche in Ref_matches:
                                print(f"{Ref_matche}リファレンス")
                        else:
                            print("マッチする行が見つかりませんでした。")

                        # print(f'リファレンス{Ref_matches}')
                        size = size_and_material_match.group(1)

                        # サイズを抽出する正規表現パターン
                        size_pattern = re.compile(r"(\d+)\s*mm")
                        # サイズマッチング
                        size = size_pattern.search(size)
                        size = size.group(1) + "mm"
                        print(f"{size}がサイズ")
                        # 金額
                        price = size_and_material_match.group(2).replace("'", "")
                        print(price)
                        single_rowdata = []
                        # ここでjsonファイルに入稿する。
                        # リファレンスナンバーで管理する
                        key_to_add = desired_match
                        data_to_add = {
                            "model": inputuse_item_name,
                            "year": extracted_year,
                            "ref": Ref_matche,
                            "size": size,
                            "price": price,
                            "bracelet": "",
                            "dial": bottom_lines,
                            "url": url,
                        }

                        if not check_key_in_master(BuchererMainDatasjson, key_to_add):
                            add_data_to_master(
                                BuchererMainDatasjson,
                                data=data_to_add,
                                key=key_to_add,
                                checkdatas="master",
                            )
                        else:
                            print(
                                f'キー"{key_to_add}"はすでにmasterに存在しています。追加処理は行われませんでした。'
                            )
                        # 日付jsonデータにリファレンスナンバーのみ入稿する。

                        add_data_to_master(
                            BuchererMainDatasjson,
                            data={"price": price},
                            key=key_to_add,
                            checkdatas=json_datagetnow,
                        )
                        # ?フロー
                        # アイテムナンバーが先週に存在するか→しない先々週→...いちども存在しない場合、赤文字で追加する。
                        # これは別ファイルでjsonを確認して実行する？全ての日付データ数を取得する。
                        # 毎回データを取りにいく。
                        # jsonファイル処理ここまで

                        single_rowdata.append(desired_match)
                        single_rowdata.append(inputuse_item_name)
                        single_rowdata.append(extracted_year)
                        single_rowdata.append(Ref_matche)
                        single_rowdata.append(size)
                        single_rowdata.append(price)

                        single_rowdata.append(bottom_lines)
                        single_rowdata.append(url)

                        # price  = size_and_material_match.group(2).replace("'", "")
                        # # パターンの正規表現
                        # print(f'{id_number}はid')
                        # print(f'{price}が金額')
                    csv_input_data.append(single_rowdata)
                    joint_text = ""
                    single_rowdata = []
                    brbproducts_list_array_index += 1
                else:
                    print("通信失敗")
                    brbproducts_list_array_index += 1
                # 新しい行を追加
                url_csv_writer.writerow([url])
                if data_tracking:
                    # JSONデータを辞書に変換
                    data_dict = json.loads(data_tracking)
                    # 'url'キーからURLを取得
                    url = data_dict.get("url")
                    # if url:
                    # print(url)
        # main.json(全ての製品データ。)に存在するかチェックする。
        # Ref_matcheで検索する。
        # ? csv_input_dataの[RefNomber]をmain.jsonを検索する。

        # CSVファイルを書き込みモードで開く
        with open("output.csv", "w", newline="", encoding="utf-8") as csvfile:
            # CSVライターを作成
            csvwriter = csv.writer(csvfile)
            # JSONファイルにも保存して、永続的にする。
            # データをCSVファイルに書き込む
            csvwriter.writerows(csv_input_data)
    # print("CSVファイルが作成されました。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

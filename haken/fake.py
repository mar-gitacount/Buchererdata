from mypackage import utils
import json
import random

# 文字列をjson形式にする
def parse_json_string(json_string):
    try:
        json_data = json.loads(json_string)
        return json_data
    except json.JSONDecodeError as e:
        print("JSONデコードエラー:", e)
        return None
    

def check_key_in_master(json_file, key, checkdatas="master"):
    with open(json_file, "r", encoding="utf-8") as file:
        json_data = json.load(file)
        master_data = json_data.get(checkdatas, {})
        for item_key, item_value in master_data.items():
            if item_key == key:
                return item_value
# URLアクセス。
# ランダムなURL→jsonデータから抽出する。
# ランダムな処理、4通りくらい。
# JSONファイルのパス
BuchererMainDatasjson = "BuchererDatas/BuchererMainDatas.json"

# JSONファイルを読み込む。
with open(BuchererMainDatasjson, "r", encoding="utf-8") as file:
    data = json.load(file)
# マスターデータを抽出する。
master = data["master"]
# print(master)
# アイテムをコピーする
master_items_copy = dict(master)

num = 0
# 10回繰り返す。
while num < 10:
    random_key, random_value = random.choice(list(master.items()))
    # ランダムキーをjsonデータを抽出する。
    # 辞書型からurlを抽出する。
    url = random_value['url']
    utils.get_page_source(url,False)
    print(url)
    print("-------------------------")
    # コールバック関数は引数に関数を渡す。
    # 関数Aの引数に関数Bを渡す関数A内で関数Bを使うことができる。これを関数B'とする。関数A内で関数B'を使うことができる。
    # get_page_sourceを受け取るコールバック関数を作る？
    # get_page_sourceからは、ページソースが返ってくる。
    # つまり、get_page_sourceを引数として受け取る関数を作る？
    # ランダムなコールバック関数を使う。


    # url = random_value.url
    # print(url)
    num += 1
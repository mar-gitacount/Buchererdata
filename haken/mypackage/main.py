# main.py

# オリジナルメソッドを含む外部ファイルから必要なメソッドをインポートする
from .utils import json_near_date_get, getdir, get_page_source

# メインの処理
def main():
    # オリジナルメソッドを呼び出す
    json_near_date_get()
    # getdir()
    get_page_source()

# スクリプトが直接実行された場合にmain()関数を呼び出す
if __name__ == "__main__":
    main()
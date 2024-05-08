from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mypackage import utils
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import subprocess
from datetime import datetime
def is_scrolled_to_bottom(driver):
    # JavaScriptを実行してスクロールが一番下にあるかどうかを判定
    script = """
    function isScrolledToBottom() {
        var scrollPosition = window.scrollY || window.pageYOffset || document.documentElement.scrollTop;
        var pageHeight = document.documentElement.scrollHeight;
        return (scrollPosition + window.innerHeight) >= pageHeight;
    }
    return isScrolledToBottom();
    """
    return driver.execute_script(script)

def wait_for_element(driver, locator, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
        print(element)
        print("要素が見つかりました")
        return element
    except TimeoutException:
        print("要素が見つかりませんでした。")
        return None

# デバッグ書き込み用関数
def debug_insert_text(txt,file_path):
    if os.path.exists(file_path):
        print(f"ファイルが存在します。上書きします: {file_path}")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(str(txt))
    else:
        print(f"ファイルが存在しません。新しいファイルを作成します: {file_path}")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(str(txt))
    # print("デバッグ情報を書き込みます。")


today_date = datetime.now().date()

file_name = f"debaug_{today_date}.txt"

# WebDriverを初期化
driver = webdriver.Chrome()
# https://www.bucherer.com/rolex-certified-pre-owned/watches?srule=Ranking+by+Category+Position&sopt=relevance&start=0&sz=54

# Webページに移動
driver.get("https://www.bucherer.com/rolex-certified-pre-owned/watches?srule=Ranking+by+Category+Position&sopt=relevance&start=0&sz=54")







# !button = wait_for_element(driver, (By.CLASS_NAME, "brb-btn"),100)
# button.click()

#? 11で datetime <= timestamp
test = utils.get_page_source("https://www.bucherer.com/rolex-certified-pre-owned/watches?srule=Ranking+by+Category+Position&sopt=relevance&start=0&sz=54")
# testbtnget = test.find_all("button",class_="brb-btn")
# ?whileで繰り返す。
# ボタンがNoneになるまで
# オブジェクトがNoneの場合、以下をFalseにする。
brb_btn_flg = True


# スクロールして、maxheightと同じ場合処理を抜ける。
scrollflg = True
# brb-products__list product-grid
# driver.execute_script("arguments[0].scrollIntoView();",show_more_get_test)

# ?スクロールテスト
time.sleep(4)
# ページの一番下までスクロールするためにJavaScriptを実行する
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(4)
# ?headerサイズ座標

# ?footerサイズ座標
scroll_element_footer = wait_for_element(driver,(By.CLASS_NAME, "m-footer"),100)
# フッター要素の位置を取得
footer_location = scroll_element_footer.location
# scroll_element_footer_height = scroll_element_footer.size['height']
# scroll_element_blbfooterget = wait_for_element(driver,(By.CLASS_NAME, "brb-footer"),100)
# scroll_element_blbfooterget_heght = scroll_element_blbfooterget.size['height']

# ?ボタンのエレメントを取得する。
# scroll_element = wait_for_element(driver,(By.CLASS_NAME, "show-more"),100)
# scroll_element = driver.find_element(By.CLASS_NAME, "show-more")
# !scroll_element = wait_for_element(driver,(By.CLASS_NAME, "m-footer"),100)
# scroll_element = wait_for_element(driver,(By.CLASS_NAME, "brb-products__item"),100)
# product product-tile brb-products__item


# !以下をwhile文内に入れる。
# 複数の要素を見つける（各時計アイテムを取得する。）
elements = driver.find_elements(By.CLASS_NAME, "brb-products__item")
# 最後の要素を取得
last_element = elements[-1]
print(elements)

# ?要素までスクロール
actions = ActionChains(driver)
actions.move_to_element(last_element).perform()

# ?ボタンをチェックする。
button = wait_for_element(driver, (By.CLASS_NAME, "brb-btn"),10)
time.sleep(5)
# デバッグテキスト用変数
debug_element = ""
gauge = "-"
# ボタンの存在がTrueの場合、実行する。
while button is not None:
    # ボタンが存在し、エラーの場合は、100pxずつずらして確認する。
    # time.sleep(2)
    gauge += "-"
    print(gauge)
    print("ボタン探しループ内")  
    # ?ここで、footer位置と同様の場合、上に上がる処理
    scroll_position = driver.execute_script("return window.scrollY;")
    
    print("ページの垂直スクロール位置:", scroll_position)
    # スクロール情報をデバッグファイルに書き込む
    debug_insert_text("ページの垂直スクロール位置:"+str(scroll_position),file_name)
    scroll_element_footer = wait_for_element(driver,(By.CLASS_NAME, "m-footer"),100)
    # フッター要素の位置を取得
    footer_location = scroll_element_footer.location
    print("フッターの座標: x=", footer_location['x'], ", y=", footer_location['y'])
    debug_insert_text("フッターの座標: x="+ str(footer_location['x']) + "y="+str(footer_location['y']),file_name)

    # スクロールが一番下にあるかどうかを判定
    if is_scrolled_to_bottom(driver):
        print("スクロールが一番下にあります")
    else:
        print("スクロールが一番下にありません")
    time.sleep(1)
    try:
        # 5200
        show_more_get_test = wait_for_element(driver,(By.CLASS_NAME, "show-more"),100)
        brb_btn = show_more_get_test.find_element(By.CLASS_NAME, "brb-btn")

        brb_btn.click()
        elements = driver.find_elements(By.CLASS_NAME, "brb-products__item")
        print("ボタンがありましたクリックします")
        # スクロールしたに
        # ページのスクロール位置を取得

        # footerの最後か判定して、一致したら上る。すなわち、上いったり下いったりする。

        # ここで一番に下にあるか判定する。
        # scrollflg = False
    except Exception as e:
        print("要素はあるが、ボタンがないスクロールする")
        
        driver.execute_script("window.scrollBy(0, 100);")
        # time.sleep(3)
        # 
        # actions.move_to_element(last_element).perform()
    button = wait_for_element(driver, (By.CLASS_NAME, "brb-btn"),10)
  
    if show_more_get_test is None:
        break
    # if button is None:
    #     break
print("処理抜ける")
page_source = driver.page_source
# ?アイテム部分だけを取得する。
# ?brb-products__list
target_class = "brb-products__list"
# elements_with_class = page_source.find(class_=target_class)
# 取得したページソースをHTMLファイルに書き込む
file_path = "test.html"

# ファイルが存在するかチェックし、存在する場合は上書き、存在しない場合は新規作成
if os.path.exists(file_path):
    print(f"ファイルが存在します。上書きします: {file_path}")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(page_source)
else:
    print(f"ファイルが存在しません。新しいファイルを作成します: {file_path}")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(page_source)

# 移行はjsonファイルにデータを書きこむ処理
# C:\Users\01794\Desktop\仕事でつかうやつ\Buchererデータ抽出\haken\htmlload.py
html_load_file = "htmlload.py"
jsondataloademake_file ="jsondataloadmakeexcel.py"
subprocess.run(["python",html_load_file])
subprocess.run(["python",jsondataloademake_file])


# with open("test.html", "w", encoding="utf-8") as f:
#     f.write(page_source)
# ?ここでページをすべてコピーする。
# ?utilsのメソッドを利用する。


if button:
    # この中でエラーになった場合、100ずつ下にスクロールする。
    #      try:
#         brb_btn.click()
#         # ここで一番に下にあるか判定する。
#         scrollflg = False
#      except Exception as e:
#         print("ボタンがないスクロールする")   
    print("要素がみつかりました。この場合、ボタンを押下します。")
else:
    print("要素取得エラー？")
#  footer + (全体-(アイテム+footer))だけ上にスクロールする。

# upheight = scroll_element_footer_height
# driver.execute_script(f"window.scrollBy(0, - {scroll_element_footer_height+scroll_element_blbfooterget_heght});")
# product product-tile brb-products__item brb-products__item--cpo(大きいアイテム)
time.sleep(100)


# while scrollflg:
#      driver.execute_script("window.scrollBy(0, 100);")
#      scroll_element = wait_for_element(driver,(By.CLASS_NAME, "brb-products__list"),100)
#      scroll_element_height = scroll_element.size['height']
#     #  driver.execute_script("arguments[0].scrollIntoView();",scroll_element_height)
#      print("要素の高さ",scroll_element_height)
#      driver.execute_script(f"window.scrollBy(0, {scroll_element_height});")
#     #  スクロールで一番下までいく。
#     #  footer + (全体-(アイテム+footer))だけ上にスクロールする。
#     #  ボタンを押す。

#      show_more_get_test=wait_for_element(driver,(By.CLASS_NAME, "show-more"),100)
#      brb_btn = show_more_get_test.find_element(By.CLASS_NAME, "brb-btn")


#      time.sleep(5)
#      try:
#         brb_btn.click()
#         # ここで一番に下にあるか判定する。
#         scrollflg = False
#      except Exception as e:
#         print("ボタンがないスクロールする")   


# while brb_btn_flg:
#     show_more_get = test.find("div",class_="show-more")
#     show_more_get_test=wait_for_element(driver,(By.CLASS_NAME, "show-more"),100)
#     if show_more_get_test:
#         # ?ここでボタンを押せる。
#         brb_btn = show_more_get_test.find_element(By.CLASS_NAME, "brb-btn")
#         # ここで、要素の数だけスクロールする。= アイテム数
#         scrtest = True
#         # ?
#         while scrtest:
#             # スクロールするためにJavaScriptを実行する
#             driver.execute_script("window.scrollBy(0, 100);")
#             show_more_get_test=wait_for_element(driver,(By.CLASS_NAME, "show-more"),100)
#             brb_btn = show_more_get_test.find_element(By.CLASS_NAME, "brb-btn")
#             time.sleep(5)
#             try:
#                 brb_btn.click()
#                 scrtest = False
#             except Exception as e:
#                 print("ボタンがないスクロールする")   
#         time.sleep(10)
       
#         driver.execute_script("arguments[0].scrollIntoView();",show_more_get_test)
#         time.sleep(10)
#         brb_btn.click()
#         # スクロールするためにJavaScriptを実行する
#         time.sleep(10)
#     else:
#         brb_btn_flg = False


# print(show_more_get)
# btn_get = show_more_get.find("button",class_="brb-btn")
# print(len(btn_get))

# button = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, "brb-btn")))

# # print(button)
# button = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CLASS_NAME, "brb-btn")))
# try:
#     # ボタン要素が表示されるまで待機
#     button = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, "brb-btn")))
#     # ボタンがクリック可能になるまで待機
#     button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "brb-btn")))
#     # ボタンをクリック
#     button.click()
# except Exception as e:
#     print("ボタンをクリックできませんでした:", e)

# ボタンタグを取得する。
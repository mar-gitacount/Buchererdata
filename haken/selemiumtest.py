from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# WebDriverの設定
driver = webdriver.Chrome()

# ターゲットのURLを指定
url = 'https://www.bucherer.com/rolex-certified-pre-owned/watches?srule=Ranking+by+Category+Position&sopt=relevance&start=0&sz=360'
driver.get(url)

# ページが完全に読み込まれるまで待つ
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="search-result-items"]')))

# ボタンを特定して押下
button = driver.find_element(By.XPATH,  '//button[@class="brb-btn"]')
button.click()

# ボタンを押した後に生成される要素が表示されるまで待つ
element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="your-generated-element-class"]')))

# 生成された要素の内容を表示
print(element.text)

# ブラウザを閉じる
driver.quit()

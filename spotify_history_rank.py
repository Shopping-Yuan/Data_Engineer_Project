import subprocess
result = subprocess.run(['google-chrome', '--version'], capture_output=True, text=True)
chrome_version = result.stdout.strip().split()[-1]
print(f"Chrome Version: {chrome_version}")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.88 Safari/537.36"
Referer = "https://charts.spotify.com/"
A_L = "zh-TW,zh;q=0.9 zh-TW,zh;q=0.9"
Accept = "*/*"
A_E = "gzip, deflate, br, zstd"
SFM = "cors"
SFS = "cross-site"

SChUA = '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"'
SChUAM = '?0'

chrome_options.add_argument(f"Referer={user_agent}")
chrome_options.add_argument(f"Accept-Language={A_L}")
chrome_options.add_argument(f"Accept={Accept}")
chrome_options.add_argument(f"Accept-Encoding={A_E}")
chrome_options.add_argument(f"Sec-Fetch-Mode={SFM}")
chrome_options.add_argument(f"Sec-Fetch-Site={SFS}")
chrome_options.add_argument(f"Sec-Ch-UA={SChUA}")
chrome_options.add_argument(f"Sec-Ch-UA-Mobile={SChUAM}")
profile_path = './'
chrome_options.add_argument(f'user-data-dir={profile_path}')

chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
# 初始化 WebDriver
driver = webdriver.Chrome(options=chrome_options)
# 打開登錄頁面
driver.get("https://charts.spotify.com/home")  # 替換為實際登錄頁面 URL
driver.get_screenshot_as_file("first.png")
time.sleep(1)
login_field = driver.find_element(By.XPATH, "//*[@class='Button-sc-qlcn5g-0 icaoRV encore-text-body-medium-bold']")
time.sleep(1)
login_field.click()
driver.get_screenshot_as_file("login_page.png")
wait = WebDriverWait(driver, 10)
# driver.get("https://accounts.spotify.com/zh-TW/login?continue=https%3A%2F%2Fcharts.spotify.com/login")
u_field = wait.until(EC.presence_of_element_located((By.ID, "login-username")))
p_field = wait.until(EC.presence_of_element_located((By.ID, "login-password")))
time.sleep(1)
driver.find_element(By.XPATH, "//*[@class='Button-sc-1dqy6lx-0 dOClrT']").click()

username = input("請手動輸入名稱，完成後按 Enter 鍵繼續...")
u_field.send_keys(username)
password = input("請手動輸入密碼，完成後按 Enter 鍵繼續...")
p_field.send_keys(password)
# 提交表單
try:
    # login_button = WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-testid='login-button']")) )
    login_button = driver.find_element(By.ID, "login-button")
    time.sleep(1)
    login_button.click()
except Exception as e:
    print("登入按鈕未能找到或點擊失敗:", e)
finally:
  # 確認登錄成功
  driver.get_screenshot_as_file("final.png")
  time.sleep(1)
  html = driver.page_source
  spotify_bs4 = BeautifulSoup(html,parser = "html.parser")

  try:
    human_check_botton = \
    driver.find_element(By.XPATH, "//*[@class='Button-sc-1dqy6lx-0 iljZso CloseButton-sc-abn00m-0 hripiO']")
    time.sleep(1)
    human_check_botton.click()
  except :
    pass
  time.sleep(5)
  driver.get_screenshot_as_file("final2.png")
  # u_field = driver.find_element(By.ID, "login-username")  # 替換為實際用戶名字段名稱
  # p_field = driver.find_element(By.ID, "login-password")  # 替換為實際密碼字段名稱
  # p_field.send_keys(password)
  # login_button = driver.find_element(By.ID, "login-button")
  # login_button.click()
  # time.sleep(1)
  # driver.get_screenshot_as_file("final3.png")

  driver.quit()
import requests
from bs4 import BeautifulSoup
spotify_bs4.prettify()
spotify_bs4.find_all("button")

# test-crawl.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

# 設置 Chrome 選項
chrome_options = Options()
chrome_options.add_argument("--headless")  # 運行無頭模式（不顯示瀏覽器界面）

# 獲取 Selenium Hub URL
selenium_url = os.getenv('SELENIUM_URL', 'http://localhost:4444/wd/hub')

# 創建 WebDriver 服務
service = Service(selenium_url)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 打開網站
    driver.get('http://example.com')

    # 打印頁面標題
    print("Page Title:", driver.title)

    # 查找元素示例
    element = driver.find_element(By.TAG_NAME, 'h1')
    print("Heading:", element.text)
    
    # 執行其他操作...
    
finally:
    # 關閉 WebDriver
    driver.quit()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # 無頭模式，無需顯示瀏覽器界面

service = Service('http://localhost:4444/wd/hub')
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('http://example.com')
print(driver.title)
driver.quit()
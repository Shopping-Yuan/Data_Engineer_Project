from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from datetime import date
import random

#Chrome browser env prepare
# 設置Chrome選項
options = Options()
profile_path = '/Library/Application Support/Google/Chrome/MyPorfile' #cookies path
options.add_argument(f'user-data-dir={profile_path}') #載入cookies

# 設置ChromeDriver服務
service = Service('/usr/local/chromedriver-mac-arm64/chromedriver')

# 初始化WebDriver
driver = webdriver.Chrome(service=service, options=options)
 

#透過修改url抓到資料=試抓一個月
years = [2021] #years for 2021-2024 and oen year trial
months = [1] # for one months try
days = list(range(32)[1:])
for year in years:
    for month in months:
        for day in days:
            #進入指定日期charts和抓取page sou
            chart_url = f"https://charts.spotify.com/charts/view/regional-tw-daily/{year}-{month:02d}-{day:02d}"
            driver.get(chart_url)
            page_source = driver.page_source
            
            # 生成 3 到 10 秒之間的隨機等待時間
            random_wait_time = random.uniform(5, 12)
            # 使用隨機等待時間創建 WebDriverWait 對象
            wait = WebDriverWait(driver, random_wait_time)
            tbody = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'tbody')))
            # 找到 tbody 下的所有 tr 元素
            rows = tbody.find_elements(By.TAG_NAME, 'tr')

            daily_data =[] 

            for row in rows:
                # 處理每一行的數據
                #print(row.text)  # 轉成文字印出
                daily_data.append(row.text)
    
            #driver.close()
            
            def split_for_one(data):
            #split for one
                daily_data_split = data.split("\n")
                return daily_data_split
        
            #remove index 1 and 4
            def remove_index(daily_data_split,rmindex = [1,4]):
                daily_data_clean = []
                for i, data in enumerate(daily_data_split):
                    if i not in rmindex:
                        daily_data_clean.append(data)
                return daily_data_clean

            def get_pk(data):
                #(統計資料)peak, previous rank, streak and streams
                Peak_Prev_Streak_Streams = data.split("\n")[4].split(" ")
                return Peak_Prev_Streak_Streams  

            daily_data_cleans = []
            for data in daily_data:
                daily_data_split = split_for_one(data)
                daily_data_clean = remove_index(daily_data_split)
                Peak_Prev_Streak_Streams = get_pk(data)
                daily_data_clean.extend(Peak_Prev_Streak_Streams)#加入切完的統計資料
                daily_data_cleans.append(daily_data_clean)


            
            # 獲取當前日期
            today = f"{year}-{month:02d}-{day:02d}"

            # 定義列名
            columns = ["date", "rank", "track_name", "artist_names", "peak_rank", "previous_rank", "days_on_chart", "streams"]

            # 創建 DataFrame
            df = pd.DataFrame(data=daily_data_cleans, columns=columns[1:])

            # 添加 date 列並將其移到第一列
            df.insert(0, "date", today)

            # 設置顯示選項
            pd.set_option('display.max_columns', None)  # 顯示所有列
            pd.set_option('display.width', None)  # 自動調整寬度
            pd.set_option('display.max_colwidth', None)  # 顯示完整的列內容

            # 顯示前幾行，使用更好的格式
            print(df.head().to_string(index=False))
            
            
            

            # file保存路徑
            file_path = f'/Users/niehjuihung/Documents/Programming learning/緯育/專題/Web scrabing_kkbox&spotify/Spotify/Daily_charts_tw/{year}-{month:02d}-{day:02d}_spotify_chart_tw.csv'

            # 將table存成csv
            df.to_csv(file_path, index=False, encoding='utf-8')
  
driver.close()
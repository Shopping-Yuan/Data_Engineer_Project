import sys
print(sys.path)
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidSessionIdException
from user import username, password
from bs4 import BeautifulSoup
from setting import driver_setting
from driver import get_driver

def connect_to_main(driver):
    driver.get("https://charts.spotify.com/home")
    time.sleep(5)
    driver.get_screenshot_as_file("first.png")

def to_log_in_field(driver):
    login_field = driver.find_element(By.XPATH, "//*[@class='ButtonInner-sc-14ud5tc-0 bRLmlP encore-bright-accent-set']")
    time.sleep(1)
    login_field.click()
    time.sleep(5)
    driver.get_screenshot_as_file("login_page.png")

def log_in(driver):
    wait = WebDriverWait(driver, 10)
    u_field = wait.until(EC.presence_of_element_located((By.ID, "login-username")))
    p_field = wait.until(EC.presence_of_element_located((By.ID, "login-password")))
    show_password = driver.find_element(By.XPATH, "//*[@class='Button-sc-1dqy6lx-0 bnvbjc']")
    time.sleep(1)
    show_password.click()
    time.sleep(3)
    u_field.send_keys(username)
    time.sleep(3)
    p_field.send_keys(password)
    login_button = driver.find_element(By.ID, "login-button")
    time.sleep(1)
    login_button.click()
    time.sleep(5)
    driver.get_screenshot_as_file("final.png")

def main():
    # 初始化 WebDriver
    driver = get_driver(**driver_setting)
    
    try:
        # 連接到主頁面
        connect_to_main(driver)
        
        # 進入登錄字段
        to_log_in_field(driver)
        
        # 執行登錄操作
        log_in(driver)
    finally:
        # 確保 WebDriver 會話被正確關閉
        try:
            driver.quit()
        except selenium.common.exceptions.InvalidSessionIdException:
            print("Session has already been terminated or invalid.")

if __name__ == "__main__":
    main()

# time.sleep(1)
# html = driver.page_source
# spotify_bs4 = BeautifulSoup(html,parser = "html.parser")

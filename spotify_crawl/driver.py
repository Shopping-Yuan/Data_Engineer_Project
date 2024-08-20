from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def get_driver(chrome_options_argument,grid_url):
    chrome_options = Options()
    for argument in chrome_options_argument:
        chrome_options.add_argument(argument)
    driver = webdriver.Remote(
        command_executor=grid_url,
        options=chrome_options
    )
    return driver
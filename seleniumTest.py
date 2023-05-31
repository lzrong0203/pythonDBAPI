from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

import time

inews_url = "https://mops.twse.com.tw/mops/web/t05st02"
realtime_news_url = "https://mops.twse.com.tw/mops/web/t05sr01_1"
service = Service(executable_path="/Users/lzrong/PycharmProjects/pythonDBAPI/geckodriver")


def get_realtime_news(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(realtime_news_url)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "hasBorder")))
    # for i in driver.find_elements(By.XPATH, "//input[@value='詳細資料']"):
    #     print(i)
    original_window = driver.current_window_handle
    for i, news in enumerate(driver.find_elements(By.XPATH, "//input[@value='詳細資料']")):
        news.click()
        wait.until(EC.presence_of_element_located((By.ID, "table01")))
        driver.switch_to.window(driver.window_handles[1])
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tblHead")))
        time.sleep(3)
        driver.find_element(By.TAG_NAME, "body").screenshot(f"news_{i}.png")
        print(f"news_{i}.png generate...")
        driver.close()
        driver.switch_to.window(original_window)
        if i > 10:
            break


# entire = driver.find_element_by_tag_name("body")
#         time.sleep(3)
#         entire.screenshot(f"{i}.png")
#         driver.close()
#         driver.switch_to.window(original_window)
#         if i > 2:
#             break


if __name__ == "__main__":
    options = Options()
    options.headless = True
    with webdriver.Firefox(service=service, options=options) as driver:
        get_realtime_news(driver)

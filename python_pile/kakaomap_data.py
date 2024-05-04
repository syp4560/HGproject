from selenium import webdriver as wb
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup as bs
import time
import requests

options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = wb.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("https://map.kakao.com/")

driver.find_element(By.CSS_SELECTOR, "div.inner_coach_layer").click()

search = driver.find_element(By.CSS_SELECTOR,"#search\.keyword\.query")
search.send_keys("도서관")
driver.find_element(By.CSS_SELECTOR,"#search\.keyword\.submit").click()


# soup = bs(driver.page_source, "lxml")
# a = soup.find("a", class_="moreview")
# href_url = a["href"]
# driver.get(href_url)

# driver.find_element(By.CSS_SELECTOR,"ul.placelist > li").click()
# driver.find_element(By.CSS_SELECTOR,"a.link_detail").click()






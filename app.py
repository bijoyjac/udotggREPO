from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

from lane_filter import select_lane

lanes = ["top", "jungle", "mid", "bot", "supp"]

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(3)

# Open page, accept cookies
driver.get("https://u.gg/lol/tier-list")
driver.switch_to.frame('sp_message_iframe_633208')
accept_cookies = driver.find_element_by_xpath('//*[@id="notice"]/div[5]/button[2]').click()
driver.maximize_window()


def parsing(driver, lane):
    select_lane(driver, lane)
    items = driver.find_elements_by_xpath('//*[@id="stats-tables-container-ID"]/div[6]/div/div/div/div[1]')
    for item in items:
        champ = item.text
        print(champ)


# for i in range(5)
for lane in lanes:
    parsing(driver, lane)
    print("\n")



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


def select_lane(driver, lane):
    if lane == "top":
        driver.find_element_by_xpath('//*[@id="stats-tables-container-ID"]/div[5]/div/div/div[3]/a[2]').click()
    elif lane == "jungle":
        driver.find_element_by_xpath('//*[@id="stats-tables-container-ID"]/div[5]/div/div/div[3]/a[3]').click()
    elif lane == "mid":
        driver.find_element_by_xpath('//*[@id="stats-tables-container-ID"]/div[5]/div/div/div[3]/a[4]').click()
    elif lane == "bot":
        driver.find_element_by_xpath('//*[@id="stats-tables-container-ID"]/div[5]/div/div/div[3]/a[5]').click()
    elif lane == "supp":
        driver.find_element_by_xpath('//*[@id="stats-tables-container-ID"]/div[5]/div/div/div[3]/a[6]').click()
    else:
        print("Pythagoras is awesome!")

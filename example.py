# python -m pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Chrome("E:\Python Project\python_selenium_sf\chromedriver")
driver.get("https://yandex.ru/")
sleep(5)
driver.find_element(By.XPATH, "//*[@id=\"0\"]/article/div[1]/div[1]/a").click()
sleep(5)
driver.save_screenshot('yandex_news1234.png')
driver.quit()

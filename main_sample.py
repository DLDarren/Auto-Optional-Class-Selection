from datetime import datetime
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Edge()

account = input("tap your account:")
password = input("tap your password:")

# you have to input Xpath
class_1 = '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[1]/table/tr[2]/td[2]/div[1]/label/span[1]'   # a sample
class_2 = '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[1]/table/tr[7]/td[5]/div[1]/label/span[1]'   # another sample
driver.get("https://czb.shphschool.com/static/qt/index.html#/main/index?code=1")
driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/form/div[1]/div/div/input').send_keys(account)
driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/form/div[2]/div/div/input').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/form/div[3]/div/button[1]').click()
tim = "2024-09-08 09:00"  # sample time
# timeout = 5

while True:
    if datetime.now().strftime("%Y-%m-%d %H:%M") == tim:
        element_present = EC.presence_of_element_located((By.ID, 'main'))
        # WebDriverWait(driver, timeout).until(element_present)
        driver.refresh()
        time.sleep(2)
        # two solutions are provided
        driver.find_element(By.XPATH, class_1).click()
        driver.find_element(By.XPATH, class_2).click()
        driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/button').click()
        sys.exit()

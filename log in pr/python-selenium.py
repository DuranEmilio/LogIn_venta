from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome(
    'C:/Chrome-webdrivers/chromedriver.exe')
driver.get("https://web.yimiglobal.com/")
username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class='email']")))
password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))
username.clear()
password.clear()
username.send_keys("durantelleze@gmail.com")
password.send_keys("1206Lilo")
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[name='login']"))).click()
time.sleep(5)


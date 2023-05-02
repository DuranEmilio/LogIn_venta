import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('C:/Chrome-webdrivers/chromedriver.exe')
driver.get("https://pos.yimiglobal.com/login")
Email = driver.find_element(By.ID, 'emailInputCheck')
Email.send_keys('yimiwings@gmail.com')

logButton = driver.find_element(By.ID, 'loginButton')
logButton.click()

password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "passWordLogin")))
password.send_keys('123456')

logbuttpasword = driver.find_element(By.ID, 'loginButton')
logbuttpasword.click()

pin = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="loginPinMain"]/div/div[3]/div[2]/div[4]/div[2]')))
for i in range(4):
    pin.click()

pedido = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="pedidosTab"]/aside/div[7]/div[2]/div')))

pedido = driver.find_element(By.ID, 'newOrderPedidos')
pedido.click()

order = driver.find_element(By.XPATH, '//*[@id="orderTypeOrders"]/div[2]')
order.click()

# categories = driver.find_element(By.ID, 'categorys-container')
b = driver.find_element(By.XPATH,'//*[@id="categorys-container"]/div[3]')
driver.execute_script("arguments[0].click();", b)
time.sleep(5)

pay = driver.find_element(By.ID, 'btnPayOrder')
pay.click()

paylast = WebDriverWait(driver,10).until(
EC.element_to_be_clickable((By.ID, 'btnPagar')))
paylast.click()
time.sleep(5)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    'C:/Chrome-webdrivers/chromedriver.exe')
driver.get("https://www.yimi.com.mx/negocio")

CreateAccount = driver.find_element(
    By.XPATH, '/html/body/section[3]/div/div/div[1]/div/a[1]')
CreateAccount.click()

Email = driver.find_element(By.ID, 'emailInputCheck')
Email.send_keys("mabeltellez@gmail.com")

continua = driver.find_elements(
    By.XPATH, '/html/body/div[2]/div/section[1]/div/div[2]/div[3]')
continua[0].click()
time.sleep(2)

name = driver.find_element(By.ID, 'nombreForm')
name.send_keys("prueba")

negocio = driver.find_element(By.ID, 'nombreNegocioForm')
negocio.send_keys("NegocioPrueba")

cel = driver.find_element(By.ID, 'telForm')
cel.send_keys("1234567890")

password = driver.find_element(By.ID, 'passwordForm')
password.send_keys("123456")

CreateAccountButton = driver.find_element(By.ID, 'vl')
CreateAccountButton.click()
time.sleep(3)

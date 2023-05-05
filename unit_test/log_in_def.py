import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_create_account():
    CreateAccount = driver.find_element(By.XPATH, '/html/body/section[3]/div/div/div[1]/div/a[1]')
    CreateAccount.click()

def fill_email():
    Email = driver.find_element(By.ID, 'emailInputCheck')
    Email.send_keys("durantelleze+2@gmail.com")

def click_next():
    continua = driver.find_elements(By.XPATH, '/html/body/div[2]/div/section[1]/div/div[2]/div[3]')
    continua[0].click()
    time.sleep(2)

def fill_form():
    name = driver.find_element(By.ID, 'nombreForm')
    name.send_keys("prueba")

    negocio = driver.find_element(By.ID, 'nombreNegocioForm')
    negocio.send_keys("NegocioPrueba")

    cel = driver.find_element(By.ID, 'telForm')
    cel.send_keys("1234567890")

    password = driver.find_element(By.ID, 'passwordForm')
    password.send_keys("123456")

def click_create_account_button():
    CreateAccountButton = driver.find_element(By.ID, 'vl')
    CreateAccountButton.click()
    time.sleep(3)

if __name__ == '__main__':
    driver = webdriver.Chrome('C:/Chrome-webdrivers/chromedriver.exe')
    driver.get("https://www.yimi.com.mx/negocio")

    click_create_account()
    fill_email()
    click_next()
    fill_form()
    click_create_account_button()

    driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time

def in_account(login, password, link):
    try:
        driver = webdriver.Chrome()
        driver.get(link)

        login_input = driver.find_element(By.ID, "userName")
        password_input = driver.find_element(By.ID, "password")

        login_input.send_keys(login)
        password_input.send_keys(password)

        login_buttom = driver.find_element(By.ID, "login")
        
        try:
            login_buttom.click()
        except ElementClickInterceptedException:
            try:
                driver.execute_script("arguments[0].scrollIntoView(true);", 
                                      login_buttom)
                time.sleep(1)
                login_buttom.click()
            except ElementClickInterceptedException:
                driver.execute_script("arguments[0].click()", 
                                      login_buttom)
        
        time.sleep(3)
        return driver
            
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return driver

    
link = input("Введите ссылку на сайт: ")
login = input("Введите логин: ")
password = input("Введите пароль: ")

driver = in_account(login, password, link)

if driver:
    input()
    driver.quit()
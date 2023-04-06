import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"
browser.get(link)


try: 
    
    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text

    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text

    r = str(int(x)+int(y))
    
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(r) 


    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)


finally:

    time.sleep(10)

    browser.quit()
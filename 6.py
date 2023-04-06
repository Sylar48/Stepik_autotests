import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/registration1.html'


def main():
    with webdriver.Chrome() as browser:
        browser.get(link)

        first_name_field = browser.find_element(By.XPATH, '//input[@required and @class="form-control first"]')
        first_name_field.send_keys('Ivan')

        last_name_field = browser.find_element(By.XPATH, '//input[@required and @class="form-control second"]')
        last_name_field.send_keys('Ivanov')

        email_address_field = browser.find_element(By.XPATH, '//input[@required and @class="form-control third"]')
        email_address_field.send_keys('ivan.ivanov@example.org')

        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')

        assert 'Congratulations! You have successfully registered!' == welcome_text_elt.text


if __name__ == '__main__':
    main()
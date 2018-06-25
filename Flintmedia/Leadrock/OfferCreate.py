import unittest
from time import sleep
from random import choice
from selenium import webdriver
from string import ascii_uppercase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class OfferCreate(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\drivers\\chromedriver.exe")
        self.driver.maximize_window()

    def test_open_leadrock(self):
        driver = self.driver
        driver.get("http://test.leadrock.com")
        driver.find_element_by_link_text('Login').click()
        driver.find_element_by_id('LoginForm_username').send_keys(input("Введите email: "))
        driver.find_element_by_id('LoginForm_password').send_keys(input("Введите пароль: "), Keys.ENTER)
        sleep(3)
        try:
            driver.find_element_by_xpath("//*[contains(text(), 'Error!')]")
        except Exception:
            print('OK')
        else:
            print('Incorrect E-mail or password! Test stop')
            self.driver.close()
        driver.get("http://test.leadrock.com/administrator/offer/offer/create")
        assert "No results found." not in driver.page_source
        random_offer_name = random_word(5) + '_TEST'
        driver.find_element_by_id('Offer_name').send_keys(random_offer_name)
        Select(driver.find_element_by_id('Offer_sale_manager_id')).select_by_value("5")
        Select(driver.find_element_by_id('Offer_manager_id')).select_by_value("4")
        Select(driver.find_element_by_id('Offer_allowed_sources')).select_by_value("1")
        driver.find_element_by_id('Offer_is_multiple_leads').is_selected()
        driver.find_element_by_id('Offer_is_full_private').is_selected()
        driver.find_element_by_id('Offer_description').send_keys(random_word(40))
        driver.find_element_by_css_selector('button.btn').click()
        time.sleep(3)
        driver.get('http://test.leadrock.com/administrator/offer/offer/list')
        driver.find_element_by_xpath('//*[@id="yw0"]/div[1]/div[1]/div/span').click()
        driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(random_offer_name, Keys.ENTER)
        driver.find_element_by_css_selector('button.btn').click()
        sleep(10)
        offer_name = driver.find_element_by_xpath('//*[@id="yw1"]/table/tbody/tr/td[4]/a').text
        if offer_name == random_offer_name:
            print('Offer created successfully')
        else:
            print('Error. Creating failed')
        driver.quit()

def random_word(m):
    return ''.join(choice(ascii_uppercase) for i in range(m))

if __name__ == "__main__":
    unittest.main()

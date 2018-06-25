import unittest
import configparser
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class LoginEmailPandao(unittest.TestCase):

    #Driver setup
    def setUp(self):
        key = config('Remote', 'url')
        self.driver = webdriver.Remote(
            command_executor=key,
            desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.maximize_window()

    #Login
    def test_login(self):
        driver = self.driver
        byxpath = driver.find_element_by_xpath
        byid = driver.find_element_by_id
        key = config('Url', 'main')
        driver.get(key)
        byxpath('/html/body/header/div/div[2]/div/a[2]').click()
        sleep(3)
        key = config('LOGIN', 'email')
        byid('login_form_email').send_keys(key)
        key = config('LOGIN', 'password')
        byid('login_form_password').send_keys(key)
        sleep(3)
        byid('login_form_button').click()
        sleep(3)
        check = byxpath('/html/body/header/div/div[2]/div/div[1]/span[2]').text
        print('Hello ' + str(check))
        if 'Ниндзя' in check:
            print('Login OK')
        else:
            print('Login ERROR!!')
            driver.quit()

#Config data
def config(section, title):
    config = configparser.ConfigParser()
    config.read('..//settings.ini')
    config.sections()
    key = config[section][title]
    return key

if __name__ == "__main__":
    unittest.main()
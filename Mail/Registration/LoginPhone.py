import RegistrationPhone
import unittest
import configparser
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class LoginPandao(unittest.TestCase):

    #Driver setup
    def setUp(self):
        url = config('Remote', 'url')
        self.driver = webdriver.Remote(
            command_executor = url,
            desired_capabilities = DesiredCapabilities.CHROME)
        self.driver.maximize_window()

    #Registration + logout + login
    def test_login(self):
        phone_number, code = RegistrationPhone.RegistrationPandao.test_registration(self)
        driver = self.driver
        byxpath = driver.find_element_by_xpath
        byid = driver.find_element_by_id
        byxpath('/html/body/header/div[2]/div[3]/div/div[1]').click()
        byxpath('/html/body/header/div[2]/div[3]/div/div[1]/nav/ul/li[5]/a').click()
        byxpath('/html/body/header/div/div[2]/div/a[2]').click()
        sleep(2)
        byid('login_by_phone').click()
        byid('login_phone_form_phone').send_keys(phone_number)
        byid('login_phone_form_button').click()
        sleep(2)
        byid('sms_form_code').send_keys(code)
        byid('sms_form_button').click()
        print('Login OK')
        driver.close()

#Config data
def config(section, title):
    config = configparser.ConfigParser()
    config.read('..//settings.ini')
    config.sections()
    url = config[section][title]
    return url

if __name__ == "__main__":
    unittest.main()
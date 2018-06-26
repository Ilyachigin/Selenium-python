import unittest
from time import sleep
from selenium import webdriver
from random import choice
from random import randint
from string import ascii_uppercase
import configparser
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class leadrock(unittest.TestCase):

    #Driver setup
    def setUp(self):
        key = config('Remote', 'url')
        self.driver = webdriver.Remote(
            command_executor=key,
            desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.maximize_window()

    #Form filling
    def test_rock(self):
        driver = self.driver
        count = 1
        for x in range(1,101):
            print('Lead №'+count)
            driver.get(config('Remote', 'url'))
            driver.find_element_by_id('name').send_keys(str('TEST#'+ str(x) +'_'+random_word(6)+random_number(4)))
            driver.find_element_by_id('phone').send_keys(str(random_number(12)))
            driver.find_element_by_id('sendLeadButton').click()
            sleep(2)
            count = count+1
            driver.delete_all_cookies()

    #Steps after test
    def tearDown(self):
        sleep(2)
        self.driver.close()

#Random data
def random_number(n):
    start = 10**(n-1)
    end = (10**n)-1
    return randint(start, end)
def random_word(m):
    return ''.join(choice(ascii_uppercase) for i in range(m))

#Config data
def config(section, title):
    config = configparser.ConfigParser()
    config.read('settings.ini')
    config.sections()
    key = config[section][title]
    return key

if __name__ == "__main__":
    unittest.main()
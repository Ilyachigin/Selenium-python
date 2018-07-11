import unittest
import configparser
from time import sleep
from random import choice
from random import randint
from selenium import webdriver
from string import ascii_uppercase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class IntegrationLeadrock(unittest.TestCase):

    #Driver setup
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.maximize_window()

    def test_integration(self):
        driver = self.driver
        byxpath = driver.find_element_by_xpath
        byid = driver.find_element_by_id
        byname = driver.find_element_by_name
        driver.get(config('Site', 'url2'))
        login(driver, config('Login', 'email2'), config('Login', 'password2'))
        driver.get(config('Site', 'url2') + '/webmaster/offer/offer/view/id/8')
    #Url parsing
        simple = byxpath('//*[@id="subscribe-list"]/table/tbody/tr[1]/td[2]').text
        straight = byxpath('//*[@id="subscribe-list"]/table/tbody/tr[2]/td[2]').text
        prelend = byxpath('//*[@id="subscribe-list"]/table/tbody/tr[5]/td[2]').text
        prelend_straight = byxpath('//*[@id="subscribe-list"]/table/tbody/tr[7]/td[2]').text
        if "Обычная новая" in simple and "Прямая новая" in straight and "Преленд новый" in prelend and "Преленд новый прямой" in prelend_straight:
            simple_url = byxpath('//*[@id="subscribe-list"]/table/tbody/tr[1]/td[5]/span').text
            straight_url = byxpath('//*[@id="subscribe-list"]/table/tbody/tr[2]/td[5]/span').text
            prelend_url = byxpath('//*[@id="subscribe-list"]/table/tbody/tr[5]/td[5]/span').text
            prelend_straight_url = byxpath('//*[@id="subscribe-list"]/table/tbody/tr[7]/td[5]/span').text
    #Relogin to administrator
        driver.get(config('Site', 'url2') + '/user/authorization/logout')
        login(driver, config('Login', 'email'), config('Login', 'password'))
    #Straight land  + checking lead availability
        print('Simple landing test')
        driver.get(straight_url)
        name = 'TEST_' + random_word(6)
        byname('name').send_keys(name)
        byname('address').send_keys('TEST_' + random_word(10))
        byname('city').send_keys('TEST_' + random_word(5))
        byname('pcode').send_keys(str(random_number(5)))
        byname('phone').send_keys(str(random_number(11)))
        sleep(2)
        byid('submit-button').click()
    #Straight checking
        confirm = driver.current_url
        if "confirm" in str(confirm):
            print('  ...OK!')
            sleep(3)
            driver.get(config('Site', 'url2') + '/administrator/lead')
            name_check = byxpath('//*[@id="lead-list"]/table/tbody/tr[1]/td[3]').text
            if str(name) in str(name_check):
                print('Straight lead integration OK!')
                driver.delete_all_cookies()
            else:
                print('NO LEAD!!')
                driver.quit()
        else:
            print('Confirm page ERROR!!')
            driver.quit()

    #Steps after test
    def tearDown(self):
        sleep(5)
        self.driver.close()

#Random data
def random_number(n):
    start = 10**(n-1)
    end = (10**n)-1
    return randint(start, end)
def random_word(m):
    return ''.join(choice(ascii_uppercase) for i in range(m))

#Common login
def login(driver, email, password):
    try:
        driver.find_element_by_link_text('Login').click()
    except Exception:
        driver.find_element_by_link_text('Войти').click()
    sleep(2)
    driver.find_element_by_id('LoginForm_username').send_keys(email)
    driver.find_element_by_id('LoginForm_password').send_keys(password, Keys.ENTER)
    sleep(3)

#Config data
def config(section, title):
    config = configparser.ConfigParser()
    config.read('../../../settings.ini')
    config.sections()
    key = config[section][title]
    return key

if __name__ == "__main__":
    unittest.main()
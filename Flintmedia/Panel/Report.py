import unittest
import configparser
from time import sleep
from random import choice
from random import randint
from selenium import webdriver
from string import ascii_uppercase
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class PanelFlintmedia(unittest.TestCase):

    #Driver setup
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor=config('Remote', 'url'),
            desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.maximize_window()

    #Login
    def test_login(self):
        driver = self.driver
        byxpath = driver.find_element_by_xpath
        byid = driver.find_element_by_id
        driver.get(config('Site', 'url')+'/user/sign-in/login')
        sleep(1)
        byid('loginform-identity').send_keys(config('Login', 'email'))
        byid('loginform-password').send_keys(config('Login', 'password'))
        driver.find_element_by_name('login-button').click()
        sleep(2)
    #New report
        driver.get(config('Site', 'url')+'/arbitration/report/create')
        Select(byid('report-isuseprevious')).select_by_value('0')
        byxpath("//*[contains(text(), 'Сохранить')]").click()
        sleep(2)
        Select(byid('reportline-0-subsource_id')).select_by_value('1')
        Select(byid('reportline-0-offer_advertiser_id')).select_by_value('13')
        sleep(2)
        Select(driver.find_element_by_name('ReportLine[0][geo_country_id]')).select_by_value('108')
        price = str(random_number(2))
        price2 = str(random_number(2))
        byid('reportline-0-money_spent_amount').send_keys(price)
        byid('reportline-0-money_income_amount').send_keys(price2)
        Select(driver.find_element_by_id('reportline-0-money_spent_currency_id')).select_by_value('2')
        Select(driver.find_element_by_id('reportline-0-money_income_currency_id')).select_by_value('2')
        byid('reportline-0-cpa_comment').send_keys(random_word(10))
        sleep(1)
        byxpath("//*[contains(text(), 'Сохранить')]").click()
        sleep(2)
    #Checking report presence
        driver.get(config('Site', 'url') + '/arbitration/report?ReportSearch%5Buser_id%5D=3&my=true')
        x = 1
        check_report = byxpath('//*[@id="w0"]/table/tbody/tr[1]/td[4]').text
        check_report2 = byxpath('//*[@id="w0"]/table/tbody/tr[1]/td[6]').text
        while price not in check_report and price2 not in check_report2:
            check = '//*[@id="w0"]/table/tbody/tr[' + str(x) + ']/td[4]'
            check2 = '//*[@id="w0"]/table/tbody/tr[' + str(x) + ']/td[6]'
            print(check + ' + ' + check2)
            check_report = byxpath(check).text
            check_report2 = byxpath(check2).text
            print(check_report + ' + ' + check_report2)
            x = x + 1

    #Steps after test
    def tearDown(self):
        sleep(12)
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
    config.read('..//settings.ini')
    config.sections()
    key = config[section][title]
    return key

if __name__ == "__main__":
    unittest.main()
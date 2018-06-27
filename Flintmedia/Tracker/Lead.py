import re
import unittest
import configparser
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class LeadTracker(unittest.TestCase):

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
        driver.get(config('Site', 'url')+'/user/authorization/login')
        sleep(1)
        byid('LoginForm_username').send_keys(config('Login', 'email'))
        byid('LoginForm_password').send_keys(config('Login', 'password'))
        byxpath('//*[@id="login-form"]/div[1]/div/div[2]/button').click()
        sleep(2)
    #New clickid
        driver.get(config('Site', 'url')+'/arbitration/campaign/update/id/31')
        traffic = byxpath('//*[@id="urls"]/div[1]/div/span').text
        driver.get(traffic)
        clickid_url = driver.current_url
        match = re.search('(\d+)', str(clickid_url))
        clickid = match.group(0)
        print('Clickid: ' + clickid)
    #Checking statistics
        driver.get(config('Site', 'url') + '/arbitration/statistics')
        statistics_leads = byxpath('//*[@id="yw1"]/table/tfoot/tr/td[4]').text
    #New lead
        driver.get(config('Site', 'url') + '/postback?u=268b785d88&id='+clickid)
        error = byxpath('/html/body').text
        if 'false' in error:
            print('Lead was created')
        else:
            print('Lead ERROR!')
            exit()
    #Checking statistics with new lead
        driver.get(config('Site', 'url') + '/arbitration/statistics')
        leads = byxpath('//*[@id="yw1"]/table/tfoot/tr/td[4]').text
        check_lead = int(statistics_leads) + 1
        if str(check_lead) == str(leads):
            print('Test PASSED!')
        else:
            print('Test ERROR!')
            exit()

    #Steps after test
    def tearDown(self):
        sleep(12)
        self.driver.close()

#Config data
def config(section, title):
    config = configparser.ConfigParser()
    config.read('../../settings.ini')
    config.sections()
    key = config[section][title]
    return key

if __name__ == "__main__":
    unittest.main()
import unittest
import configparser
from time import sleep
from selenium import webdriver
from uitest.Registration import RegistrationPhone
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class ProfilePandao(unittest.TestCase):

    #Driver setup
    def setUp(self):
        key = config('Remote', 'url')
        self.driver = webdriver.Remote(
            command_executor=key,
            desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.maximize_window()
        RegistrationPhone.RegistrationPandao.test_registration(self)

    def test_promocode(self):
        driver = self.driver
        byxpath = driver.find_element_by_xpath
        byid = driver.find_element_by_id
        sleep(4)
    #Promocode input
        driver.find_element_by_css_selector('body > div.page.personal-page.personal-main > div.content-page.content-page-personal > div > div.wrapper-personal-header > ul > li.promo-ico > a').click()
        byid('promocode_input').send_keys('selenium')
        byid('promocode_button').click()
        byxpath('//*[@id="modal_promocode"]/div/div[1]').click()
    #Promocode history checking
        driver.get(config('Url', 'main') + 'profile/points_history')
        history = byxpath('//*[@id="points-wrapper"]/div[1]/div/div[2]/div[1]').text
        if '10 баллов по промокоду selenium' in history:
            print('Test PASSED!')
        else:
            print('Test FAILED!')
            driver.quit()

    #Steps after test
    def tearDown(self):
        sleep(2)
        self.driver.close()

#Config data
def config(section, title):
    config = configparser.ConfigParser()
    config.read('..//settings.ini')
    config.sections()
    key = config[section][title]
    return key

if __name__ == "__main__":
    unittest.main()
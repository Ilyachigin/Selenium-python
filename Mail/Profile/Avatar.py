import sys
import unittest
import configparser
from time import sleep
from selenium import webdriver
from uitest.Registration import LoginEmail
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class AvatarPandao(unittest.TestCase):

    #Driver setup
    def setUp(self):
        key = config('Remote', 'url')
        self.driver = webdriver.Remote(
            command_executor=key,
            desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.maximize_window()
        LoginEmail.LoginEmailPandao.test_login(self)

    #Avatar deleting + adding
    def test_avatar(self):
        driver = self.driver
        byid = driver.find_element_by_id
        driver.get(config('Url', 'main') + 'profile/settings')
        try:
            byid('button_delete').click()
            sleep(2)
            byid("avatar_upload").send_keys(sys.path[0] + '/uitest/Profile/123.png')
            print('Test PASSED!')
        except Exception:
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
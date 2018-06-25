import sys
sys.path.append("../../apitest//sms")
import requests
import unittest
import getNumber
import configparser
from random import choice
from string import ascii_uppercase
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class RegistrationPandao(unittest.TestCase):

    #Driver setup
    def setUp(self):
        url = config('Remote', 'url')
        self.driver = webdriver.Remote(
            command_executor = url,
            desired_capabilities = DesiredCapabilities.CHROME)
        self.driver.maximize_window()

    #Registration steps + code from sms request
    def test_registration(self):
        url = config('Url', 'main')
        driver = self.driver
        driver.get(url)
        driver.find_element_by_xpath('/html/body/header/div/div[2]/div/a[1]').click()
        sleep(5)
        lastName = random_word(6) + '_TEST'
        driver.find_element_by_name('reg_form[firstName]').send_keys(random_word(5))
        driver.find_element_by_id('reg_form_lastName').send_keys(lastName)
        phone_number, activation_id = getNumber.NumberPandao().test_number()
        driver.find_element_by_id('reg_form_phone').send_keys(phone_number)
        driver.find_element_by_id('reg_form_button').click()
        code = codeFromSms(activation_id)
        while str(code) == 'STATUS_WAIT_CODE':
            print('No code. Wait 15s\n')
            sleep(15)
            code = codeFromSms(activation_id)
        else:
            print('Code from sms: ' + str(code))
        driver.find_element_by_id('sms_form_code').send_keys(code)
        driver.find_element_by_id('sms_form_button').click()
        sleep(3)
        new_url = url + 'profile/'
        driver.get(new_url)
        currentUrl = driver.current_url
        if new_url == currentUrl:
            print('Registration OK')
        else:
            print('Registration ERROR!')
        return phone_number, code
        sleep(10)

#Config data
def config(section, title):
    config = configparser.ConfigParser()
    config.read('..//settings.ini')
    config.sections()
    url = config[section][title]
    return url

#Get request + code parsing
def codeFromSms(activationid):
    url = config('SMS', 'url') + '?api_key=' + config('SMS', 'key') + '&action=getStatus&id=' + activationid
    print('\n---Get status---' + '\nURL: ' + url)
    headers = {'Content-type': 'text/xml',
                'Accept': 'text/plain',
                'Content-Encoding': 'utf-8'}
    answer = requests.get(url, headers, verify=False)
    code = str(answer.text)
    try:
        code = code.split(":")[1]
        print(str(answer) + '\n' + code)
    except IndexError:
        print(str(answer) + '\n' + str(code))
    return code

#Random data
def random_word(m):
    return ''.join(choice(ascii_uppercase) for i in range(m))

if __name__ == "__main__":
    unittest.main()
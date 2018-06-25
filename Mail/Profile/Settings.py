import unittest
import configparser
from time import sleep
from selenium import webdriver
from uitest.Registration import RegistrationPhone
from random import choice
from random import randint
from string import ascii_uppercase
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class settingsPandao(unittest.TestCase):

    #Driver setup
    def setUp(self):
        key = config('Remote', 'url')
        self.driver = webdriver.Remote(
            command_executor=key,
            desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.maximize_window()
        RegistrationPhone.RegistrationPandao.test_registration(self)

    def test_settings(self):
        driver = self.driver
        byxpath = driver.find_element_by_xpath
        byid = driver.find_element_by_id
        driver.get(config('Url', 'main') + 'profile/settings')
    #Contact data
        firstname,lastname,email,fathername,country,city,region,street,house,housing,structure,flat,index = value()
        byid('form_lastName').clear()
        byid('form_lastName').send_keys(lastname)
        byid('form_firstName').clear()
        byid('form_firstName').send_keys(firstname)
        byid('form_email').clear()
        byid('form_email').send_keys(email)
        byid('edit-profile-btn').click()
        sleep(3)
        driver.get(driver.current_url)
        namecheck = byxpath('/html/body/div[1]/div[4]/div/div[1]/div[1]/div/div[2]/p').text
        fullname = firstname + ' ' + lastname
        if namecheck == fullname:
            print('Contact changing OK!')
        else:
            print('Contact changing ERROR')
            driver.quit()
    #Delivery address
        byxpath("//*[contains(text(), 'Добавить адрес')]").click()
        firstname,lastname,email,fathername,country,city,region,street,house,housing,structure,flat,index = value()
        byid('form_lastName').clear()
        byid('form_firstName').clear()
        byid('form_fathersName').clear()
        byid('form_email').clear()
        byid('form_phone').clear()
        byid('form_lastName').send_keys(lastname)
        byid('form_firstName').send_keys(firstname)
        byid('form_fathersName').send_keys(fathername)
        byid('form_email').send_keys(email)
        byid('form_phone').send_keys('+7'+str(random_number(10)))
        byid('form_country').send_keys(country)
        byid('form_city').send_keys(city)
        byid('form_region').send_keys(region)
        byid('form_street').send_keys(street)
        byid('form_houseNumber').send_keys(house)
        byid('form_housing').send_keys(housing)
        byid('form_structure').send_keys(structure)
        byid('form_flat').send_keys(flat)
        sleep(3)
        byid('form_index').clear()
        byid('form_index').send_keys(index)
        byxpath("//*[contains(text(), 'Сохранить')]").click()
        namecheck = byxpath('/html/body/div[1]/div[4]/div/div[2]/div[3]/p[1]').text
        addresscheck = byxpath('/html/body/div[1]/div[4]/div/div[2]/div[3]/p[2]').text
        fullname = lastname + ' '+ firstname + ' ' + fathername
        if str(index) in str(addresscheck) and str(namecheck) == str(fullname):
            print('Delivery address adding is OK!\n'+'Test PASSED')
        else:
            print('Delivery address adding ERROR!\n'+'Test FAILED')
            driver.quit()

    #Steps after test
    def tearDown(self):
        sleep(2)
        self.driver.close()

#Common data
def value():
    firstname = random_word(5)
    lastname = random_word(6)
    email = random_word(5) + '@mail.ru'
    fathername = random_word(5)
    country = random_word(6)
    city = random_word(5)
    region = random_word(6)
    street = random_word(7)
    house = random_number(2)
    housing = random_number(1)
    structure = random_number(1)
    flat = random_number(3)
    index = random_number(6)
    return firstname,lastname,email,fathername,country,city,region,street,house,housing,structure,flat,index

#Config data
def config(section, title):
    config = configparser.ConfigParser()
    config.read('..//settings.ini')
    config.sections()
    key = config[section][title]
    return key

#Random data
def random_number(n):
    start = 10**(n-1)
    end = (10**n)-1
    return randint(start, end)
def random_word(m):
    return ''.join(choice(ascii_uppercase) for i in range(m))

if __name__ == "__main__":
    unittest.main()
import unittest
import configparser
from time import sleep
from random import choice
from random import randint
from string import ascii_uppercase
from selenium import webdriver
from uitest.Registration import LoginEmail
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class OrderPandao(unittest.TestCase):

    #Driver setup
    def setUp(self):
        key = config('Remote', 'url')
        self.driver = webdriver.Remote(
            command_executor = key,
            desired_capabilities = DesiredCapabilities.CHROME)
        self.driver.maximize_window()
        LoginEmail.LoginEmailPandao.test_login(self)

    def test_order(self):
        driver = self.driver
        byxpath = driver.find_element_by_xpath
        byid = driver.find_element_by_id
    #Adding random product to cart
        byxpath('/html/body/header/div/div[2]/div/div[2]/a[2]').click()
        byxpath('//*[@id="menu-wrap"]/div/nav/ul/li[1]/a').click()
        category = '/html/body/div[1]/div[1]/ul/li['+str(randint(1,3))+']/ul/li['+str(randint(1,3))+']/a'
        byxpath(category).click()
        product = '//*[@id="product-wrapper"]/a['+str(randint(1,10))+']/div[1]/img'
        byxpath(product).click()
        driver.find_element_by_css_selector('#add-to-cart').click()
        #try:
        #    byxpath('//*[@id="add-to-cart"]').click()
        #except Exception:
         #   byxpath('//*[@id="buy-now"]').click()
        sleep(2)
    #Creating an order
        byxpath('/html/body/header/div/div[2]/div/div[2]/a[2]').click()
        byxpath("//*[contains(text(), 'Оформить заказ')]").click()
    #Adding delivery address
        byxpath("//*[contains(text(), 'Добавить адрес')]").click()
        byid('form_lastName').send_keys(random_word(6))
        byid('form_firstName').send_keys(random_word(5))
        byid('form_fathersName').send_keys(random_word(7))
        byid('form_email').clear()
        byid('form_email').send_keys(random_word(5)+'@mail.ru')
        byid('form_phone').clear()
        byid('form_phone').send_keys('+7'+str(random_number(10)))
        sleep(2)
        byid('go-last').click()
        byid('form_city').send_keys('Санкт-Петербург')
        byid('form_region').send_keys('Санкт-Петербург')
        byid('form_street').send_keys('улица Ленина')
        byid('form_houseNumber').send_keys(random_number(2))
        byid('form_housing').send_keys(random_number(1))
        byid('form_flat').send_keys(random_number(3))
        sleep(2)
        byid('form_structure').send_keys(random_number(1))
        byid('form_submit').click()
    #Payment
        sleep(2)
        byxpath("//*[contains(text(), 'оплатить')]").click()
        print('Payment in process...')
        sleep(8)
        driver.get(config('Url', 'main')+'profile/orders')
    #Checking and cancel order
        byxpath('//*[@id="orders-wrapper"]/div').click()
        status = driver.find_element_by_css_selector('body > div.page.personal-page.order_page > div:nth-child(4) > div > div.personal-content > div > div.right-block > div > div:nth-child(3) > p:nth-child(2)').text
        if 'Собирается' in status:
            sleep(3)
            byxpath("//*[@class='btn grey-btn mgr10']").click()
            driver.find_element_by_css_selector('body > div.page.personal-page.my-orders-page > div:nth-child(4) > div > div > div > div.dec-buttons > a:nth-child(2)').click()
        else:
            driver.quit()
        decline = driver.find_element_by_css_selector('body > div.page.personal-page.my-orders-page > div:nth-child(4) > div > div > div > div.title-data-merchant').text
        if 'Ваш заказ успешно отменен' in decline:
            sleep(4)
            byxpath("//*[contains(text(), 'Вернуться в мои заказы')]").click()
        else:
            driver.quit()()
        order_check = byxpath('//*[@id="orders-wrapper"]/div/p[1]').text
        if 'нет заказов' in order_check:
            print('Test PASSED!')
        else:
            print('Test FAILED!')

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

#Random
def random_number(n):
    start = 10**(n-1)
    end = (10**n)-1
    return randint(start, end)
def random_word(m):
    return ''.join(choice(ascii_uppercase) for i in range(m))

if __name__ == "__main__":
    unittest.main()
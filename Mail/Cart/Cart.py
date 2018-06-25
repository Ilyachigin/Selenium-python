import unittest
import configparser
from time import sleep
from random import randint
from selenium import webdriver
from uitest.Registration import LoginEmail
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class CartPandao(unittest.TestCase):

    #Driver setup
    def setUp(self):
        key = config('Remote', 'url')
        self.driver = webdriver.Remote(
            command_executor = key,
            desired_capabilities = DesiredCapabilities.CHROME)
        self.driver.maximize_window()
        LoginEmail.LoginEmailPandao.test_login(self)

    #Checking empty cart
    def test_cart(self):
        driver = self.driver
        byxpath = driver.find_element_by_xpath
        sleep(2)
        byxpath('/html/body/header/div/div[2]/div/div[2]/a[2]').click()
        cart = byxpath('/html/body/div[1]/div[2]/div[2]/h2').text
        if cart == 'Корзина пуста':
            print('1) Cart is empty = OK')
        else:
            print('Cart is not empty! STOP TEST!')
            driver.quit()
    #Cart updating + compliance checking
        byxpath('//*[@id="menu-wrap"]/div/nav/ul/li[1]/a').click()
        category = '/html/body/div[1]/div[1]/ul/li['+str(randint(1,3))+']/ul/li['+str(randint(1,3))+']/a'
        byxpath(category).click()
        product = '//*[@id="product-wrapper"]/a['+str(randint(1,20))+']/div[1]/img'
        byxpath(product).click()
        productname = byxpath('//*[@id="mm-0"]/div[1]/div[3]/div/div[2]/div[1]/div/h1').text
        try:
            price = byxpath('//*[@id="mm-0"]/div[1]/div[3]/div/div[2]/div[1]/div/div[2]/div/p').text
        except Exception:
            price = byxpath('//*[@id="mm-0"]/div[1]/div[3]/div/div[2]/div[1]/div/div[3]/div/p[2]').text
        shop = byxpath('//*[@id="mm-0"]/div[1]/div[3]/div/div[2]/div[2]/div/div/div/div/a').text
        try:
            byxpath('//*[@id="add-to-cart"]').click()
        except Exception:
            byxpath('//*[@id="buy-now"]').click()
        sleep(2)
        byxpath('/html/body/header/div/div[2]/div/div[2]/a[2]').click()
        shop_check = byxpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]').text
        productname_check = byxpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/p').text
        price_check = byxpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div/span').text
        if shop_check in shop and productname_check in productname and price_check in price:
            print('2) Cart if full = OK')
        else:
            print('Cart ERROR!')
    #Cart deleting
        byxpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/a').click()
        cart = byxpath('/html/body/div[1]/div[2]/div[2]/h2').text
        if cart == 'Корзина пуста':
            print('3) Cart is empty = OK. \n Test PASSED')
        else:
            print('Cart is not empty! STOP FAILED!')

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
from selenium import webdriver
from time import sleep
import unittest
from random import randint
from random import choice
from string import ascii_uppercase
from selenium.webdriver.common.keys import Keys

class Registration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\drivers\\chromedriver.exe")
        self.driver.maximize_window()
    #Temp mail
    def test_open_leadrock(self):
        driver = self.driver
        driver.get("https://www.mydlo.ru/")
        registration_email= driver.find_element_by_id("mbox-address")
        temp_email = registration_email.get_attribute("textContent")
        print("Temp email: " + temp_email)
        random_skype = random_word(6).upper()
        random_password = random_word(10)
        print('Random password: ' + random_password)
    #Landing registration
        driver.execute_script('''window.open("http://test.leadrock.com","_blank");''')
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_link_text('Sign up').click()
        driver.find_element_by_name("User[email]").send_keys(temp_email)
        driver.find_element_by_name("User[password]").send_keys(random_password)
        driver.find_element_by_name("User[password2]").send_keys(random_password)
        driver.find_element_by_id("User_check_communication_1").click()
        driver.find_element_by_name("User[skype]").send_keys(random_skype)
        driver.find_element_by_xpath('//*[@id="registration-form"]/div[9]/div/button').click()
        sleep(4)
        try:
            driver.find_element_by_xpath("//*[contains(text(), 'Registration is completed')]")
        except Exception:
            print('Registration failed. Test stoped')
            self.driver.close()
        else:
            print('Registration completed')
    #Email activation
        driver.switch_to.window(driver.window_handles[0])
        sleep(5)
        driver.refresh()
        driver.find_element_by_xpath('//*[@id="message_list"]/table/tbody/tr/td[2]/a').click()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[2]/p/a').click()
        try:
            driver.find_element_by_xpath("//*[contains(text(), 'Activation completed')]")
        except Exception:
            print('Registration failed')
            self.driver.close()
        else:
            print('Activation completed')
    #Account approval
        driver.get("http://test.leadrock.com")
        driver.find_element_by_link_text('Login').click()
        driver.find_element_by_id('LoginForm_username').send_keys(input("Введите email: "))
        driver.find_element_by_id('LoginForm_password').send_keys(input("Введите пароль: "), Keys.ENTER)
        sleep(4)
        driver.get('http://test.leadrock.com/administrator/moderate/user')
        driver.find_element_by_name('User[email]').send_keys(temp_email, Keys.ENTER)
        sleep(5)
        driver.find_element_by_xpath('//*[@id="list-moderate"]/table/tbody/tr[1]/td[8]/a[1]').click()
        sleep(3)
        try:
            driver.find_element_by_xpath("//*[contains(text(), 'Статус успешно изменен')]")
        except Exception:
            print('Registration failed')
            self.driver.close()
        else:
            print('Approve completed')
        driver.get('http://test.leadrock.com/user/authorization/logout')
        driver.find_element_by_link_text('Войти').click()
        driver.find_element_by_id('LoginForm_username').send_keys(temp_email)
        driver.find_element_by_id('LoginForm_password').send_keys(random_password, Keys.ENTER)
        sleep(4)
        try:
            driver.find_element_by_xpath("//*[contains(text(), 'Data Summary')]")
        except Exception:
            print('Registration failed')
            self.driver.close()
        else:
            print('Registration passed')

    #Random
def random_number(n):
    start = 10**(n-1)
    end = (10**n)-1
    return randint(start, end)
def random_word(m):
    return ''.join(choice(ascii_uppercase) for i in range(m))

if __name__ == "__main__":
    unittest.main()
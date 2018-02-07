from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
from random import randint
from random import choice
from string import ascii_uppercase


driver=webdriver.Chrome("C:\\drivers\\chromedriver.exe")
driver.maximize_window()
    #Temp mail
driver.get("https://www.mydlo.ru/")
registration_email= driver.find_element_by_id("mbox-address")
temp_email = registration_email.get_attribute("textContent")
print("Temp email is " + temp_email)
    #Random
def random_number(n):
    start = 10**(n-1)
    end = (10**n)-1
    return randint(start, end)
def random_word(m):
    return ''.join(choice(ascii_uppercase) for i in range(m))
random_skype = random_word(6).upper()
random_password = random_word(10)
    #Landing
driver.get("http://test.leadrock.com/")
driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[8]/a").click()
driver.find_element_by_name("User[email]").send_keys(temp_email)
driver.find_element_by_name("User[password]").send_keys(random_password)
driver.find_element_by_name("User[password2]").send_keys(random_password)
driver.find_element_by_id("User_check_communication_1").click()
driver.find_element_by_name("User[skype]").send_keys(random_skype)
driver.find_element_by_xpath('//*[@id="registration-form"]/div[8]/div/button').click()

driver.quit()

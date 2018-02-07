from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome("C:\\drivers\\chromedriver.exe")
driver.maximize_window()
driver.get("http://test.leadrock.com/")
driver.find_element_by_xpath('/html/body/header/div/nav/ul/li[7]/a').click()
driver.find_element_by_id('LoginForm_username').send_keys(input("Введите email: "))
driver.find_element_by_id('LoginForm_password').send_keys(input("Введите пароль: "), Keys.ENTER)
driver.get("http://test.leadrock.com/administrator/offer/offer/list")
select = Select(driver.find_element_by_id("offer-name")).select_by_value("1")
driver.find_element_by_xpath("//*[contains(text(), 'Фильтровать')]").click()
driver.find_element_by_xpath('//*[@id="yw1"]/table/tbody/tr/td[12]/a').click()
driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/ul/li[5]/a").click()
Weblink = driver.find_element_by_xpath('//*[@id="yw3"]/table/tbody/tr/td[5]').text
Postback =driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[3]/td[2]").text
driver.get(Weblink)
Url = driver.current_url
Trkid = re.search(r'\=([\d]*)', Url)
print("trkid=" + Trkid.group(1))
Replace = Postback.replace("{subId}", "");
driver.get(Replace + Trkid.group(1))
try:
    driver.find_element_by_xpath("//*[contains(text(), 'Ok')]")
except Exception:
    print("Lead ERROR")
else:
    print("Lead was created")
time.sleep(3)
driver.quit()
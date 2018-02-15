import json
import requests
import unittest
from selenium import webdriver

class CasCore(unittest.TestCase):

    def setUp(self):
            self.driver = webdriver.PhantomJS("phantomjs.exe")

    def test_User(self):
    #Information
        url = 'http://cas-core.kpilead.ru/api/v1/user/info'
        print('\nUser - Информация' + '\nURL: ' + url)
        headers = {'Content-type': 'application/json',
                   'Accept': 'text/plain',
                   'Content-Encoding': 'utf-8'}
        data = {"user_id": 13,
                "games_limit": 300,
                "games_offset": 0}
        post(data, url, headers)

    #Registration
        url = 'http://cas-core.kpilead.ru/api/v1/user/register'
        print('\nUser - Регистрация' + '\nURL: ' + url)
        post('', url, headers)

    def test_Machine(self):
    #Game
        url = 'http://cas-core.kpilead.ru/api/v1/machine/play'
        print('\nMachine - Игра' + '\nURL: ' + url)
        headers = {'Content-type': 'application/json',
                   'Accept': 'text/plain',
                   'Content-Encoding': 'utf-8'}
        data = {"user_id": 13,
                "machine_id": 1,
                "bet": 1}
        post(data, url, headers)
    #Information
        url = 'http://cas-core.kpilead.ru/api/v1/machine/detail'
        print('\nMachine - Информация' + '\nURL: ' + url)
        data = {"machine_id": 1}
        post(data, url, headers)
    #List
        url = 'http://cas-core.kpilead.ru/api/v1/machine/list'
        print('\nMachine - Список доступных пользователю машин' + '\nURL: ' + url)
        data = {"user_id": 1}
        post(data, url, headers)

    def test_Balance(self):
    # Input
        url = 'http://cas-core.kpilead.ru/api/v1/balance/recharge'
        print('\nBalance - Ввод средств' + '\nURL: ' + url)
        headers = {'Content-type': 'application/json',
                   'Accept': 'text/plain',
                   'Content-Encoding': 'utf-8'}
        data = {"user_id": 13,
                "value": 300}
        post(data, url, headers)
    #Output
        url = 'http://cas-core.kpilead.ru/api/v1/balance/payout'
        print('\nBalance - Вывод средств' + '\nURL: ' + url)

        data = {"user_id": 13,
                "value": 200}
        post(data, url, headers)

def post(data, url, headers):
    print('Request: ' + str(data))
    answer = requests.post(url, data=json.dumps(data), headers=headers)
    response = answer.json()
    print(str(answer) + '\nResponse: ' + str(response))
    check = '<Response [200]>'
    if check == str(answer):
        print('OK')
    else:
        print('ERROR!!')
        driver.quit()


if __name__ == "__main__":
    unittest.main()
    driver.close()
    driver.quit()

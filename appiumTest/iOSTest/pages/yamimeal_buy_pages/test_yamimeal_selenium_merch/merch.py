# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 6:49 下午
# @Author  : Cyrus
# @File    : merch.py
# @Software: PyCharm
# @Function: 联动appium
import json
from time import sleep

from selenium import webdriver

class selenium_yamimeal_merch:
    def linkage_appium(self):
        driver = webdriver.Chrome()
        #由于机制原因需要做一步登录跳转
        driver.get('https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f')
        driver.find_element_by_class_name('iconGoogle').click()
        driver.find_element_by_class_name('zHQkBf').send_keys('hw19950322@gmail.com')
        driver.find_element_by_class_name('VfPpkd-RLmnJb').click()
        sleep(5)
        driver.find_element_by_css_selector('#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input').send_keys('Core0322..')
        sleep(3)
        driver.find_element_by_class_name('VfPpkd-RLmnJb')
        cookies = driver.get_cookies()
        print(cookies)
        with open('cookies.txt','w') as fp:
            json.dump(cookies,fp)



        # driver.get('https://yamimealservertest.azurewebsites.net/web/merch/#/merch/orders/index')
        js = "window.open('https://yamimealservertest.azurewebsites.net/web/merch/#/merch/orders/index')"
        driver.execute_script(js)
        sleep(5)
        driver.find_element_by_class_name('loginStyle').click()
        driver.find_element_by_name('loginfmt').send_keys('562792094@qq.com')
        driver.find_element_by_name('passwd').send_keys()




if __name__ == '__main__':
    a = selenium_yamimeal_merch()
    a.linkage_appium()
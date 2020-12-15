# -*- coding: utf-8 -*-
# @Time    : 2020/12/9 3:32 下午
# @Author  : Cyrus
# @File    : test_wb_Mammal_login.py
# @Software: PyCharm
# @Function :用例执行入口

import allure
import pytest
from appiumTest.iOSTest.pages.yamimeal_login_pages.login_Test import loginPage
import time
from appium import webdriver
import os

@allure.feature('test_login')
class Test_YamimealLogin():

    def setup_method(self,method) -> None:
        desired_caps = {
                            "platformName": "iOS",
                            "deviceName": "iPhone",
                            "bundleId": "com.benmu.mobile.YamiMeal",
                            "AutomationName": "XCUITest",
                            "udid": "00008030-0004688822A1802E",
                            "platformVersion": "14.0",
                        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.case = self
    def teardown_method(self,method) -> None:
        time.sleep(2)
        self.driver.close_app()
    #执行测试用例
    '''
        :param:loginPage 有两个参数
                driver:appium控制器
                case:unittest框架
    '''
    @allure.story('微信登录')
    # def test_wx_Yamimeal_login(self):
    #     '''微信登录'''
    #     yamimealLoginPage = loginPage(self.driver,self.case)
    #     yamimealLoginPage.login_approbject(0)

    # def test_fb_Yamimeal_login(self):
    #     '''脸书登录'''
    #     fbLoginPage = loginPage(self.driver,self.case)
    #     fbLoginPage.login_approbject(1)

    def test_google_yamimeal_login(self):
        '''谷歌第三方登录'''
        ggLoginPage = loginPage(self.driver,self.case)
        ggLoginPage.login_approbject(2)


    # def test_apple_yamimeal_login(self):
    #     '''苹果第三方登录'''


    # def test_skip_yamimel_login(self):
    #     '''跳过按钮'''
    #     skipLoginPage = loginPage(self.driver,self.case)
    #     skipLoginPage.login_approbject(4)

    # def test_fb_en_yamimeal_login(self):
    #     enFbLoginPage = loginPage(self.driver,self.case)
    #     enFbLoginPage.login_approbject_EN(0)


if __name__ == '__main__':
    pytest.main(['-s', './Test_wb_yamimeal_login.py', '--alluredir', './temp','--reruns','2'])
    os.system('allure generate ./temp -o ./report --clean')




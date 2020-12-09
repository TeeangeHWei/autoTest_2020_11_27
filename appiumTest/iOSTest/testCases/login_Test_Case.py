# coding=utf-8

from appiumTest.iOSTest.pages.login_Test import loginPage
import unittest
import time
from appium import webdriver
import os






class testYamimealLogin(unittest.TestCase):

    def setUp(self) -> None:
        app = os.path.abspath('/Users/cyrus.h/Desktop/AutoTest/autoTest_2020_11_27/appiumTest/iOSTest/config/Yamimeal_2.7.0.ipa')
        desired_caps = {
                          "platformName": "iOS",
                          "deviceName": "甜在心馒头",
                          "bundleId":"com.benmu.YamiMeal",
                          "AutomationName":"XCUITest",
                          "udid":"00008020-000E2D540209002E",
                          "platformVersion": "14.1",
                          "app":app
                        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.case = self
    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.close_app()
    #执行测试用例
    '''
        :param:loginPage 有两个参数
                driver:appium控制器
                case:unittest框架
    '''
    def test_wx_Yamimeal_login(self):
        '''微信登录'''
        yamimealLoginPage = loginPage(self.driver,self.case)
        yamimealLoginPage.login_approbject(0)

    # def test_fb_Yamimeal_login(self):
    #     '''脸书登录'''
    #     fbLoginPage = loginPage(self.driver,self.case)
    #     fbLoginPage.login_approbject(1)

    # def test_google_yamimeal_login(self):
    #     '''谷歌第三方登录'''
    #     ggLoginPage = loginPage(self.driver,self.case)
    #     ggLoginPage.login_approbject(2)


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
    unittest.main()

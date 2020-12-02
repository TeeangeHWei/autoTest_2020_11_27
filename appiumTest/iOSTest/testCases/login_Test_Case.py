# coding=utf-8

from appiumTest.iOSTest.pages.login_Test import loginPage
import unittest
import time
from appium import webdriver




class testYamimealLogin(unittest.TestCase):
    def setUp(self) -> None:
        desired_caps = {
                          "platformName": "iOS",
                          "deviceName": "甜在心馒头",
                          "bundleId":"com.benmu.YamiMeal",
                          "AutomationName":"XCUITest",
                          "udid":"00008020-000E2D540209002E",
                          "platformVersion": "14.1",
                        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.case = self
    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.close_app()
    #执行测试用例
    # def wx_Yamimeal_login(self):
    #     yamimealLoginPage = loginPage(self.driver)
    #     yamimealLoginPage.login_approbject(0)

    def test_fb_Yamimeal_login(self):
        '''脸书登录'''
        fbLoginPage = loginPage(self.driver,self.case)
        fbLoginPage.login_approbject(1)

    def test_google_yamimeal_login(self):
        '''谷歌第三方登录'''
        ggLoginPage = loginPage(self.driver,self.case)
        ggLoginPage.login_approbject(2)


    # def test_apple_yamimeal_login(self):
    #     '''苹果第三方登录'''


    # def skip_yamimel_login(self):
    #     skipLoginPage = loginPage(self.driver)
    #     skipLoginPage.login_approbject(3)


if __name__ == '__main__':
    unittest.main()

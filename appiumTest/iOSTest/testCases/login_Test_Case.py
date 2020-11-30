# coding=utf-8

from appiumTest.AndroidTest.pages.login_Test import loginPage
import unittest
import time
from appium import webdriver


class testYamimealLogin(unittest.TestCase):
    def setUp(self) -> None:
        desired_caps = {
                          "platformName": "Android",
                          "deviceName": "127.0.0.1:62001",
                          "appPackage": "com.proton.YamiMeal",
                          "appActivity": "com.proton.YamiMeal.activity.SplashActivity",
                          "platformVersion": "7"
                        }

        desired_caps["unicodeKeyboard"] = True  # 使用unicode编码方式发送字符串
        desired_caps["resetKeyboard"] = True   # 将键盘隐藏起来
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.verificationError = u''

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.close_app()
    #执行测试用例
    def test_Yamimeal_login(self):
        yamimealLoginPage = loginPage(self.driver)
        yamimealLoginPage.login_approbject(0)

        self.assertEqual(self.verificationError, yamimealLoginPage.login_result_text, msg=u'验证失败')


if __name__ == '__main__':
    unittest.main()

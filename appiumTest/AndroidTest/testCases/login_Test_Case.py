# coding=utf-8

from appiumTest.AndroidTest.pages.login_Test import loginPage
import unittest
import time
from appium import webdriver


class testYamimealLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.imgs = []
        desired_caps = {
                          "platformName": "Android",
                          "deviceName": "emulator-5554",
                          "appPackage": "com.sjhd.yamimealmerchant",
                          "appActivity": "com.sjhd.yamimealmerchant.SplashActivity",
                          "platformVersion": "7"
                        }

        desired_caps["unicodeKeyboard"] = True  # 使用unicode编码方式发送字符串
        desired_caps["resetKeyboard"] = True   # 将键盘隐藏起来
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.verificationError = u''

    # 截图
    def get_screenShot(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.close_app()


    #执行测试用例
    def test_Yamimeal_login(self):
        yamimealLoginPage = loginPage(self.driver)
        yamimealLoginPage.login_approbject(0)



if __name__ == '__main__':
    unittest.main()

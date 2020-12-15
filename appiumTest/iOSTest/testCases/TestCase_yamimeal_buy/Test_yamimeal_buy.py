# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 1:48 下午
# @Author  : Cyrus
# @File    : Test_yamimeal_buy.py
# @Software: PyCharm
# @Function : 购物流程用例页面
import os

import allure
import time

import pytest
from appium import webdriver
from appiumTest.iOSTest.pages.yamimeal_buy_pages.test_yamimeal_buy_pages import buy_Pages
from appiumTest.iOSTest.pages.yamimeal_order_pages.test_yamimeal_order_pages import order_Pages
@allure.feature('test_buy')
class Test_Yamimeal_buy():

    def setup_method(self):
        '''

        :return: 初始化设备
        '''
        test_device_udid = '00008030-0004688822A1802E'
        my_phone_udid = '00008020-000E2D540209002E'
        desired_caps = {
            "platformName": "iOS",
            "deviceName": "iPhone",
            "bundleId": "com.benmu.mobile.YamiMeal",
            "AutomationName": "XCUITest",
            "udid": test_device_udid,
            "platformVersion": "14.0",
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.case = self



    def teardown_method(self) -> None:
        '''

        :return: 在运行结束时跑此方法
        '''

        time.sleep(2)
        self.driver.close_app()

    # @allure.story('购买流程')
    # def test_buy_01(self):
    #     buy_case_01 = buy_Pages(self.driver)
    #     buy_case_01.Test_NormalBuy()

    @allure.story('分类购买')
    def test_buy_02(self):
        buy_case_01 = buy_Pages(self.driver)
        buy_case_01.Test_Category_Buy()

    @allure.story('订单情况')
    def test_order_02(self):
        order_case_01 = order_Pages(self.driver)
        # order_case_01.Test_order_process()





if __name__ == '__main__':
    pytest.main(['-s', './Test_yamimeal_buy.py', '--alluredir', './temp', '--reruns', '2'])
    os.system('allure generate ./temp -o ./report --clean')








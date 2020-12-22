# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 1:48 下午
# @Author  : Cyrus
# @File    : Test_yamimeal_buy.py
# @Software: PyCharm
# @Function : 购物流程用例页面
import os
import re

import allure
import time
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appiumTest.iOSTest.pages.yamimeal_buy_pages.test_yamimeal_buy_pages import buy_Pages
from appiumTest.iOSTest.pages.yamimeal_order_pages.test_yamimeal_order_pages import order_Pages
from appiumTest.iOSTest.pages.yamimeal_login_pages.page_Elements import pageElements
from appiumTest.iOSTest.common import basePage
from time import sleep
from appiumTest.iOSTest.common.math_formula import math_mula
import pytest_check as check


@allure.feature('测试购买')
class Test_Yamimeal_buy():
    buyClose = pageElements.buy_close_btn
    account_btn = pageElements.account_click_btn
    account_collection_btn = pageElements.account_collection_btn
    item_01 = pageElements.your_collection_item
    add_btn = pageElements.add_Goods_btn
    category_Item_btn = pageElements.categroy_item
    category_suffix = pageElements.categroy_item_suffix
    checkOut_btn = pageElements.check_out_btn
    nextStep_btn = pageElements.next_step_btn
    placeOrder_btn = pageElements.placeOrder_btn
    orderText_btn = pageElements.order_comfirm_text
    orderdetail_btn = pageElements.order_detail_btn
    pop_btn = pageElements.pop_btn
    isScrollView_element = pageElements.isScrollView
    small_num_text = pageElements.goods_smallNum_text
    math = math_mula()
    elements_List = []
    num_list = []

    # ----------------------------结账时所有参数---------------------------#
    # 商品小计
    goods_xiaoji = 0.0
    # yamimeal服务费
    yamimeal_service_tips = 0.0
    # 配送费 有两个数据类型 str，float
    delivery_tips = 0.0
    # 优惠价扣除
    discount_OFF = 0.0
    # 商家服务费
    merch_Service_tips = 0.0
    # 小费
    tips = 0.0
    # 总合计
    total = 0.0
    # 包装费
    package_tips = 0.0
    # 商品税
    goods_tax = 0.0
    # 税
    tax = 0.0
    # ----------------------------end---------------------------#

    # ----------------------------测试时结账所有测试参数---------------------------#
    # 商品小计
    test_goods_xiaoji = 10
    # yamimeal服务费
    test_yamimeal_service_tips = 0.0
    # 配送费 有两个数据类型 int，float
    test_delivery_tips = 0.0
    # 优惠价扣除
    test_discount_OFF = 0.6
    # 商家服务费
    test_merch_Service_tips = 0.1
    # 小费
    test_tips = 0.0
    # 总合计
    test_total = 0.0
    # 包装费
    test_package_tips = 1.0
    #商品税
    test_goods_tax = 0.0
    # 税
    test_tax = 0.7

    # ----------------------------end---------------------------#

    def setup_method(self):
        '''

        :return: 初始化设备
        '''
        test_device_udid = '00008030-0004688822A1802E'
        my_phone_udid = '00008020-000E2D540209002E'
        simulator = 'E112CE20-6269-4306-972B-F8D8C3C234EF'
        # 模拟器 使用uuid
        desired_caps = {
            "platformName": "iOS",
            "deviceName": "iPhone",
            "bundleId": "com.benmu.mobile.YamiMeal",
            "AutomationName": "XCUITest",
            "udid": my_phone_udid,
            "platformVersion": "14.0",
            "locationServicesAuthorized":"true",
            "waitForAppScript":"$.delay(5000); $.acceptAlert(); true;",
        }
        simulator_desired_cpas = {
            "platformName": "iOS",
            "deviceName": "iPhone 11 Pro Max",
            "bundleId": "com.benmu.mobile.YamiMeal",
            "AutomationName": "XCUITest",
            # "udid": my_phone_udid,
            "uuid": simulator,
            "platformVersion": "14.2",
            "app": "/Users/cyrus.h/Desktop/AutoTest/Yamimeal2.8.0.ipa"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        self.basePage = basePage.basePage(self.driver)





    @allure.story('关闭虚拟器')
    def teardown_method(self) -> None:
        '''

        :return: 在运行结束时跑此方法
        '''

        time.sleep(2)
        self.driver.close_app()

    def Common_Tools(self):
        self.driver.implicitly_wait(10)
        sleep(3)

        # 出现 ：你的账户需要更新时弹窗选项 处理
        # '点击空白页面 将弹窗消失'
        TouchAction(self.driver).tap(x=272, y=90).perform().release()
        sleep(1)
        TouchAction(self.driver).tap(x=272, y=90).perform().release()
        print('點擊消除綁定手機的彈窗\n')
        # '點擊出现 感谢你最近的订单弹窗元素'
        sleep(1)
        try:
            # 特殊情况
            self.basePage.by_AccessId(buy_Pages).click()
            print('點擊關閉彈窗close\n')
        except Exception as e:
            print('找不到元素并跳过')
            pass
        # '點擊賬戶找到商店'
        self.basePage.by_AccessId(self.account_btn).click()
        print('點擊了tabbar的賬戶')
        # 点击收藏
        self.basePage.iOS_By_ClassChain(self.account_collection_btn).click()

        self.basePage.iOS_By_ClassChain(self.item_01).click()

    # @allure.story('测试普通购买')
    # def test_NormalBuy(self):
    #     self.Common_Tools()
    #     sleep(2)
    #     itemList = ['[1]', '[2]']
    #
    #     # 遍历item数量判断list 的位置
    #     for i in itemList:
    #         self.basePage.iOS_By_ClassChain(self.add_btn + i).click()
    #         print('点击了item添加数量')
    #     self.basePage.iOS_By_ClassChain(self.checkOut_btn).click()
    #     sleep(5)
    #     TouchAction(self.driver).tap(x=275, y=446).perform().release()
    #     # 下一步
    #     self.basePage.iOS_By_ClassChain(self.nextStep_btn).click()
    #     print('点击下一步')
    #     # 下单
    #     self.basePage.iOS_By_ClassChain(self.placeOrder_btn).click()
    #     print('点击下单')
    #     # 确认文本
    #     ordertext = self.basePage.iOS_By_ClassChain(self.orderText_btn).text
    #     assert ordertext == u'訂單確認'
    #
    #     # 进入订单详情
    #     self.basePage.by_AccessId(self.orderdetail_btn).click()
    #     print('成功下单，用例pass')

    # def test_Category_Buy(self):
    #     '''此方法未完善'''
    #     print('开始点击分类下单')
    #     list = ['[1]', '[2]', '[3]', '[4]', '[5]', '[6]', '[7]', '[8]', '[9]']
    #     self.Common_Tools()
    #
    #     # 遍历类别个数
    #     for i in list:
    #         try:
    #             print('元素' + self.isScrollView_element + i)
    #             sleep(3)
    #             self.iOS_By_ClassChain(self.isScrollView_element + i).click()
    #         except Exception as e:
    #             sleep(3)
    #             print('元素' + self.category_Item_btn + i + self.category_suffix)
    #             self.iOS_By_ClassChain(self.category_Item_btn + i + self.category_suffix).click()
    #             print('点击当前第:' + i + '个')
    #         # self.iOS_By_ClassChain(self.add_btn + i).click()
    #
    #     self.iOS_By_ClassChain(self.checkOut_btn).click()
    #     sleep(5)
    #     TouchAction(self.driver).tap(x=275, y=446).perform().release()
    #
    #     # 下一步
    #     self.iOS_By_ClassChain(self.nextStep_btn).click()
    #     print('点击下一步')
    #     # 下单
    #     self.iOS_By_ClassChain(self.placeOrder_btn).click()
    #     print('点击下单')
    #     # 确认文本
    #     ordertext = self.iOS_By_ClassChain(self.orderText_btn).text
    #     assert ordertext == u'訂單確認'
    # @allure.story('测试进入结账页面')
    # def test_Goods_Money_Heji(self):
    #     '''
    #     :case: 配送区域最低起定金额计算方式是否只计算合计
    #     :return:
    #     '''
    #     with allure.step('step1:进入收藏页面'):
    #         self.Common_Tools()
    #     sleep(2)
    #     itemList = ['[1]', '[2]']
    #
    #     with allure.step('step2:点击物品的数量和付款按钮'):
    #         # 遍历item数量判断list 的位置
    #         for i in itemList:
    #             self.basePage.iOS_By_ClassChain(self.add_btn + i).click()
    #             print('点击了item添加数量')
    #         self.basePage.iOS_By_ClassChain(self.checkOut_btn).click()
    #         sleep(5)
    #         TouchAction(self.driver).tap(x=275, y=446).perform().release()
    #         sleep(2)
    #         self.driver.swipe(start_x=166, start_y=702, end_x=184, end_y=324, duration=300)
    #         sleep(5)
    #     with allure.step('step2:进入结账页面遍历元素数据'):
    #         small_num = self.basePage.by_name_elements('XCUIElementTypeStaticText')
    #
    #         # 遍历所有TEXT的属性值元素
    #         for i in small_num:
    #             print(i.get_attribute('value'))
    #             self.elements_List.append(i.get_attribute('value'))
    #         print(self.elements_List)
    #
    #         # 遍历已经添加的今list的元素 获取下标和值
    #         try:
    #             for index, value in enumerate(self.elements_List):
    #                 print('元素下标为' + str(index) + ',对应属性值为:' + value)
    #         except Exception as e:
    #             print(e)
    #     # 切割字符串只保留浮点数
    #     # 商品小计
    #     xiaoji_str = str(self.elements_List[5]).replace('$ ', '')
    #     self.goods_xiaoji = float(xiaoji_str)
    #     print('商品小计' + str(self.goods_xiaoji))
    #     assert self.goods_xiaoji==self.test_goods_xiaoji

    @allure.story('测试包装税')
    def test_goods_packing(self):
        self.in_buy_page()
        # 包装费
        # package_tips_str = str(self.elements_List[15]).replace('$ ', '')
        # self.package_tips = float(package_tips_str)
        self.package_tips = float(self.num_list[14])
        print(self.package_tips)
        print('包装费' + str(self.package_tips))
        packing_total = self.math.packing_Tax(self.test_package_tips,self.test_tax)
        assert self.package_tips == packing_total


    @allure.story('测试商家服务费')
    def test_merch_service_tips(self):
        self.in_buy_page()
        # 商家服务费
        # merch_service_tips_str = str(self.elements_List[34]).replace('$ ', '')
        self.merch_Service_tips = float(self.num_list[15])

        print(str(self.elements_List[48]) + str(self.merch_Service_tips))
        assert self.merch_Service_tips == self.test_merch_Service_tips

    @allure.story('测试税')
    def test_tax(self):
        #税
        self.in_buy_page()
        # tax_str = str(self.elements_List[18]).replace('$ ', '')
        self.tax = float(self.num_list[8])
        # str(elements_List[19]).replace('-$ ', '')
        print(str(self.elements_List[39]) + str(self.tax))
        delivery_tax = self.math.delivery_Tax(self.test_delivery_tips,self.test_tax)
        print(delivery_tax)
        packing_tax = self.math.packing_Tax(self.test_package_tips,self.test_tax)
        merch_tax = self.math.merch_Goods_Tax(self.test_goods_xiaoji,self.test_discount_OFF,self.test_goods_tax)
        merch_service_tax = self.math.merch_service_tax(self.test_goods_xiaoji,self.test_discount_OFF,self.test_tax)
        tax_total = self.math.Tax(delivery_tax,packing_tax,merch_tax,merch_service_tax)
        assert self.tax == tax_total

    # @allure.story('测试yamimeal服务费')
    #
    # def test_yamimeal_service_tips(self):
    #     # yamimeal服务费
    #     yamimeal_tips_str = str(self.elements_List[39]).replace('$ ', '')
    #     self.yamimeal_service_tips = float(yamimeal_tips_str)
    #     print(str(self.elements_List[53]) + str(self.yamimeal_service_tips))6
    #     yamimeal_tips = self.math.


        # 配送费
    @allure.story('测试配送费')
    def test_delivery(self):
        delivery_str = str(self.elements_List[33]).replace('$ ', '')
        self.delivery_tips = float(delivery_str)
        print(str(self.elements_List[35]) + str(self.delivery_tips))
        # assert self.delivery_tips == self.test_delivery_tips
        #
    @allure.story('测试总计消费')
    def test_total_num(self):
        # # 合计总消费
        # total_str = str(self.elements_List[8]).replace('$ ', '')
        self.total = float(self.num_list[3])
        print(str(self.elements_List[16]) + str(self.total))

    def in_buy_page(self):
        self.Common_Tools()
        sleep(2)
        itemList = ['[1]', '[2]']

        # 遍历item数量判断list 的位置
        for i in itemList:
            self.basePage.iOS_By_ClassChain(self.add_btn + i).click()
            print('点击了item添加数量')
        self.basePage.iOS_By_ClassChain(self.checkOut_btn).click()
        sleep(5)
        TouchAction(self.driver).tap(x=275, y=446).perform().release()
        sleep(2)
        self.driver.swipe(start_x=166, start_y=702, end_x=184, end_y=324, duration=300)
        sleep(5)
        small_num = self.basePage.by_name_elements('XCUIElementTypeStaticText')
        # 遍历所有TEXT的属性值元素
        for i in small_num:
            print(i.get_attribute('value'))
            self.elements_List.append(i.get_attribute('value'))
        print(self.elements_List)
        for i in self.elements_List:
            num = re.sub("[^0-9.]","",i)
            if len(num) > 0:
                self.num_list.append(num)
        print(self.num_list)

        # 遍历已经添加的今list的元素 获取下标和值
        try:
            for index, value in enumerate(self.elements_List):
                print('元素下标为' + str(index) + ',对应属性值为:' + value)
        except Exception as e:
            print(e)



if __name__ == '__main__':
    math_mula.del_file('./temp')
    pytest.main(['-s','-v','./Test_yamimeal_buy.py','--alluredir','./temp'])
    os.system('allure generate ./temp -o ./testreport --clean')








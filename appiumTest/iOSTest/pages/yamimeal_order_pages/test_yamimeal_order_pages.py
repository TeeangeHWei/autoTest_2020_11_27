# -*- coding: utf-8 -*-
# @Time    : 2020/12/12 11:36 上午
# @Author  : Cyrus
# @File    : test_yamimeal_order_pages.py
# @Software: PyCharm
# @Function :订单页面测试
from time import sleep
from appiumTest.iOSTest.common import basePage
from appiumTest.iOSTest.pages.yamimeal_login_pages.page_Elements import pageElements
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait

class order_Pages(basePage.basePage):
    order_tabbar_btn = pageElements.order_click_btn
    order_wait_text = pageElements.order_Wait_Text
    order_readying = pageElements.order_readying_Text
    order_ready_Delivery = pageElements.order_Delivery_Text
    order_ready_Deliverying = pageElements.order_Deliverying_Text
    have_good_btn = pageElements.have_goods_btn


    def Test_order_process(self):
        self.driver.implicitly_wait(10)
        tabbar_order = self.by_AccessId(self.order_tabbar_btn)
        tabbar_order.click()
        sleep(5)
        print('---------点击订单--------')
        sleep(2)
        order_wait = self.iOS_By_ClassChain(self.order_wait_text)
        order_wait_text = order_wait.text
        print('当前输出：' + order_wait_text)
        assert order_wait_text == u'訂單待處理'
        sleep(2)
        for i in range(100):
            try:
                sleep(i)
                print('--------进入订单待处理界面------------')
                order_ready = self.iOS_By_ClassChain(self.order_readying)
                order_ready_text = order_ready.text
                print('当前输出：' + order_ready_text)
                assert order_ready_text == u'訂單準備中'
                break
            except Exception as e:
                print('订单页面待处理text还未执行的改变第：'+str(i)+'次')
        print('------------通过订单准备中界面------------------\n')

        print('-----------进入订单准备送货中-----------')
        for i in range(100):
            try:
                order_delivery = self.iOS_By_ClassChain(self.order_ready_Delivery)
                order_delivery_text = order_delivery.text
                assert order_delivery_text == u'準備好送貨'
                break
            except Exception as e:
                print('订单页面准备好送货text还未改变执行的第：'+str(i)+'次')
        print('-----------通过"准备好送货"界面-----------\n')

        print('-------进入订单送货中界面-------------')
        for i in range(100):
            try:
                order_deliverying = self.iOS_By_ClassChain(self.order_ready_Deliverying)
                order_deliverying_text = order_deliverying.text
                assert order_deliverying_text == u'訂單送貨中'
                print('-------------通过"订单送货中"------------')
                break
            except Exception as e:

                print('订单页面送货中text还未改变执行的第：'+str(i)+'次')

        for i in range(100):
            try:
                TouchAction(self.driver).tap(x=299,y=590).perform().release()
                # have_goods = self.iOS_By_ClassChain(self.have_good_btn)
                # have_goods.click()
                print('确认收货')
                break
            except Exception as e:
                print('订单页面已收货还未找到元素的第：' + str(i) + '次')















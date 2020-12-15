# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 2:03 下午
# @Author  : Cyrus
# @File    : test_yamimeal_buy_pages.py
# @Software: PyCharm
# @Function :购买测试用例页面


from time import sleep
from appiumTest.iOSTest.common import basePage
from appiumTest.iOSTest.pages.yamimeal_login_pages.page_Elements import pageElements
from appium.webdriver.common.touch_action import TouchAction

class buy_Pages(basePage.basePage):
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

    def Common_Tools(self):
        self.driver.implicitly_wait(10)
        sleep(3)

        # 出现 ：你的账户需要更新时弹窗选项 处理
        # '点击空白页面 将弹窗消失'
        TouchAction(self.driver).tap(x=272, y=90).perform().release()
        print('點擊消除綁定手機的彈窗\n')
        # '點擊出现 感谢你最近的订单弹窗元素'
        sleep(1)
        try:
            # 特殊情况
            self.by_AccessId(buy_Pages).click()
            print('點擊關閉彈窗close\n')
        except Exception as e:
            print('找不到元素并跳过')
            pass
        # '點擊賬戶找到商店'
        self.by_AccessId(self.account_btn).click()
        print('點擊了tabbar的賬戶')
        # 点击收藏
        self.iOS_By_ClassChain(self.account_collection_btn).click()

        self.iOS_By_ClassChain(self.item_01).click()


    def Test_NormalBuy(self):
        '''普通购买'''
        self.Common_Tools()
        sleep(2)
        itemList = ['[1]','[2]']

        #遍历item数量判断list 的位置
        for i in itemList:
            self.iOS_By_ClassChain(self.add_btn + i).click()
            print('点击了item添加数量')
        self.iOS_By_ClassChain(self.checkOut_btn).click()
        sleep(5)
        TouchAction(self.driver).tap(x=275,y=446).perform().release()

        #下一步
        self.iOS_By_ClassChain(self.nextStep_btn).click()
        print('点击下一步')
        #下单
        self.iOS_By_ClassChain(self.placeOrder_btn).click()
        print('点击下单')
        #确认文本
        ordertext = self.iOS_By_ClassChain(self.orderText_btn).text
        assert ordertext == u'訂單確認'

        #进入订单详情
        self.by_AccessId(self.orderdetail_btn).click()
        print('成功下单，用例pass')

    def Test_Category_Buy(self):
        print('开始点击分类下单')
        list = ['[1]','[2]','[3]','[4]','[5]','[6]','[7]','[8]','[9]']
        self.Common_Tools()

        #遍历类别个数
        for i in list:
            try:
                print('元素' + self.isScrollView_element+i)
                sleep(3)
                self.iOS_By_ClassChain(self.isScrollView_element+i).click()
            except Exception as e:
                sleep(3)
                print('元素' + self.category_Item_btn + i + self.category_suffix)
                self.iOS_By_ClassChain(self.category_Item_btn + i + self.category_suffix).click()
                print('点击当前第:' + i + '个')
            # self.iOS_By_ClassChain(self.add_btn + i).click()

        self.iOS_By_ClassChain(self.checkOut_btn).click()
        sleep(5)
        TouchAction(self.driver).tap(x=275, y=446).perform().release()

        # 下一步
        self.iOS_By_ClassChain(self.nextStep_btn).click()
        print('点击下一步')
        # 下单
        self.iOS_By_ClassChain(self.placeOrder_btn).click()
        print('点击下单')
        # 确认文本
        ordertext = self.iOS_By_ClassChain(self.orderText_btn).text
        assert ordertext == u'訂單確認'



























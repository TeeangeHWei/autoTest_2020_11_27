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
import allure
import pytest
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
    small_num_text = pageElements.goods_smallNum_text

    #----------------------------结账时所有参数---------------------------#
    #商品小计
    goods_xiaoji = 0.0
    #yamimeal服务费
    yamimeal_service_tips = 0.0
    #配送费 有两个数据类型 str，float
    delivery_tips = 0.0
    #优惠价扣除
    discount_OFF = 0.0
    #商家服务费
    merch_Service_tips = 0.0
    #小费
    tips = 0.0
    #总合计
    total = 0.0
    #包装费
    package_tips = 0.0
    #税
    tax = 0.0
    # ----------------------------end---------------------------#

    # ----------------------------测试时结账所有测试参数---------------------------#
    # 商品小计
    test_goods_xiaoji = 0.0
    # yamimeal服务费
    test_yamimeal_service_tips = 0.0
    # 配送费 有两个数据类型 int，float
    test_delivery_tips = 0.0
    # 优惠价扣除
    test_discount_OFF = 0.0
    # 商家服务费
    test_merch_Service_tips = 0.0
    # 小费
    test_tips = 0.0
    # 总合计
    test_total = 0.0
    # 包装费
    test_package_tips = 0.0
    # 税
    test_tax = 0.0

    # ----------------------------end---------------------------#
    @allure.story('通用类')
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

    @allure.story('测试普通购买')
    def Test_NormalBuy(self):

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
        '''此方法未完善'''
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
    @allure.story('合计数额')
    def test_Goods_Money_Heji(self):
        '''
        :case: 配送区域最低起定金额计算方式是否只计算合计
        :return:
        '''
        self.Common_Tools()
        sleep(2)
        itemList = ['[1]', '[2]']

        # 遍历item数量判断list 的位置
        for i in itemList:
            self.iOS_By_ClassChain(self.add_btn + i).click()
            print('点击了item添加数量')
        self.iOS_By_ClassChain(self.checkOut_btn).click()
        sleep(5)
        TouchAction(self.driver).tap(x=275, y=446).perform().release()
        sleep(2)
        self.driver.swipe(start_x=166,start_y=702,end_x=184,end_y=324,duration=300)
        sleep(5)
        small_num = self.by_name_elements('XCUIElementTypeStaticText')
        elements_List = []
        #遍历所有TEXT的属性值元素
        for i in small_num:
            print(i.get_attribute('value'))
            elements_List.append(i.get_attribute('value'))
        # print(small_num)
        print(elements_List)

        #遍历已经添加的今list的元素 获取下标和值
        try:
            for index,value in enumerate(elements_List):
                print('元素下标为' + str(index) + ',对应属性值为:' + value)
        except Exception as e:
            print(e)

        try:

            #切割字符串只保留浮点数
            #商品小计
            xiaoji_str = str(elements_List[5]).replace('$ ','')
            self.goods_xiaoji = float(xiaoji_str)
            print('商品小计'+str(self.goods_xiaoji))
            # assert self.goods_xiaoji == self.test_goods_xiaoji,"判断商品小计的值是否为测试预设的数据"
            #优惠off
            discount_off_str = str(elements_List[10]).replace('-$ ','')
            self.discount_OFF = float(discount_off_str)
            print('优惠价'+str(elements_List[17])+str(self.discount_OFF))
            # assert self.discount_OFF == self.test_discount_OFF*self.goods_xiaoji,"判断优惠价的值是否为测试预设的数据"


            # 包装费
            package_tips_str = str(elements_List[6]).replace('$ ', '')
            self.package_tips = float(package_tips_str)
            print('包装费' + str(self.package_tips))
            # assert self.package_tips == self.test_package_tips,"判断包装费的值是否为测试预设的数据"

            #商家服务费
            merch_service_tips_str = str(elements_List[34]).replace('$ ','')
            self.merch_Service_tips = float(merch_service_tips_str)
            print(str(elements_List[48])+str(self.merch_Service_tips))
            # assert self.merch_Service_tips == self.test_merch_Service_tips,"判断商家服务费的值是否为测试预设的数据"

            #税
            tax_str = str(elements_List[18]).replace('$ ','')
            self.tax = float(tax_str)
            str(elements_List[18]).replace('-$ ','')
            print(str(elements_List[39]) + str(self.tax))

            #yamimeal服务费
            yamimeal_tips_str = str(elements_List[40]).replace('$ ','')
            self.yamimeal_service_tips = float(yamimeal_tips_str)
            print(str(elements_List[56]) + str(self.yamimeal_service_tips))
            # assert self.yamimeal_service_tips == self.test_yamimeal_service_tips

            #配送费
            delivery_str = str(elements_List[15]).replace('$ ','')
            self.delivery_tips = float(delivery_str)
            print(str(elements_List[35]) + str(self.delivery_tips))
            # assert self.delivery_tips == self.test_delivery_tips


            #小费
            tips_str = str(elements_List[11]).replace('$ ','')
            self.tips = float(tips_str)
            print(str(elements_List[19]) + str(self.tips))

            #合计总消费
            total_str = str(elements_List[8]).replace('$ ','')
            self.total = float(total_str)
            print(str(elements_List[16]) + str(self.total))
        except Exception as e:
            print(e)



if __name__ == '__main__':
    pytest.main(['-s','./test_yamimeal_buy_pages.py'])
































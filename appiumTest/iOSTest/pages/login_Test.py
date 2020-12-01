# coding=utf-8
from time import sleep

from appiumTest.iOSTest.common import basePage
from appiumTest.iOSTest.pages.page_Elements import pageElements

class loginPage(basePage.basePage):
    weChat_login_Btn = pageElements.wechat_btn_element
    fb_login_Btn = pageElements.fb_btn_element
    google_login_btn = pageElements.fb_btn_element
    appleID_login_btn = pageElements.google_btn_element
    skip_btn = pageElements.skip_btn_element
    confirm_Adrees_Btn = pageElements.confirm_btn_element
    login_result_text = pageElements.login_result_element
    policy_btn = pageElements.policy_element
    permisson_sys_btn = pageElements.permission_element
    fb_aler_continue = pageElements.alert_Countinue_element
    yes_loca_element = pageElements.yes_location_element
    no_loca_element = pageElements.no_location_element
    #截图
    imgs = []
    def clickPolicy(self):
        '''点击协议'''
        self.by_id(self.policy_btn).click()

    def clickSysPermisson(self):
        '''点击权限'''
        self.by_id(self.permisson_sys_btn).click()

    def click_wx_LoginBtn(self):
        """点击微信登录按钮"""
        self.by_id(self.weChat_login_Btn).click()

    def click_fb_loginBtn(self):
        """点击脸书登录按钮"""
        self.by_id(self.fb_login_Btn).click()

    def click_google_login_btn(self):
        """google登录按钮"""
        self.by_id(self.google_login_btn).click()

    def click_appele_login_btn(self):
        """苹果登录按钮"""
        self.by_id(self.appleID_login_btn).click()

    def click_skip_btn(self):
        """跳过"""
        self.by_id(self.skip_btn).click()


    def get_screenShot(self):
        '''截屏方法'''
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True


    def thrid_fb_login(self,status):
        '''fb第三方登录'''
        '''
        status:0 从未登录过 1 已登录过
        '''
        if status == 0:
            self.by_id('').sendKey('')
            self.by_id('').sendKey('')
            self.by_id('').click()
        else:
            sleep(2)
            self.by_AccessId(self.fb_aler_continue).click()
            sleep(3)
            self.by_AccessId(self.fb_aler_continue).click()
            sleep(5)
            self.get_screenShot()
            self.iOS_By_ClassChain(self.yes_loca_element).click()
            sleep(1)
            self.get_screenShot()




    def thrid_gg_login(self):
        '''google登录'''
        self.by_id('').sendKey('')
        self.by_id('').sendKey('')
        self.by_id('').click()


    def thrid_apple_login(self):
        '''苹果登录'''
        self.by_id('').sendKey('')
        self.by_id('').sendKey('')
        self.by_id('').click()


    def login_approbject(self, tag):
        """
        :param tag: 传入需要的登录按钮的tag 0：wechat 1：fb 2：google 3：apple 4：skip
        :return:
        """
        if tag == 0:
            sleep(2)
            #点击协议
            self.clickPolicy()
            sleep(2)
            #截屏
            self.get_screenShot()
            #点击权限
            self.clickSysPermisson()
            #点击wx按钮
            self.click_wx_LoginBtn()

        if tag == 1:
            self.click_fb_loginBtn()
            self.thrid_fb_login(1)
        if tag == 2:
            self.click_google_login_btn()
        if tag == 3:
            self.click_appele_login_btn()
        if tag == 4:
            self.click_skip_btn()

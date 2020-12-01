# coding=utf-8
from time import sleep

from appiumTest.AndroidTest.common import basePage
from appiumTest.AndroidTest.pages.page_Elements import pageElements

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

    #图片list
    imgs = []
    def clickPolicy(self):

        self.by_id(self.policy_btn).click()

    def clickSysPermisson(self):
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
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

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
            #截图
            self.get_screenShot()
            #点击权限
            self.clickSysPermisson()
        if tag == 1:
            self.click_fb_loginBtn()
        if tag == 2:
            self.click_google_login_btn()
        if tag == 3:
            self.click_appele_login_btn()
        if tag == 4:
            self.click_skip_btn()

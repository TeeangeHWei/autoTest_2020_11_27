# coding=utf-8
from time import sleep
from unittestreport import rerun
from appiumTest.iOSTest.common import basePage
from appiumTest.iOSTest.pages.page_Elements import pageElements
from appium.webdriver.common.touch_action import TouchAction
class loginPage(basePage.basePage):

    weChat_login_Btn = pageElements.wechat_btn_element
    fb_login_Btn = pageElements.fb_btn_element
    google_login_btn = pageElements.google_btn_element
    appleID_login_btn = pageElements.google_btn_element
    skip_btn = pageElements.skip_btn_element
    confirm_Adrees_Btn = pageElements.confirm_btn_element
    login_result_text = pageElements.login_result_element
    policy_btn = pageElements.policy_element
    permisson_sys_btn = pageElements.permission_element
    fb_aler_continue = pageElements.alert_Countinue_element
    yes_loca_element = pageElements.yes_location_element
    no_loca_element = pageElements.no_location_element
    logout_account = pageElements.account_click
    logout_userInfo = pageElements.user_click
    logout_btn_click = pageElements.logout_element
    no_try_alert = pageElements.no_Try_element
    off_alert_account_update = pageElements.off_update_account
    gg_third_login = pageElements.gg_thrid_login_element


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
        print('执行了截屏')
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
            sleep(10)
            self.by_AccessId(self.fb_aler_continue).click()
            sleep(10)
            self.by_AccessId(self.fb_aler_continue).click()
            sleep(12)
            self.iOS_By_ClassChain(self.yes_loca_element).click()
            sleep(5)
            self.alert()
            sleep(5)
            homeText = self.by_AccessId('首頁').text
            print(homeText)
            self.assert_Equal(homeText, u'首頁')
            sleep(4)
            self.logout()

    def thrid_gg_login(self,status):
        if status == 0:
            '''google登录'''
            self.by_id('').sendKey('')
            self.by_id('').sendKey('')
            self.by_id('').click()
        else:
            sleep(3)
            self.alert_accept()
            sleep(5)
            self.by_xpath(self.gg_third_login).click()
            sleep(12)
            self.iOS_By_ClassChain(self.yes_loca_element).click()
            sleep(5)
            self.alert()
            sleep(5)
            homeText = self.by_AccessId('首頁').text
            print(homeText)
            self.assert_Equal(homeText, u'首頁')
            sleep(4)
            self.logout()





    def thrid_apple_login(self):
        '''苹果登录'''
        self.by_id('').sendKey('')
        self.by_id('').sendKey('')
        self.by_id('').click()

    def logout(self):
        '''退出登录'''

        self.by_AccessId(self.logout_account).click()
        sleep(1)
        self.iOS_By_ClassChain(self.logout_userInfo).click()
        sleep(5)
        self.iOS_By_ClassChain(self.logout_btn_click).click()
        sleep(1)
        self.alert_accept()
        # logoutext = self.iOS_By_ClassChain('**/XCUIElementTypeStaticText[`value == "歡迎 ,"`]').text
        # self.assertEqual(logoutext,u'歡迎')

    def alert(self):
        '''处理登录之后有需要更新的alert'''
        sleep(10)
        self.by_AccessId(self.no_try_alert).click()
        sleep(10)
        TouchAction(self.driver).press(x=247,y=225).perform().release()



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
            '''脸书第三方登录'''
            self.click_fb_loginBtn()
            self.thrid_fb_login(1)

        if tag == 2:
            '''谷歌第三方登录'''
            self.click_google_login_btn()
            self.thrid_gg_login(1)
        if tag == 3:
            self.click_appele_login_btn()
        if tag == 4:
            self.click_skip_btn()

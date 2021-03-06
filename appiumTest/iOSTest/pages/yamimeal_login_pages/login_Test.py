# coding=utf-8
from time import sleep
from appiumTest.iOSTest.common import basePage
from appiumTest.iOSTest.pages.yamimeal_login_pages.page_Elements import pageElements
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
    logout_userInfo = pageElements.user_click
    logout_btn_click = pageElements.logout_element
    no_try_alert = pageElements.no_Try_element
    off_alert_account_update = pageElements.off_update_account
    gg_third_login = pageElements.gg_thrid_login_element
    install_page_one = pageElements.frist_page_one
    sys_alert_location = pageElements.sys_location_alert
    langage_list = pageElements.languageList
    first_wx_btn = pageElements.first_wx_btn
    first_gg_btn = pageElements.first_gg_btn
    first_appleid_btn = pageElements.first_appleid_btn
    first_fb_btn = pageElements.first_fb_btn
    not_login_mypage = pageElements.not_login_my
    fb_account_login_element = pageElements.fb_Account_element
    fb_password_login_element = pageElements.fb_password_element
    fb_comfirm_login_element = pageElements.fb_comfirmBtn_confirm_element


    #截图
    imgs = []
    def first_wx_loginbtn(self):
        '''第一次安装时按钮元素'''
        self.by_AccessId(self.first_wx_btn).click()
    def first_fb_loginbtn(self):
        self.by_AccessId(self.first_fb_btn).click()
    def first_gg_loginbtn(self):
        self.by_AccessId(self.first_gg_btn).click()
    def first_appleid_loginbtn(self):
        self.by_AccessId(self.first_appleid_btn).click()
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
        try:
            """跳过"""
            self.iOS_By_ClassChain(self.skip_btn).click()
        except Exception as e:
            print('未找到元素{0}'.format(e))



    def frist_Install_app(self,item):
        '''
        第一次安装app
        :param item: 选择语言
        :return:
        '''

        try:
            sleep(5)
            self.by_AccessId(self.sys_alert_location).click()
            print('点击系统定位弹窗')
            sleep(3)
            self.alert_accept()
            print('点击系统级弹窗通过')
            sleep(3)
            self.iOS_By_ClassChain(self.install_page_one).click()

            sleep(3)
            self.iOS_By_ClassChain(self.langage_list[item]).click()
            print('点击选择语言item')
        except Exception as e:
            print('找不到元素已跳过{0}'.format(e))


    def thrid_wx_login(self,status):
        '''
        wx 第三方登录
        :param status: 从未登录过 1 已登录过
        :return:
        '''
        if status == 0:
            self.frist_Install_app(1)
            # 点击wx按钮
            self.click_wx_LoginBtn()
        else:
            sleep(2)
            # 点击协议
            self.clickPolicy()
            sleep(2)
            # 点击权限
            self.clickSysPermisson()
            # 点击wx按钮
            self.click_wx_LoginBtn()




    def thrid_fb_login(self,status):

        '''fb第三方登录'''
        '''
        status:0 从未登录过 1 已登录过
        '''
        if status == 0:
            # self.frist_Install_app(1)

            # self.first_fb_loginbtn()

            TouchAction(self.driver).tap(x=162,y=464).perform().release()
            sleep(10)
            self.by_AccessId(self.fb_aler_continue).click()
            sleep(5)
            self.iOS_By_ClassChain(self.fb_account_login_element).send_keys('13590926268')
            self.iOS_By_ClassChain(self.fb_password_login_element).send_keys('2226511aa')
            self.iOS_By_ClassChain(self.fb_comfirm_login_element).click()


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
        else:
            # self.click_fb_loginBtn()
            TouchAction(self.driver).tap(x=160,y=472).perform().release()
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
            self.frist_Install_app(1)
            # self.by_id('').sendKey('')
            # self.by_id('').sendKey('')
            # self.by_id('').click()
            sleep(10)
            # self.first_fb_loginbtn()
            TouchAction(self.driver).tap(x=252, y=464).perform().release()
            sleep(10)
            self.by_AccessId(self.fb_aler_continue).click()
            sleep(10)
            self.by_xpath(self.gg_third_login).click()
            sleep(12)
            self.iOS_By_ClassChain(self.yes_loca_element).click()
            sleep(5)
            self.alert()
            sleep(5)
            homeText = self.by_AccessId('首頁').text
            print(homeText)
            self.assert_Equal(homeText, u'首頁')
            print('谷歌登录用例通过(未登录过的状态)')
            sleep(4)
            self.logout()
        else:
            TouchAction(self.driver).tap(x=252, y=464).perform().release()
            sleep(3)
            self.alert_accept()
            sleep(5)
            # self.by_xpath(self.gg_third_login).click()
            # sleep(12)
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

    def user_page_login(self):
        '''跳過後到用戶頁面點擊登錄'''
        self.by_AccessId(self.logout_account).click()
        sleep(1)
        self.iOS_By_ClassChain(self.not_login_mypage).click()
        sleep(2)
        self.thrid_gg_login(1)


    def alert(self):
        '''处理登录之后有需要更新的alert'''
        sleep(10)
        try:
            self.by_AccessId(self.no_try_alert).click()
            sleep(10)
            TouchAction(self.driver).press(x=247, y=225).perform().release()
        except Exception as e:
            print('定位不到元素即将跳过{0}'.format(e))
            pass




    def login_approbject(self, tag):
        """
        :param tag: 传入需要的登录按钮的tag 0：wechat 1：fb 2：google 3：apple 4：skip
        :return:
        """
        if tag == 0:
            self.thrid_wx_login(0)
        if tag == 1:
            '''脸书第三方登录，并退出登录'''
            self.thrid_fb_login(0)
        if tag == 2:
            '''谷歌第三方登录，并退出登录'''
            self.thrid_gg_login(1)
        if tag == 3:
            self.click_appele_login_btn()

        if tag == 4:
            self.frist_Install_app(1)
            '''跳过按钮，回到首页'''
            self.click_skip_btn()
            print('点击跳过按钮')
            sleep(2)
            self.iOS_By_ClassChain(self.yes_loca_element).click()
            print('点击确认送货地址')
            sleep(5)
            try:
                self.alert()
                print('点击"没有找到你附近的商家"按钮')

            except Exception as e:
                pass
            sleep(3)

    def login_approbject_EN(self,tag):
        if tag == 0:
            self.thrid_wx_login(0)
        if tag == 1:
            self.thrid_fb_login(0)








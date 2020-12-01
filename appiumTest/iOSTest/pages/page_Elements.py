# coding=utf8
from appiumTest.AndroidTest.common import basePage


class pageElements(basePage.basePage):
    #弹框按钮元素
    alert_Countinue_element = '继续'
    alert_Cancel_element = '取消'
    #fb登录元素
    '''使用class chain'''
    fb_Account_element = '**/XCUIElementTypeTextField[`value == "手机号或邮箱"`]'
    fb_password_element = '**/XCUIElementTypeSecureTextField[`value == "Facebook 密码"`]'
    fb_comfirmBtn_confirm_element = '登录'
    #已有登录状态
    fb_existing_element = '继续'
    fb_existing_cancel_element = '取消'


    #google登录元素
    gg_Account_element = '电子邮件地址或电话号码'
    gg_next_element = '下一步'
    gg_Password_element = '输入您的密码'

    #确认地址
    yes_location_element = '**/XCUIElementTypeStaticText[`value == "是的，這是我的地址"`]'
    no_location_element = '**/XCUIElementTypeStaticText[`value == "不，我需要更改它"`]'

    #登入进去的第一个弹框:没有附近的上家
    goTry_element = '馬上試試'
    no_Try_element = '不了'

    #账户需要更新时弹框
    cancel_update_element = '//*[@id="screenshotContainer"]/div/div/div/div/div/div[14]'
    bindPhone = '**/XCUIElementTypeStaticText[`value == "綁定電話"`]'

    #点击用户信息
    user_click = '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]'
    #退出登录
    logout_element = '**/XCUIElementTypeStaticText[`value == "退出登錄"`]'
    #微信登录按钮
    '''使用accessiD'''
    wechat_btn_element = '/var/mobile/Containers/Data/Application/CC010926-CB01-42A2-A5E1-C834501BCFA3/Library/Bundlejs/bundle/assets/wechat.png'
    # google登录按钮
    google_btn_element = '/var/mobile/Containers/Data/Application/CC010926-CB01-42A2-A5E1-C834501BCFA3/Library/Bundlejs/bundle/assets/google.png '
    # fb登录按钮
    fb_btn_element = '/var/mobile/Containers/Data/Application/CC010926-CB01-42A2-A5E1-C834501BCFA3/Library/Bundlejs/bundle/assets/facebook.png'
    #苹果登录
    apple_btn_element = '/var/mobile/Containers/Data/Application/CC010926-CB01-42A2-A5E1-C834501BCFA3/Library/Bundlejs/bundle/assets/apple.png'
    #跳过按钮
    skip_btn_element = ''
    #确认按钮
    confirm_btn_element = ''
    #结果text
    login_result_element = ''

    #隐私协议accept按钮
    policy_element = ("com.proton.YamiMeal:id/btn_pos")
    #权限设定
    permission_element = ("com.proton.YamiMeal:id/dialog_confirm_btn")

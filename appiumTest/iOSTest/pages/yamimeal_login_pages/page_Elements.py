# coding=utf8
from appiumTest.AndroidTest.common import basePage


class pageElements(basePage.basePage):
    #新安装app
    frist_page_one = '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]'
    english = '**/XCUIElementTypeStaticText[`value == "English"`]'
    traditional = '**/XCUIElementTypeStaticText[`value == "繁體中文"`]'
    espain = '**/XCUIElementTypeStaticText[`value == "Español"`]'
    languageList = [english,traditional,espain]
    first_wx_btn = '/var/mobile/Containers/Data/Application/2EA57CCE-1201-4DAF-8807-6834C2A60806/Library/Bundlejs/bundle/assets/wechat.png'
    first_fb_btn = '/var/mobile/Containers/Data/Application/2EA57CCE-1201-4DAF-8807-6834C2A60806/Library/Bundlejs/bundle/assets/facebook.png'
    first_gg_btn = '/var/mobile/Containers/Data/Application/2EA57CCE-1201-4DAF-8807-6834C2A60806/Library/Bundlejs/bundle/assets/google.png'
    first_appleid_btn = '/var/mobile/Containers/Data/Application/2EA57CCE-1201-4DAF-8807-6834C2A60806/Library/Bundlejs/bundle/assets/apple.png'
    cn_select_bt = [first_wx_btn]


    #弹框按钮元素
    alert_Countinue_element = '继续'
    alert_Cancel_element = '取消'
    #fb登录元素
    '''使用class chain'''
    fb_Account_element = '**/XCUIElementTypeTextField[`value == "手机号或邮箱"`]'
    fb_password_element = '**/XCUIElementTypeSecureTextField[`value == "Facebook 密码"`]'
    fb_comfirmBtn_confirm_element = '**/XCUIElementTypeButton[`label == "登录"`]'
    #已有登录状态
    fb_existing_element = '继续'
    fb_existing_cancel_element = '取消'


    #google登录元素
    gg_Account_element = '电子邮件地址或电话号码'
    gg_next_element = '下一步'
    gg_Password_element = '输入您的密码'
    gg_thrid_login_element = '//XCUIElementTypeOther[@name=\"登录 - Google 帐号\"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]'

    #确认地址
    yes_location_element = '**/XCUIElementTypeStaticText[`value == "是的，這是我的地址"`]'
    no_location_element = '**/XCUIElementTypeStaticText[`value == "不，我需要更改它"`]'

    #登入进去的第一个弹框:没有附近的上家
    goTry_element = '馬上試試'
    no_Try_element = '不了'
    off_update_account = '//XCUIElementTypeApplication[@name="Yamimeal"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeStaticText'

    #账户需要更新时弹框
    cancel_update_element = '//*[@id="screenshotContainer"]/div/div/div/div/div/div[14]'
    bindPhone = '**/XCUIElementTypeStaticText[`value == "綁定電話"`]'

    #点击用户信息
    user_click = '**/XCUIElementTypeStaticText[`value == "用戶信息"`]'
    #未登錄狀態下我的頁面 用戶信息
    not_login_my = '**/XCUIElementTypeStaticText[`value == "登錄"`]'
    #退出登录
    logout_element = '**/XCUIElementTypeStaticText[`value == "退出登錄"`]'
    #微信登录按钮
    '''使用accessiD'''
    wechat_btn_element = '/var/mobile/Containers/Data/Application/3A2A6BDA-6C2C-42CA-82FA-5CB9DEE5D32C/Library/Bundlejs/bundle/assets/wechat.png'
    # google登录按钮
    google_btn_element = '/var/mobile/Containers/Data/Application/CC010926-CB01-42A2-A5E1-C834501BCFA3/Library/Bundlejs/bundle/assets/google.png'
    # fb登录按钮
    fb_btn_element = '/var/mobile/Containers/Data/Application/CC010926-CB01-42A2-A5E1-C834501BCFA3/Library/Bundlejs/bundle/assets/facebook.png'
    #苹果登录
    apple_btn_element = '/var/mobile/Containers/Data/Application/CC010926-CB01-42A2-A5E1-C834501BCFA3/Library/Bundlejs/bundle/assets/apple.png'

    #以上元素有变化，使用上一层元素
    '''使用ios class chain'''

    wechat_btn_XY_element = ''


    #跳过按钮
    '''classChain元素'''
    skip_btn_element = '**/XCUIElementTypeStaticText[`value == "跳過"`]'
    #确认按钮
    confirm_btn_element = ''
    #结果text
    login_result_element = ''

    #隐私协议accept按钮
    policy_element = ("com.proton.YamiMeal:id/btn_pos")
    #权限设定
    permission_element = ("com.proton.YamiMeal:id/dialog_confirm_btn")
    #系统定位弹窗
    sys_location_alert = '使用App时允许'
# ------------------------------------------------------tabbar按钮---------------------------------------------#

    #点击首页
    home_click_btn = '首頁'
    #點擊訂單
    order_click_btn = '訂單'
    # 點擊購物車
    shoppingCar_click_btn = '購物車'
    #點擊消息
    msg_click_btn = '信息'
    # 点击账户
    account_click_btn = '帳戶'
# ------------------------------------------------------賬戶页面元素---------------------------------------------#
    #收藏
    account_collection_btn = '**/XCUIElementTypeStaticText[`value == "收藏"`]'
    #砍单跟买
    account_kandan_btn = '**/XCUIElementTypeStaticText[`value == "砍單跟買"`]'
    #晒单
    accoubt_shaidan_btn = '**/XCUIElementTypeStaticText[`value == "曬單"`]'
    '''以下使用class chain'''
    #商家积分
    account_merch_btn = '**/XCUIElementTypeOther[`label == ",,"`][1]'
    #非现金抵用券
    account_notCash_btn = '**/XCUIElementTypeOther[`label == ",,"`][2]'
    #信用卡
    account_credit_btn = '**/XCUIElementTypeOther[`label == ",,"`][3]'
    #我的地址
    account_myAdress_btn = '**/XCUIElementTypeOther[`label == ",,"`][4]'
    #语言
    account_langague_btn = '**/XCUIElementTypeOther[`label == ",,"`][5]'
    #需要帮助?
    account_CanHelp_btn = '**/XCUIElementTypeOther[`label == ",,"`][6]'





#------------------------------------------------------buy 页面元素---------------------------------------------#


    #出现 感谢你最近的订单弹窗元素
    buy_close_btn = '关闭'
    #收藏也面的item商铺
    '''ios class chain'''
    #分两个状态，一个滚动视图的元素，一只原始状态
    isScrollView = '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeTable/XCUIElementTypeOther/XCUIElementTypeImage'
    categroy_item = '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView/XCUIElementTypeOther'
    categroy_item_suffix = '/XCUIElementTypeOther[1]/XCUIElementTypeImage'
    your_collection_item = '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage'
# ------------------------------------------------------结账页面元素---------------------------------------------#
    goods_smallNum_text = '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeScrollView/XCUIElementTypeOther[4]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther'



#------------------------------------------------------商品页面元素---------------------------------------------#
    #添加商品元素"+"
    add_Goods_btn = '**/XCUIElementTypeStaticText[`value == ""`]'
    #结账
    check_out_btn = '**/XCUIElementTypeStaticText[`value == "去結賬"`]'
    #结账页面
    next_step_btn = '**/XCUIElementTypeStaticText[`value == "下一步"`]'
    #下单
    placeOrder_btn = '**/XCUIElementTypeStaticText[`value == "下單"`]'
    #订单确认text
    order_comfirm_text = '**/XCUIElementTypeStaticText[`value == "訂單確認"`][1]'
    #订单里返回按钮
    pop_btn = '"//XCUIElementTypeApplication[@name=\"Yamimeal\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeOther/XCUIElementTypeStaticText[1]"'
    #订单详情
    order_detail_btn = '訂單詳情'

#------------------------------------------------------当前订单页面---------------------------------------------#
    #当前订单 待处理TEXT
    order_Wait_Text = '**/XCUIElementTypeStaticText[`value == "訂單待處理"`]'
    #订单准备中
    order_readying_Text = '**/XCUIElementTypeStaticText[`value == "訂單準備中"`]'
    #准备好送货
    order_Delivery_Text = '**/XCUIElementTypeStaticText[`value == "準備好送貨"`]'
    #送貨中
    order_Deliverying_Text = '**/XCUIElementTypeStaticText[`value == "訂單送貨中"`]'
    #在線溝通
    online_communication_btn = '在線溝通'
    #已收貨按鈕
    have_goods_btn = '**/XCUIElementTypeOther[`label == "已收貨"`]'










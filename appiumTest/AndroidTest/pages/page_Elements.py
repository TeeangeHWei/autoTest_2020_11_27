# coding=utf8
from appiumTest.AndroidTest.common import basePage


class pageElements(basePage.basePage):
    #微信登录按钮
    wechat_btn_element = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView'
    # google登录按钮
    google_btn_element = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout[3]/android.widget.ImageView'
    # 微信登录按钮
    fb_btn_element = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.ImageView'
    #苹果登录
    apple_btn_element = ''
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



class iOSPageElements():
    wechat_btn_element = ''
    google_btn_element = ''
    fb_btn_element = ''
    apple_btn_element = ''
    skip_btn_element = ''
    confirm_btn_element = ''
    login_result_element = ''
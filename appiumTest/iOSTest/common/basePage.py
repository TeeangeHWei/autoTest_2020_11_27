# coding=utf-8


class basePage(object):
    def __init__(self,driver):
        self.driver = driver
    # 元素id
    def by_id(self,loca):
        try:
            return self.driver.find_element_by_id(loca)
        except Exception as e:
            print('未找到元素{0}'.format(e))
    # 元素xpath
    def by_xpath(self,loca):
        try:
            return self.driver.find_element_by_xpath(loca)
        except Exception as e:
            print('未找到元素{0}'.format(e))
    # name 元素
    def by_name(self,loca):
        try:
            return self.driver.find_element_by_name(loca)
        except Exception as e:
            print('未找到元素{0}'.format(e))

    # accessibilityId
    def by_AccessId(self, loca):
        try:
            return self.driver.find_element_by_accessibility_id(loca)
        except Exception as e:
            print('未找到元素{0}'.format(e))

    def iOS_By_ClassChain(self,loca):
        try:
            return self.driver.find_element_by_ios_class_chain(loca)
        except Exception as e:
            print('未找到元素{0}'.format(e))

    def by_seletor(self,loca):
        try:
            return self.driver.find_element_by_css_selector(loca)
        except Exception as e:
            print('未找到元素{0}'.format(e))


    def assert_Equal(self,a,b):
        '''断言equal判断相等'''
        try:
            return self.caseAssert.assertEqual(a,b)
        except Exception as e:
            print('未找到断言内容{0}'.format(e))

    def assert_Not_Equal(self,a,b):
        '''断言equal判断相等'''
        try:
            return self.caseAssert.assertNotEqual(a,b)
        except Exception as e:
            print('未找到断言内容{0}'.format(e))

    def alert_accept(self):
        '''允许所有弹窗'''
        try:
            return self.driver.switch_to.alert.accept()
        except Exception as e:
            print('未找到断言内容{0}'.format(e))


    def implicitly_wait(self,time):
        try:
            return self.driver.implicitly_wait(time)
        except Exception as e:
            print('超时失败')





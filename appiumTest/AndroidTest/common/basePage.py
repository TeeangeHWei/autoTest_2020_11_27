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






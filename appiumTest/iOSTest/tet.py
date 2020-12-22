# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 4:22 下午
# @Author  : Cyrus
# @File    : tet.py
# @Software: PyCharm
# @Function :
import numbers
import re
list1 = ['結賬', '小費', '到店自提', '商家配送', 'broc storebroc storebroc storebroc storebroc sbroc storebroc st', '$ 170.00', '$ 88.06', '12 商品', '$ 88.06', '下一步', '-$ 102.00', '$ 0.00', '司機小費，你所支付的小費100%歸司機所有。', '配送備注', '商品小計: ', '免費', '合計: ', '60% OFF', '$ 12.26', '小费', '訂單要求', '支付方式', '無小費', '$ 1', '$ 2', '$ 4', '其他', '\ue651', '放在門口', '門口交收', '門外交收', '5', '/150', '$ 1.00', '$ 6.80', '配送费', 'China, Guangdong Province, Zhongshan, Huoju Road, 中山火炬高技术产业开发区', '刪除', '刪除', '稅 ', '$ 0.99', '-$ 0.99', '12/22', 'Tue', '14:02 - 15:59', '测1', '测2', '包裝費', '商家服務費', '\ue651', '信用卡', '\ue651', '\ue651', '$ 10.00', '$ 20.00', '\ue782', 'Yamimeal 服務費', 'Yamimeal 服務費', '\ue651', '\ue651', '\ue651', '\ue782', '\ue782', '7', '5', '\ue846', '\ue847', '\ue846', '\ue847']
list2 = ['結賬', '小費', '到店自提', '商家配送', 'broc storebroc storebroc storebroc storebroc sbroc storebroc st', '$ 270.00', '$ 138.86', '20 商品', '$ 138.86', '下一步', '-$ 162.00', '$ 0.00', '司機小費，你所支付的小費100%歸司機所有。', '配送備注', '商品小計: ', '免費', '合計: ', '60% OFF', '$ 19.06', '小费', '訂單要求', '支付方式', '無小費', '$ 1', '$ 2', '$ 4', '其他', '\ue651', '放在門口', '門口交收', '門外交收', '5', '/150', '$ 1.00', '$ 10.80', '配送费', 'China, Guangdong Province, Zhongshan, Huoju Road, 中山火炬高技术产业开发区', '刪除', '刪除', '稅 ', '$ 0.99', '-$ 0.99', '12/22', 'Tue', '16:00 - 16:59', '测1', '测2', '包裝費', '商家服務費', '\ue651', '信用卡', '\ue651', '\ue651', '$ 10.00', '$ 20.00', '\ue782', 'Yamimeal 服務費', 'Yamimeal 服務費', '\ue651', '\ue651', '\ue651', '\ue782', '\ue782', '13', '7', '\ue846', '\ue847', '\ue846', '\ue847']
list_01 = []
# for i,value in enumerate(list):
#     # print(i)
#     # print(value)
#     list_01.append(value)
#
# print(list_01)
# str = str(list_01[1])
# print(str)
# replace = str.replace('$ ','')
# print(replace)
for i in list1:
    ss = re.sub("[^0-9.]","",i)
    if len(ss)>0:
        list_01.append(ss)
    else:
        print('weikong')

    print(ss)
print(list_01)
for index,value in enumerate(list_01):
    print(index,value)
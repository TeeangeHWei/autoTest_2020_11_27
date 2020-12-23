# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 4:22 下午
# @Author  : Cyrus
# @File    : tet.py
# @Software: PyCharm
# @Function :
import numbers
import re
from decimal import Decimal


def packing_Tax(packtips, packtax) -> str:
    '''

    :param packTips: 包装费
    :param packTax: 包装税
    :return:
    '''
    packingTax = Decimal(packtips) + Decimal(packtax)
    str1 = str(packingTax.quantize(Decimal('0.00')))
    return str1

ss = (packing_Tax(2.32,3.11))
print(ss)


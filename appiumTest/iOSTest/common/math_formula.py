# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 9:31 上午
# @Author  : Cyrus
# @File    : math_formula.py
# @Software: PyCharm
# @Function : 计算公式
import os
import shutil
from decimal import Decimal


class math_mula():
    '''
            商家收费：商家服务费		10%
            包装费		$1
            配送费		$1
            优惠		60%
TAx
            商品税		10%
            包装税		70%
            配送税		70%
            商家服务税	70%


        商家服务费 = 商品小计 - 优惠 * 商家服务费
                   [$20-($20*60)] *10%

        商家服务费税 = 商品小计 - 优惠 * 商家服务费*商家服务费税
                     [$20-($20*60%)] *10% *70%

        商品税 = 商品小计 - 优惠 * 商品税
                    [$20-($20*60%)] *10%

        包装税 = 包装费 * 包装税
               $1 *70%

        配送税 = 配送费 * 配送税
              $1 *70%

    '''
    #商家服务费
    def merch_service_tips(self,goodsnum,discount,merchtips)->str:
        '''

        :param goodsNum: 商品小计
        :param discount: 优惠
        :param merchTips: 商家服务费
        :return:
        '''
        total_result_Decimal = (Decimal(goodsnum) - Decimal(goodsnum*discount)) *Decimal(merchtips)
        total_result = str(total_result_Decimal.quantize(Decimal('0.00')))

        return total_result
    #商家服务费税
    def merch_service_tax(self,goodsnum,discount,merchtips,tax) -> str:
        '''

        :param goodsNum: 商品小计
        :param discount: 优惠
        :param merchTips: 商家服务费
        :param tax: 税费
        :return:
        '''
        merch_tax_Decimal = (Decimal(goodsnum)-Decimal((goodsnum*discount)))*Decimal(merchtips)*Decimal(tax)
        merch_tax = str(merch_tax_Decimal.quantize(Decimal('0.00')))
        return merch_tax

    #商品税
    def merch_Goods_Tax(self, goodsnum, discount, goodstax) -> str:
        '''

        :param goodsNum: 商品小计
        :param discount: 优惠
        :param goodsTax: 商品税
        :return:
        '''

        merchTax = Decimal(goodsnum) - (Decimal(goodsnum*discount)) * Decimal(goodstax)
        merch_Tax = str(merchTax.quantize(Decimal('0.00')))
        return merch_Tax

    #包装税
    def packing_Tax(self,packtips,packtax) -> str:
        '''

        :param packTips: 包装费
        :param packTax: 包装税
        :return:
        '''
        packingTax = Decimal(packtips) * Decimal(packtax)
        str1 = str(packingTax.quantize(Decimal('0.00')))
        return str1

    #配送税
    def delivery_Tax(self,deliverytips,deliverytax) -> str:
        '''

        :param deliveryTips: 配送费
        :param deliveryTax: 配送税
        :return:
        '''
        deliveryTax = Decimal(deliverytips) * Decimal(deliverytax)
        delivery_tax_total = str(deliveryTax.quantize(Decimal('0.00')))
        return delivery_tax_total

    def Tax(self,deliverytax,packtax,goodstax,merchtax) -> str:

        tax_total = deliverytax + packtax + goodstax + merchtax
        return tax_total

    def del_file(filepath):
        """
        删除某一目录下的所有文件或文件夹
        :param filepath: 路径
        :return:
        """
        del_list = os.listdir(filepath)
        for f in del_list:
            file_path = os.path.join(filepath, f)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
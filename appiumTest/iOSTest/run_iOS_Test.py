#coding=utf-8
import unittest,os
from appiumTest.iOSTest.testCases.TestCase_yamimeal_login import login_Test_Case
from unittestreport import TestRunner
import pytest
cur_Path = os.path.dirname(os.path.realpath(__file__))
case_Path = os.path.join(cur_Path,'testcases')
report_path = os.path.join(cur_Path, 'reports')

if __name__ == '__main__':
    pytest.main(['-s', '-v', './testCases/TestCase_yamimeal_buy/Test_yamimeal_buy.py', '--alluredir', './temp', '--reruns', '1'])
    os.system('allure generate ./temp -o ./report --clean')



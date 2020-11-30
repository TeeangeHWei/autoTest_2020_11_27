#coding=utf-8
import unittest,os
from appiumTest.AndroidTest.common.HwTestReport import HTMLTestReportEN
from appiumTest.AndroidTest.testCases import login_Test_Case
cur_Path = os.path.dirname(os.path.realpath(__file__))
case_Path = os.path.join(cur_Path,'testcases')
report_path = os.path.join(cur_Path, 'reports')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suiteCase01 = unittest.TestLoader().loadTestsFromTestCase(login_Test_Case.testYamimealLogin)
    suite.addTest(suiteCase01)
    with open('TESTREPORT.html', 'wb') as report:
        runner = HTMLTestReportEN(stream=report,verbosity=2,images=True,title='测试',description='带截图',tester='cyrus')
        runner.run(suite)







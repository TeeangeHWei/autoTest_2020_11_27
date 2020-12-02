#coding=utf-8
import unittest,os
from appiumTest.iOSTest.common import HwTestReport
from appiumTest.iOSTest.testCases import login_Test_Case
from unittestreport import TestRunner
cur_Path = os.path.dirname(os.path.realpath(__file__))
case_Path = os.path.join(cur_Path,'testcases')
report_path = os.path.join(cur_Path, 'reports')

if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suiteCase01 = unittest.TestLoader().loadTestsFromTestCase(login_Test_Case.testYamimealLogin)
    # suite.addTest(suiteCase01)
    # with open('./iOS_yamimeal.html', 'wb') as report:
    #     runner = HwTestReport.HTMLTestReport(stream=report,
    #                                          verbosity=2,
    #                                          images=True,
    #                                          title='loginTest',
    #                                          description='iOS_yamimeal',
    #                                          tester='cyrus'
    #                                          )
    #     runner.run(suite)
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(login_Test_Case.testYamimealLogin)

    runner = TestRunner(suite=suite,filename='yamimeal.html',title='登录测试报告',tester='CYRUS',desc='yamimealTestReport')
    # runner.run()
    runner.rerun_run(count=3,interval=2)


#coding=utf-8
import unittest,os
from appiumTest.AndroidTest.common import HwTestReport
from appiumTest.AndroidTest.testCases import login_Test_Case
cur_Path = os.path.dirname(os.path.realpath(__file__))
case_Path = os.path.join(cur_Path,'testcases')
report_path = os.path.join(cur_Path, 'reports')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suiteCase01 = unittest.TestLoader().loadTestsFromTestCase(login_Test_Case.testYamimealLogin)
    suite.addTest(suiteCase01)
    with open('./123.html', 'wb') as report:
        runner = HwTestReport.HTMLTestReport(stream=report,
                                             verbosity=2,
                                             images=True,
                                             title='test',
                                             description='jietu',
                                             tester='cyrus'
                                             )
        runner.run(suite)







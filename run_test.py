import os
import unittest
import time
from HTMLTestRunner import HTMLTestRunner

current = os.path.dirname(__file__)
cases_path = os.path.join(current, 'test_cases')    # 用例地址
report_path = os.path.join(current, 'report')   # 报告地址
html_path = os.path.join(report_path, 'report_%s.html'%time.strftime('%Y_%m_%d_%H_%M_%S'))
# 用例集
discover = unittest.defaultTestLoader.discover(start_dir=cases_path, pattern='*_case.py', top_level_dir=cases_path)

main_suite = unittest.TestSuite()   # 创建主集合
main_suite.addTest(discover)    # 增加用例集

file = open(html_path, 'wb')    # 创建html文件
html_runner = HTMLTestRunner(stream=file, title='禅道UI自动化测试项目', description='自动化测试，包含大部分场景')     # 调用html报告模板
html_runner.run(main_suite)


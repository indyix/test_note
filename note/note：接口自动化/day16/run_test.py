import unittest
import sys
import os.path
from HTMLTestRunnerNew import HTMLTestRunner
import test_Login
sys.path.append(os.path.abspath(__file__))

loader = unittest.TestLoader()
test_suit = unittest.TestSuite()
test_suit.addTests(loader.loadTestsFromModule(test_Login))

if __name__ == '__main__':
	with open("report.html", "wb") as rep:
		runner = HTMLTestRunner(
		rep,title="day16作业", description="封装读取数据的操作的文件：exhander.py；用例数据：cases.xlsx,；用例：test_login.py", tester="007"
	)
		runner.run(test_suit)


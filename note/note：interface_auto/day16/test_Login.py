import unittest
import ddt
import exhander

# ============测试函数=================
def login(username=None, password=None):
	"""登录"""
	if (not username) or (not password):
		# 用户名或者密码为空
		return {"msg": "empty"}

	if username == 'yuz' and password == '123456':
		# 正确的用户名和密码
		return {"msg": "success"}

	return {"msg": "error"}


# =================测试数据==============
# cases = [
# 	{'case_id': 1, 'module': '登录', 'title': '登录失败', 'data': '{"username":"231","password":"123456"}', 'expected': '{"msg": "error"}'},
# 	{'case_id': 2, 'module': '登录', 'title': '登陆成功', 'data': '{"username":"yuz","password":"123456"}', 'expected': '{"msg": "success"}'},
# 	{'case_id': 3, 'module': '登录', 'title': '登录失败', 'data': '{"username":None,"password":"123456"}', 'expected': '{"msg": "empty"}'}
# ]

cases = exhander.ExcelHandler("cases.xlsx").read_data("Sheet1")
# print(cases)

# ================测试用例===============
@ddt.ddt
class TestLogin(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print("======执行测试用例======")
	@classmethod
	def tearDownClass(cls):
		print("======测试结束======")

	@ddt.data(*cases)
	def test_login(self,cases_info):  # cases 取*cases中的数据
		username = eval(cases_info["data"])["username"]
		password = eval(cases_info["data"])["password"]
		expect_response = cases_info["expected"]
		actual_response = login(username,password)
		self.assertTrue(actual_response,expect_response)




# """登录功能的测试用例。"""
# import pytest
#
# from data.login_data import login_error, login_success, login_invalid
# from middleware.handler import Handler
# from middleware.pages.login import LoginPage
# from middleware.pages.index import IndexPage
#
# # 读取 Excel 当中的数据
# data_error = Handler.excel.read_data("login_error")
# data_success = Handler.excel.read_data("login_success")
#
#
# class TestLogin():
#     """登录功能的测试类"""
#
#     @pytest.mark.error_test
#     @pytest.mark.parametrize("test_info", login_error)
#     def test_login_error(self, test_info, driver):
#         """"""
#         # 先初始化页面，测试用到的页面
#         login_page = LoginPage(driver)
#
#         # 测试步骤：页面的行为，PO当中的方法
#         actual = login_page.get().login_fail(
#             username=test_info["username"],
#             password=test_info["password"],
#         ).get_error_message()
#
#
#         # 实际结果和预期结果比对
#         # 日志记录，错误处理
#         try:
#             assert actual == test_info["expected"]
#         except AssertionError as e:
#             Handler.logger.error("测试用例不通过")
#             raise e
#
#     @pytest.mark.parametrize("test_info",login_success)
#     @pytest.mark.success
#     def test_login_success(self, test_info, driver):
#         """登录成功用例
#
#     测试步骤：
#     1， 登录页面输入用户名
#     2， 登录页面输入密码
#     3， 登录页面点击登录
#     4， 首页页面获取用户信息
#
#         """
#         login_page = LoginPage(driver)
#
#         actual = login_page.get().login_success(
#             username=test_info["username"],
#             password=test_info["password"],
#         ).get_account_name()
#
#         try:
#             assert actual == test_info["expected"]
#         except AssertionError as e:
#             Handler.logger.error("测试用例不通过")
#             raise e
#
#     @pytest.mark.parametrize("test_info", login_invalid)
#     def test_login_invalid(self, test_info, driver):
#         """登录未授权.
#
#         测试步骤：
#             1， 登录页面输入用户名
#             2， 登录页面输入密码
#             3， 登录页面点击登录
#             4， 登录页面获取未授权信息
#         """
#         login_page = LoginPage(driver)
#         actual = login_page.get().login_fail(
#             username=test_info["username"],
#             password=test_info["password"]
#         ).get_invalid_message()
#         try:
#             assert actual == test_info["expected"]
#         except AssertionError as e:
#             Handler.logger.error("测试用例不通过")
#             raise e

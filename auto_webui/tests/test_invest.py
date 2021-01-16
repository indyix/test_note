# """投资用例"""
# from middleware.pages.index import IndexPage
#
#
# # def test_invest_not_10_times(login):
# #     """投资不是 10 的整数倍。
# #
# #     测试步骤：
# #         1， 前置条件：登录（）
# #             - 有钱
# #             - 有标可以投
# #             可以通过接口，可以通过修改数据库，可以手工充值，可以手工加标。
# #             - 每次你在执行之前都自动充值或者加一次标
# #             - 一次性满足条件
# #
# #         2， 首页：点击抢投标
# #         3， 投标详情页：输入投标金额
# #         4， 投标详情页：获取结果
# #     """
# #     driver = login  # 登录 ==0.4=》 首页
# #     actual = IndexPage(driver).click_invest_btn().write_money(
# #         1).get_error_msg()
# #     assert actual == '请输入10的整数倍'
#
#
# def test_invest_success(login):
#     """投资成功用例.
#
#     步骤：
#         1， 首页，点击强投标
#         （获取投标之前的余额）
#         2， 详情页，输入投标金额
#         3， 详情页，点击投标
#         4， 断言出现投标成功
#         5， 详情页，点击查看并激活
#         6， 用户界面断言余额
#     """
#     driver = login
#     invest_page = IndexPage(driver).click_invest_btn()
#     before_money = invest_page.get_money()
#
#     success_msg = invest_page.write_money(
#         100).click_invest_btn().get_success_msg()
#     assert  "投标成功" in success_msg
#
#     after_money = invest_page.click_active_btn().get_balance()
#
#     from decimal import Decimal
#     assert Decimal(before_money) - Decimal(str(100)) == Decimal(after_money)
#
#
#
#
#
#
#

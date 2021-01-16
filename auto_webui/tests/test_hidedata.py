"""登录功能的测试用例。"""
from time import sleep

import pytest

from data.login_data import login_error, login_success, login_invalid
from middleware.handler import Handler
from middleware.pages.pf_sen_guo_cc import LoginPage
from middleware.pages.boss_login import BossLoginPage
from middleware.pages.center import CenterPage
from middleware.pages.boss_index import BossIndex

# # 读取 Excel 当中的数据
# data_error = Handler.excel.read_data("login_error")
# data_success = Handler.excel.read_data("login_success")


@pytest.mark.hidedata
def test_hidedata(driver):
    # 先初始化页面，测试用到的页面
    cc_page = LoginPage(driver)

    # 测试步骤：页面的行为，PO当中的方法
    actual = cc_page.get().click_into_boss_login_page().login_success(17386049001,123456).click_to_pfshops_list().click_into_shop("亚特兰蒂斯").hide_indexdata()
    sleep(25)

# test_hidedata()

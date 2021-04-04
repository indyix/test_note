import pytest

from data.tiku_data import select_tiku_data
from pages.nav import NavPage


@pytest.mark.parametrize("test_info", select_tiku_data)
def test_tiku(test_info, login):
    """测试题库。

    步骤：
        1， 前置条件登录
        2， 在导航叶念点击题库页面
        2， 在题库页面（列表）点击题库标题（逻辑思维题）
        //android.widget.TextView[contains(@text, '逻辑思维题')]
        3， 在题库页面（详情）定位题库标题  com.lemon.lemonban:id/category_title
    """
    driver = login
    actual = NavPage(driver).click_tiku().\
        find_and_click_tiku(test_info["tiku_name"]).\
        get_title()
    assert actual == test_info["expected"]
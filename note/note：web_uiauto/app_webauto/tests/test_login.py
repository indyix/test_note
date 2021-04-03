
"""
在 app 当中，如何去设置不同的 PageObject, 是根据功能是否匹配。
如何有很多子页面，我们会把功能和操作比较多，比较复杂的子页面单独封装成一个另外的类

UserPage --> LoginPage


"""
import pytest

from data.login_data import login_error_data
from pages.nav import NavPage


@pytest.mark.parametrize("test_info", login_error_data)
def test_login_fail(test_info, driver):
    """
    测试步骤：
        0， 导航页面点击我的柠檬
        1， 进入登录页面
        2， 在登录页面点击头像 （点击头像页面和用户名密码输入页面可以被当成一个页面。
            都和某个功能相关，用户管理功能
        ）
        3， 在登录页面输入用户名和密码登录
        4， 断言。


        1, 手工执行流程，得到所有的 locator, 复制在这
        2， 封装页面行为， PO
    """
    actual = NavPage(driver).\
        click_my().\
        click_avatar().\
        login_fail(test_info["username"], test_info["pwd"]).\
        get_error_msg()
    assert actual == test_info["expected"]


from appium.webdriver.common.mobileby import MobileBy

from common.basepage import BasePage
from pages.home import HomePage


class UserPage(BasePage):

    # 头像元素定位器
    avatar_locator = (MobileBy.ID, 'com.lemon.lemonban:id/fragment_my_lemon_avatar_layout')

    # 用户登录定位器
    user_locator = (MobileBy.ID, 'com.lemon.lemonban:id/et_mobile')
    pwd_locator = (MobileBy.ID, 'com.lemon.lemonban:id/et_password')
    login_btn_locator = (MobileBy.ID, 'com.lemon.lemonban:id/btn_login')

    def click_avatar(self):
        """返回 self, 还是其他页面，取决于
        你的登录页面是否设置独立的页面对象PO
        """
        self.click(self.avatar_locator)
        return self

    def login_fail(self, username, pwd):
        """登录失败"""
        self.write(self.user_locator, username)
        self.write(self.pwd_locator, pwd)
        self.click(self.login_btn_locator)
        return self

    def login_success(self, username, pwd):
        """登录成功"""
        self.write(self.user_locator, username)
        self.write(self.pwd_locator, pwd)
        self.click(self.login_btn_locator)
        return HomePage(self.driver)

    def get_error_msg(self):
        """获取登录失败的错误信息"""
        # 定位toast弹框
        # 获取弹框的本本
        el = self.get_toast()
        return el.text


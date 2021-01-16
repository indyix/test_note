# """登录页面"""
# from common.selenium_handler import BasePage
# from middleware.pages.index import IndexPage
# from selenium.webdriver.common.by import By
#
# from middleware.handler import Handler
#
#
# class LoginPage(BasePage):
#     title = "欢迎登录"
#
#     URL = Handler.yaml["host"] + "/Index/login.html"
#     # locators
#     # login_btn_locator = ("name", "btn-special")
#     # 登录按钮元素定位
#     # TODO: 复制了代码，一定要每个字都检查清楚。
#     login_btn_locator = (By.CLASS_NAME, "btn-special")
#     username_locator = (By.NAME, "phone")
#     pwd_locator =  (By.NAME, "password")
#     error_msg_locator = (By.CLASS_NAME, "form-error-info")
#
#     # 没有通过授权元素定位方式
#     invalid_msg_locator = (By.CLASS_NAME, "layui-layer-content")
#
#
#     def get(self):
#         """访问页面"""
#         self.driver.get(self.URL)
#         return self
#
#     def login_fail(self, username, password):
#         """登录行为。
#
#         详细介绍这个函数是做什么用的，怎么使用，传什么参数，没个参数的意思，
#
#         最后的返回值是什么，返回值代表什么意思。
#
#         >>>oginPage(driver).login("yuz", "123")
#         """
#
#         self.enter_username(username)
#         self.enter_password(password)
#
#         # self.driver.find_element(*self.login_btn_locator).click()
#         self.find_element(self.login_btn_locator).click()
#         return self
#
#     def login_success(self, username, password):
#         self.enter_username(username)
#         self.enter_password(password)
#
#         self.find_element(self.login_btn_locator).click()
#         return IndexPage(self.driver)
#
#     def enter_username(self, username):
#         """输入用户名"""
#
#         self.find_element(self.username_locator).send_keys(username)
#         return self
#
#     def enter_password(self, pwd):
#         """输入用户名"""
#         self.find_element(self.pwd_locator).send_keys(pwd)
#         return self
#
#     def get_error_message(self):
#         """获取登录不成功的错误信息"""
#         return self.find_element(self.error_msg_locator).text
#
#     def get_invalid_message(self):
#         """获取登录未授权的信息.
#
#         注意事项：通过隐式等待是可以等待元素被加载。
#         但是，元素被加载并不表示里面的动态文本内容能被获取到。
#         1， 通过显示等待：visible,
#         2, text文本定位，显示等待
#         3， 强制等待， 把握好时间。
#         """
#         # 显示等待进行元素定位。
#         # el = WebDriverWait(self.driver, timeout=20, poll_frequency=0.5).until(
#         #     expected_conditions.visibility_of_element_located( self.invalid_msg_locator.values() )
#         # )
#         el = self.wait_element_visible(self.invalid_msg_locator)
#         return el.text
#
#
#

# from selenium.webdriver.common.by import By
#
# from middleware.handler import Handler
# from common.selenium_handler import BasePage
# from middleware.pages.invest import InvestPage
#
#
# class IndexPage(BasePage):
#     title = "互联网金融平台"
#
#     URL = Handler.yaml["host"] + "/index.html"
#     # 获取用户信息
#     user_locator = (By.XPATH, '//a[@href="/Member/index.html"]')
#     # 点击投标
#     invest_btn_locator = (By.CLASS_NAME, "btn-special")
#
#     # def __init__(self,driver):
#     #     super().__init__(driver)
#     #     # 其他的出事话
#
#     def get(self):
#         self.driver.get(self.URL)
#         return self
#
#     def get_account_name(self):
#         """获取用户名"""
#         el = self.driver.find_element(*self.user_locator)
#         return el.text
#
#     def click_invest_btn(self):
#         """点击抢投标"""
#         self.driver.find_element(*self.invest_btn_locator).click()
#         return InvestPage(self.driver)

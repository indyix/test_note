"""登录页面"""
from common.selenium_handler import BasePage
from selenium.webdriver.common.by import By
from middleware.handler import Handler
from middleware.pages.boss_login import BossLoginPage
from middleware.pages.cashier_login import CashierLoginPage


class LoginPage(BasePage):
    title = "微主页"

    URL = Handler.yaml["host"]["pf"]
    # locators
    # 登录页面进入按钮
    login_btn_boss = (By.XPATH, "//p[text()='批发后台登录']")
    login_btn_cashier = (By.CLASS_NAME, "cashier-login")

    def get(self):
        """访问页面"""
        self.driver.get(self.URL)
        return self

    def click_into_boss_login_page(self):
        """选择进入后台登录页。return:后台登录页面实例对象
        """
        self.find_element(self.login_btn_boss).click()
        return BossLoginPage(self.driver)

    def click_into_cashier_login_page(self):
        """选择进入收银台登录页。return：收银台登录页面实例对象
        """
        self.find_element(self.login_btn_cashier).click()
        return CashierLoginPage(self.driver)




from selenium.webdriver.common.by import By
from common.selenium_handler import BasePage
from middleware.pages.user import UserPage


class InvestPage(BasePage):
    title = "项目详情"
    # 输入用户金额
    invest_input_locator = (By.CLASS_NAME, "form-control")

    # 投标按钮
    invest_btn_locator = (By.CLASS_NAME, 'btn-special')

    # 投标成功信息
    success_msg_locator = (By.XPATH, "//div[@class='layui-layer-content']//div[contains(@class, 'capital_font1')]")

    # 查看激活
    active_btn_locator = (By.XPATH, "//div[@class='layui-layer-content']//button")

    def write_money(self, money):
        """输入用户金额"""
        self.driver.find_element(*self.invest_input_locator).send_keys(money)
        return self

    def get_error_msg(self):
        """不是10的整数倍错误信息"""
        el = self.driver.find_element(*self.invest_btn_locator)
        return el.text

    def get_success_msg(self):
        """获取投标成功信息"""
        el = self.wait_element_visible(self.success_msg_locator)
        return el.text

    def click_active_btn(self):
        """点击某个操作"""
        self.click(self.active_btn_locator)
        return UserPage(self.driver)

    def get_money(self):
        """获取余额"""
        el = self.driver.find_element(*self.invest_input_locator)
        return el.get_attribute("data-amount")

    def click_invest_btn(self):
        resp = self.click(self.invest_btn_locator)
        return resp



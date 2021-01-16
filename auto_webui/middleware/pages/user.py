from selenium.webdriver.common.by import By


from common.selenium_handler import BasePage


class UserPage(BasePage):
    title = "个人中心"

    # 用户余额
    user_balance = (By.CLASS_NAME, "color_sub")

    def get_balance(self):
        """获取余额"""
        el = self.wait_element_visible(self.user_balance)
        return el.text[:1]

"""ob对象类模板"""
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.selenium_handler import BasePage
from selenium.webdriver.common.by import By
from middleware.handler import Handler


class OBClassName(BasePage):
    title = "首页"
    URL = Handler.yaml["host"]["pf"] + ""
    be_clickable = (By.XPATH, "//*[text()='隐藏数据']")  # 该元素可操作则可进行该页面的行为

    def __init__(self, driver):
        super().__init__(driver)
        try:
            WebDriverWait(driver, 30).until(
                expected_conditions.element_to_be_clickable(self.be_clickable)
            )
        except:
            Handler.logger.warning("可能未成功进入页面【{}】，可能会引发异常!".format(self.title+": "+self.URL))

    def get(self):
        """访问页面"""
        self.driver.get(self.URL)
        return self

    # locators
    hide_data_btn = (By.XPATH, "")


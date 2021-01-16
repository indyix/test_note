"""后台主页"""
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.selenium_handler import BasePage
from selenium.webdriver.common.by import By
from middleware.handler import Handler


class BossIndex(BasePage):
    title = "首页"
    URL = Handler.yaml["host"]["pf"] + "/manage/#/main/root/index"
    be_clickable = (By.XPATH, "//*[text()='隐藏数据']")

    def __init__(self,driver):
        super().__init__(driver)
        try:
            WebDriverWait(driver, 20).until(
                expected_conditions.element_to_be_clickable(self.be_clickable)
            )
        except:
            Handler.logger.warning("可能未成功进入页面【{}】，可能会引发异常!".format(self.title))

    # locators
    hide_data_btn = (By.XPATH, "//*[text()='隐藏数据']")

    def get(self):
        """访问页面"""
        self.driver.get(self.URL)
        return self

    def hide_indexdata(self):
        sleep(2)
        self.find_element(self.hide_data_btn).click()
        return self


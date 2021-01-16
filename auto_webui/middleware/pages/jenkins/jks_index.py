"""ob对象类模板"""
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.selenium_handler import BasePage
from selenium.webdriver.common.by import By
from middleware.handler import Handler
from middleware.pages.jenkins.daily_static_page import DailyStatistic


class JksIndex(BasePage):
    title = "DYW_TEST [Jenkins]"
    URL = "http://jenkins.senguo.me/"
    UPDATE_URL = r"http://jenkins.senguo.me/view/%E7%BB%9F%E8%AE%A1%E4%BB%BB%E5%8A%A1/job/UTIL-PF%EF%BC%9A%E6%AF%8F%E6%97%A5%E7%BB%9F%E8%AE%A1%E6%9B%B4%E6%96%B0/build?delay=0sec"
    be_clickable = (By.XPATH, "//a[@href='/logout']")  # 该元素可操作则可进行该页面的行为

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

    def move_to_update(self):
        self.driver.get(self.UPDATE_URL)
        return DailyStatistic(self.driver)

    # locators
    hide_data_btn = (By.XPATH, "")



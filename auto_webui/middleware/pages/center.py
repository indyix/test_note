"""中台切店页面"""
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.selenium_handler import BasePage
from selenium.webdriver.common.by import By

from middleware.handler import Handler
from middleware.pages.boss_index import BossIndex


class CenterPage(BasePage):
    title = "选择店铺"
    URL = Handler.yaml["host"]["passport"] + "#/main/shopList"

    # locator
    # 店铺分类tab
    tab_pf = (By.ID, "tab-pf")
    tab_pps = (By.ID, "tab-pps")
    pfshop_name = (By.XPATH,)
    hide_data_btn = (By.XPATH, "//*[text()='隐藏数据']")

    def get(self):
        self.driver.get(url=self.URL)
        return self

    def click_to_pfshops_list(self):
        self.find_element(self.tab_pf).click()
        return self

    def click_into_shop(self, shop_name):
        shop_locator = self.pfshop_name + ("//*[text()='" + shop_name + "']",)
        self.find_element(shop_locator).click()
        sleep(2)
        return BossIndex(self.driver)

import time

from appium.webdriver.common.mobileby import MobileBy

from common.basepage import BasePage


class TikuPage(BasePage):

    detail_name_locator = ('id', 'com.lemon.lemonban:id/category_title')


    def find_and_click_tiku(self, name, timeout=10, poll=0.2):
        """点击某个题库，传入参数题库名称"""
        used_time = 0
        while used_time < timeout:
            try:
                self.driver.implicitly_wait(0.1)
                el = self.find_element((MobileBy.XPATH, f"//*[contains(@text, '{name}')]"))
                self.driver.implicitly_wait(10)
                el.click()
                return self
            except TimeoutError as e:
                self.swipe_up()
                time.sleep(poll)
                used_time += poll
        raise TimeoutError("找不到题库")



    def get_title(self):
        return self.find_element(self.detail_name_locator).text





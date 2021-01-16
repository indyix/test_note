"""ob对象类模板"""
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.selenium_handler import BasePage
from selenium.webdriver.common.by import By
from middleware.handler import Handler
from middleware.pages.jenkins.daily_static_page import DailyStatistic
from middleware.pages.jenkins.jks_index import JksIndex


class JksLogin(BasePage):
    title = ""
    URL = r"http://jenkins.senguo.me/login?from=%2F"
    be_clickable = (By.XPATH, "//*[@name='Submit']")  # 该元素可操作则可进行该页面的行为

    def __init__(self, driver):
        super().__init__(driver)
        self.get()
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
    submit_btn = (By.XPATH, "//*[@name='Submit']")
    user_input = (By.XPATH, "//*[@name='j_username']")
    pwd_input = (By.XPATH, "//*[@name='j_password']")

    def login(self,username,password):
        self.find_element(self.user_input).send_keys(username)
        self.find_element(self.pwd_input).send_keys(password)
        self.find_element(self.submit_btn).click()
        return JksIndex(self.driver)

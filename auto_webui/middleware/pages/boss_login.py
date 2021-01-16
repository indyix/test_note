"""后台登录页面"""
from common.selenium_handler import BasePage
from selenium.webdriver.common.by import By
from middleware.handler import Handler
from middleware.pages.center import CenterPage


class BossLoginPage(BasePage):
    title = "登录"
    URL = Handler.yaml["host"]["passport"] + "#/login"

    # locators
    login_by_phone = (By.XPATH, "//span[text()='账号密码登录']")
    phone_input = (By.XPATH, "//*[@id='app']/div/div/div[2]/div[3]/div[1]/div/input")
    pwd_input = (By.XPATH, "//*[@id='app']/div/div/div[2]/div[3]/div[2]/div/input")
    login_btn = (By.ID, "pwdLogin")

    def get(self):
        """访问页面"""
        self.driver.get(self.URL)
        return self



    def login_success(self, phone,password):
        self.find_element(self.login_by_phone).click()
        self.enter_phone(phone)
        self.enter_password(password)
        self.find_element(self.login_btn).click()
        return CenterPage(self.driver)

    def enter_phone(self,phone):
        self.find_element(self.phone_input).send_keys(phone)
        return self

    def enter_password(self, password):
        self.find_element(self.pwd_input).send_keys(password)
        return self


"""收银台登录页面"""
from common.selenium_handler import BasePage
from selenium.webdriver.common.by import By

from middleware.handler import Handler

class CashierLoginPage(BasePage):
    title = "登录"

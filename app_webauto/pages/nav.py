from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from common.basepage import BasePage
from pages.home import HomePage
from pages.tiku import TikuPage
from pages.user import UserPage


class NavPage(BasePage):

    #
    my_locator = (MobileBy.ID,'com.lemon.lemonban:id/navigation_my')
    tiku_locator = (MobileBy.ID, 'com.lemon.lemonban:id/navigation_tiku')
    home_locator = (MobileBy.ID, 'com.lemon.lemonban:id/navigation_home')


    def click_my(self):
        self.click(self.my_locator)
        return UserPage(self.driver)

    def click_tiku(self):
        self.click(self.tiku_locator)
        return TikuPage(self.driver)

    def click_home(self):
        self.click(self.home_locator)
        return HomePage(self.driver)
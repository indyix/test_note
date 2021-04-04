import pytest
from appium import webdriver

from config import unsafe_config
from pages.nav import NavPage


@pytest.fixture()
def driver():
    # yaml.load()
    caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "appPackage": "com.lemon.lemonban",
        "appActivity": ".activity.MainActivity",
        "automationName": "UiAutomator2",
    }
    # 初始化客户端
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities=caps,
    )
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture()
def back_to_home():
    """返回首页"""
    pass

## 设置了成 class
## 测试完。有没有额外的清理工作。



@pytest.fixture()
def login(driver):
    """登录前置条件"""
    NavPage(driver). \
        click_my(). \
        click_avatar(). \
        login_success(unsafe_config.username, unsafe_config.pwd)
    yield driver
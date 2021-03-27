import os
from datetime import datetime

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import config
from middleware.handler import Handler


class MobileKey:
    ENTER = 66
    HOME = 3



class BasePage:
    title = None

    def __init__(self, driver):
        self.driver = driver
        # # self.title = None
        # try:
        #     WebDriverWait(self.driver, 20).until(
        #         expected_conditions.title_contains(self.title)
        #     )
        # except:
        #
        #     print("你的操作可能没有进入对应的页面，可能会引发异常{}".format(self.title))

    def find_element(self, locator):
        """查找元素"""
        try:
            el = self.driver.find_element(*locator)
            return el
        except:
            # 如果找不到元素，截图
            self.screen_shot()
            Handler.logger.error("元素找不到{}".format(locator))
            raise TimeoutError("没有找到元素")

    def screen_shot(self):
        """截图"""
        # logs/img/screenshot-2020-08-01-12-12-23.png
        path = config.IMG_PATH
        ts = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        filename = os.path.join(path, ts + ".png")
        self.driver.save_screenshot(filename)

    def wait_element_visible(self, locator, timeout=20, poll=0.5):
        """等待某个元素可见"""
        try:
            el = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                expected_conditions.visibility_of_element_located(locator)
            )
            return el
        except:
            self.screen_shot()
            Handler.logger.error("元素找不到{}".format(locator))

    def wait_element_clickable(self, locator, timeout=20, poll=0.5):
        """邓艾某个元素可以被点击"""
        try:
            el = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                expected_conditions.element_to_be_clickable(locator)
            )
            return el
        except:
            self.screen_shot()
            Handler.logger.error("元素找不到{}".format(locator))

    def wait_element_presence(self, locator, timeout=20, poll=0.5):
        try:
            el = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
                expected_conditions.presence_of_element_located(locator)
            )
            return el
        except:
            self.screen_shot()
            Handler.logger.error("元素找不到{}".format(locator))

    def click(self, locator):
        """点击某个元素"""
        self.wait_element_clickable(locator).click()
        return self

    def write(self, locator, value=''):
        """输入信息"""
        self.wait_element_presence(locator).send_keys(value)
        return self

    def scroll(self, height=None, width=None):
        """窗口滚动"""
        if not height:
            height = 0
        if not width:
            width = 0
        js_code = "window.scrollTo({}, {});".format(width, height)
        self.driver.execute_script(js_code)
        return self

    def move_to(self, locator):
        """移动到某个元素"""
        el = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(el).perform()
        return self

    def switch_frame(self, locator, timeout=20):
        """切换到frame"""
        WebDriverWait(self.driver, timeout=timeout).until(
            expected_conditions.frame_to_be_available_and_switch_to_it(locator)
        )
        return self

    """双击，拓转，窗口切换， alert, select, 文件上传"""

    """context 切换。"""

    def switch_context(self, context=None):
        """切换上下文"""
        if not context:
            self.driver.switch_to.context('NATIVE_APP')
        contexts = self.driver.contexts
        for c in contexts:
            if c == context:
                self.driver.switch_to.context(context)

    def press_enter(self):
        """点击回车或者确认按钮.
        特别常用的键盘操作
        """
        self.driver.press_keycode(MobileKey.ENTER)


    def get_toast(self):
        """获取toast弹框"""
        el = self.wait_element_presence(('xpath', '//android.widget.Toast'))
        return el

    def swipe_left(self, duration=None):
        """向左边滑动"""
        size = self.driver.get_window_size()
        # 得到一个字典
        width = size["width"]
        height = size["height"]
        # 向左滑动
        # 这个就是滑动的标准操作
        self.driver.swipe(
            start_x=width * 0.9,
            start_y=height * 0.5,
            end_x=width * 0.1,
            end_y=height * 0.5,
            duration=duration
        )

    def swipe_right(self, duration=None):
        size = self.driver.get_window_size()
        # 得到一个字典
        width = size["width"]
        height = size["height"]
        # 向左滑动
        # 这个就是滑动的标准操作
        self.driver.swipe(
            start_x=width * 0.1,
            start_y=height * 0.5,
            end_x=width * 0.9,
            end_y=height * 0.5,
            duration=duration
        )

    def swipe_up(self, duration=None):
        size = self.driver.get_window_size()
        # 得到一个字典
        width = size["width"]
        height = size["height"]
        # 向左滑动
        # 这个就是滑动的标准操作
        self.driver.swipe(
            start_x=width * 0.5,
            start_y=height * 0.9,
            end_x=width * 0.5,
            end_y=height * 0.1,
            duration=duration
        )

    def swipe_down(self, duration=None):
        size = self.driver.get_window_size()
        # 得到一个字典
        width = size["width"]
        height = size["height"]
        # 向左滑动
        # 这个就是滑动的标准操作
        self.driver.swipe(
            start_x=width * 0.5,
            start_y=height * 0.1,
            end_x=width * 0.5,
            end_y=height * 0.9,
            duration=duration
        )


    def jiugongge(self, locator, pos: list):
        """九宫格。
        pos = [2,3,5,7]
        """
        el = self.find_element(locator)
        size = el.rect

        start_x = size["x"]
        start_y = size["y"]
        width = size["width"]
        height = size["height"]


        points = [
            {"x": start_x + width * 1 / 6, "y": start_y + height * 1 / 6},
            {"x": start_x + width * 3 / 6, "y": start_y + height * 1 / 6},
            {"x": start_x + width * 5 / 6, "y": start_y + height * 1 / 6},
            {"x": start_x + width * 1 / 6, "y": start_y + height * 3 / 6},
            {"x": start_x + width * 3 / 6, "y": start_y + height * 3 / 6},
            {"x": start_x + width * 5 / 6, "y": start_y + height * 3 / 6},
            {"x": start_x + width * 1 / 6, "y": start_y + height * 5 / 6},
            {"x": start_x + width * 3 / 6, "y": start_y + height * 5 / 6},
            {"x": start_x + width * 5 / 6, "y": start_y + height * 5 / 6},
        ]



        points = [
            {'x': start_x + width / 6 * 1, 'y': start_y + height / 6},
            {'x': start_x + width / 6 * 3, 'y': start_y + height / 6},
            {'x': start_x + width / 6 * 5, 'y': start_y + height / 6},
            {'x': start_x + width / 6 * 1, 'y': start_y + height / 6 * 3},
            {'x': start_x + width / 6 * 3, 'y': start_y + height / 6 * 3},
            {'x': start_x + width / 6 * 5, 'y': start_y + height / 6 * 3},
            {'x': start_x + width / 6 * 1, 'y': start_y + height / 6 * 5},
            {'x': start_x + width / 6 * 3, 'y': start_y + height / 6 * 5},
            {'x': start_x + width / 6 * 5, 'y': start_y + height / 6 * 5},
        ]

        touch = TouchAction(self.driver)

        # 传入的参数是从 0 开始的。
        # pos = [2,3,5,7]
        # 索引 = 位置 - 1
        touch.press(**points[pos[0] - 1]).wait(200)
        for p in pos[1:]:
            touch.move_to(**points[p - 1]).wait(200)
        touch.release().perform()






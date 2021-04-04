import time

from appium import webdriver
from appium import 

desired_caps = dict()
desired_caps["platformName"]="ios"
desired_caps["platformVersion"]="14.4."
desired_caps["deviceName"] ="iPhone X"
desired_caps["app"] ="cc.senguo.SenguoPFBossApp"
desired_caps["udid"] = "a4485fabb6c524aca88551388f334579ce8a760f"
desired_caps["xcodeOrgid"]= "D7TAX4VQ82"
desired_caps["xcodeSigningId"]= "iPhone Developer"
# 启动app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

time.sleep(10)
driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="其他方式登录"]').click()


# 点击 协议单选框
# driver.tap([(57,819)],200)
# 点击 其他方式登录
# 点击 虚拟键盘输入手机号 17386049001
# 点击 密码输入框
# 点击 虚拟键盘输入密码 123456
# 点击 确认  进行登录


time.sleep(5)
print("+++")
driver.quit()

driver.find_element_by_xpath().click()  # 点击
# 经验01 安卓中只查找屏幕上显示的控件，ios中则还能能找到屏幕外延的
# 不过要点击的话，还是需要显示在屏幕上
# driver.swipe() # 滑动
# class_name→type
# driver.execute_script("console.log('执行js代码')") # 执行js代码
# driver.execute_script("mobile: scroll",{"direction":"down"})
# driver.execute_script("mobile: swipe",{"direction":"up"})
# driver.find_element_by_xpath().clear() # 清空文本框
# driver.find_element().send_keys() # 输入文字
# 经验02 有时候send_keys、clear一类对输入框操作的方法需要在虚拟键盘唤起时才能正常使用。模拟器如果启用了实体键盘可
# 能会导致不能唤起虚拟键盘从而导致appium无法正常工作

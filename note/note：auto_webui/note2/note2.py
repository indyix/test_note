# 回顾：
import time
from selenium import webdriver
# 私密链接提示关闭
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome("./chromedriver.exe", options=options)

# driver.get("https://12306.cn/index")
# # 使用强制等待：多个系统之间的交互
# time.sleep(1)

"""=========JS操作================="""
#
# # Python脚本（http）→webdriver→js脚本→浏览器,Python脚本使用webdriver通过js脚本间接控制浏览器
# ## python可以直接获取属性
# e = driver.find_element_by_id("train_date")
# print(e.get_attribute('value'))
#
# ## 设置属性，selenium没有封装，需要自己定义
# def set_attribute(e):
#     """传入js代码，设置元素e的属性
#     e.document.getElementById("kw")
#     e.value = "搜索内容"
#     """
#     js_code="""e = document.getElementById("train_date");
#     e.value = "2020-09-08"
#     """
#     driver.execute_script(js_code)
# set_attribute(e)
#
# # 使用driver.execute_script() 执行js代码修改元素属性
# driver.execute_script('e = document.getElementById("train_date");')
# driver.execute_script('e.value = "2020-09-01"')
#
# # Python-element对象在js代码中直接转换为js对象来用, 使用arguments[x]占位
# driver.execute_script("arguments[0].value='2020-09-02'",e) # arguments[x]表示取后面传参*agrs的第x-1个参数
#
# # 窗口滚动：
# # 滚动到元素可视：有的元素不滚动到可视范围将不能操作
# cjwt = driver.find_element_by_link_text("常见问题")
# cjwt.location_once_scrolled_into_view  # 将元素滑动到可视范围内（原码：通过执行jd代码实现）
# cjwt.click()
#
# # 滚动到页面最底部（selenium没有封装）
# # js代码：window.scrollTo(x, y)  顶点为(0,0)
# # 滑动到页面底部 window.scrollTo(0, document.body.scrollHeight)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")


"""===========上传文件============"""
driver.get("D:/Pythonauto/Python_Workspace/web/note2/uploadfiles.html")
# 方法一：send_keys()
el = driver.find_element_by_name("mfile")
# el.send_keys("D:/用户/Administrator/Pictures/74238474_p0.png")  # send_keys()  发送文本，发送按键，发送文件

# 方法二：有时候上传文件的组件不是input元素，所以不能用send_keys()。需要调用系统的资源管理器
# # windows下： win32gui
# # windows下： pywinauto ， 基于win32gui进行的封装

el.click()  # 浏览器指令
# time.sleep(1)
# from pywinauto import Desktop
# app = Desktop()  # 操作系统的指令
# dialog = app["打开"]
# dialog["Edit"].type_keys("D:/用户/Administrator/Pictures/74238474_p0.png")
# dialog["Button"].click()

# 方法三：pyautogui 跨平台（建议用3.7,3.8有兼容性问题），缺点：路径中不能传中文，不过可以用pyperclip剪切盘粘贴中文
# python3.8安装
# pip install pillow==6.2.2   （3.8没有处理对pillow的兼用，需要手动安装合适的pillow版本）
# pip install pyautogui

el.click()  # 浏览器指令
import pyautogui
# pyautogui.write("d:/用户/Administrator/Pictures/74238474_p0.png")  # 选择图片
# pyautogui.press('enter',presses=2)  # 确认，按两次确认键
# time.sleep(2)
# 中文
import pyperclip
pyperclip.copy("D:\中文路径/www.txt")
time.sleep(2)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter',presses=2)



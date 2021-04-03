from selenium import webdriver
import os
import sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep



# ==== selenium原理 ==============================================================================
# webdriver 服务器驱动（提供了接口）
# selenium 对webdriver提供的接口的调用进行了封装
# urllib3  selenium的依赖库，用于发送请求

# === 踩坑 =============================================================================================
# dr = webdriver.Chrome("chromedriver.exe")
# # 坑：1.加载driver的顺序：print(sys.path)
# # 2.需要管理员模式运行cmd或者ide
# # 3.需要重装浏览器
# dr.get("http://zhihu.com")
# dr.maximize_window()
# dr.minimize_window()
# dr.set_window_size(800,600)
# dr.get("http://baidu.com")

# ==================== requests 管理cookie ===========================================================================
# # requests cookies管理：requests 用session记录cookie
# import requests
# # requests.request()  可以这么调用，也可以用session：
# s = requests.session()
# s.request("get",url="xxx")  #session调用request时会自动记录cookie

# ================ DOM操作 ===========================================================================================
# DOM操作
# 页面在不同时期内表现会不一样，定位一个元素，同样的元素定位方式去定位同一个元素
# 事件：描述
# onchange      HTML元素改变
# onclick       用户点击HTML元素
# onmouseover   元素上移动鼠标
# onmouseout    从元素上移开鼠标
# onkeydown     按下键盘按键
# onload        浏览器加载完成页面

# 定位某些输入框需要改变元素的属性使其处于可读写状态（disabled、readonly、→）
# # document.getElementsByName("username")[0].disabled=false;

# 前端网页：HTML 结构化静态页面，CSS样式，JS动效和交互（浏览器中装有js解释器，其他语言需要用js去控制浏览器）

# DOM对象：document object model，
# DOM树：Document-根元素<html>
# ---------------------------Element：<head>、
# ---------------------------Element：<head>-Element：<title>
# ---------------------------Element：<head>-Element：<title>-Text："itbil.com"
# ---------------------------Element：<body>-Element：<a>-Attribute：<href>
# ---------------------------Element：<body>-Element：<h1>-Text："www.baidu.com"
# HTML文档中的所有内容都是节点：
# -----整个文档是一个文档节点，每个HTML元素是元素节点，
# -----HTML元素内的文本是文本节点，每个HTML属性是属性节点，注释是注释节点

# DOM操作：
# Windows操作：
# window.location、  window.href、    window.name、    window.alert("hello")、  window.scrollTo()
# 常用事件： on开头
# onchange HTML元素改变、  onclick 点击触发、 onmouseover 在元素上移动鼠标、 onmouseout 从元素上移开鼠标、
# onkeydown 按下键盘按键、 onload 浏览器完成加载
# 元素定位
# e = document.getElementsByName("username")[0]，document.getElementById("id")

# 修改属性
# e.value = "修改值"
# e.style.backgroundColor = "red"

# =============== 元素定位 ==========================================================================================
# 八种元素定位方式：常用8种，实则有四种，另外四种是通过css_selector封装出来的
# id name  class_name  tag_name  link_text  partial_link_text  xpath  css_selector
# 其中 id name tag_name  class_name 也是通过css_selector来进行定位的：
# find_element_by_id('kw') 等价于find_element('id','kw')  框架封装更多用后者
# 获取元素属性：element.get_attribute('name')

# 踩坑：
# find_element（无则报错） 和find_elements（无则返回空列表）
# 获取元素属性：e.get_attribute("id")
# 不要用动态属性（纯数字22 23 、带数字a2 a3）和不规则字符串（太长）
# class_name 进行定位，字符串之间不能有空格，该定位方法是通过模糊查询进行元素查找的。不过用于xpath的谓语条件时是可以用空格的

# xpath 和css_selector  组合多个特征和属性进行定位
# xpath定位：/  // 标签 *（表任意标签或属性）、   谓语条件、   父子标签，    三部分构成
# ———— 表达式：可以自己编写、使用插件、或使用浏览器右击复制
# ———— 绝对路径：/html....
# ———— 相对路径：//*[@id='kw']、//input[@id='kw' and @name='']   [@id='kw'] ==>  谓语条件，属性=属性值
# ———— xpath中的函数：如contains(@属性,关键字)    text()
# ———————— driver.find_element("xpath","//title[text()=' 新闻']/../title")
# ———————— driver.find_element("xpath","//a[contains(text(),'新闻')]")
# 标准xpath属性：
# ———— '//input[@class='' and text()='文本']'
# ———— //div/input[谓语条件]/div
# ———— //*[]                *表任意标签
# ———— //input[@*='kw']     *表任意属性
# ———— //input[@id]         有属性id即可
# ———— //input[contains(@class,'value')]
# ———— 索引：(//input)[1]
# ———— 轴定位、轴运算：通过DOM关系结构查找元素：使用轴运算符+::修饰标签(https://www.jianshu.com/p/d4c62a1f9d8e)
# //input[@id='user2']//preceding-sibling::input[@id='user1']
# //input[@id='user2']//following-sibling::input[@id='pwd']
# 常用：following-sibling、preceding-sibling、ancestor

# css选择器：可以通过父级元素定位子元素，而不能通过子元素定位父级元素
# .s_ipt    ==> class_name = s_ipt
# #kw       ==> id = 'kw'
# input[id=kw] 或者 input#kw==> //input[@id='kw']

# css vs xpath
# css表达简洁、主流浏览器上查询速度快（ms级别，封装可以用css_selector，平时使用可以一批能够xpath）、
# xpath功能更灵活、支持text文本定位、对复杂元素的写法反而更简单（css的逻辑处理要少一些）

# =============== 元素等待 ==========================================================================================
# 强制等待：time.sleep(5)
# 隐性等待：设置元素查找的超时时间，-全局的：driver.implicitly(20)
# ————  设置超时时间，全局设置，只能用来等待元素
# 显性等待：等待某个元素可以被点击、等待某个元素可见、等待某个窗口被打开
# from selenium.webdriver.support.wait import WebDriverWait
# # wait = WebDriverWait(driver,20,poll_frequency=0.5)    # 设置定时器
# # wait.until(条件表达式)        # 设置退出条件，若超过20秒条件未达成则强制退出
# # 使用expected_conditions：
# ———— from selenium.webdriver.support import expected_conditions
# ———— locator = ('xpath','//input[@id="pwd"]')
# ———— elem = wait.until(expected_conditions.presence_of_element_located(locator=locator))  # 等待元素出现，返回该元素
# # 常用conditions：
# ———— 1. presence_of_element_located(locator)      元素是否出现
# ———— 2. visibility_of_element_located(locator)         元素可见
# ———— 3. element_to_be_clickable(locator)               元素可点
# # # 封装
# def wait_element_clickable(locator,driver,timeout=20,poll=0.5):
#     wait = WebDriverWait(driver, timeout=timeout, poll_frequency=poll)
#     elem = wait.until(expected_conditions.presence_of_element_located(locator=locator))
#     return elem
# 显性等待找不到元素：报错：TimeoutException

# 选择：有些元素再进入网页后要动态加载后出现才可点击，需要用隐式等待。如果元素需要修改条件才可见可点，可用显式等待
# 先直接find_element，如果找不到：
# 隐性：全局设置等待查找元素
# 显性：等待元素可点、可见（切换条件：clickable,visible,precese）
# 强制：多个系统交互

# 元素无法找到的原因：
# 1.检查元素定位方式是否正确 - 2.没有等待（）- 3.有没有在页面（在该窗口中？在该iframe中？）

"""=================== 窗口切换 ============================================================================"""

# 获取当前窗口的url：driver.current_url
# 切换到窗口：driver.switch_to.window(窗口句柄)、driver.switch_to.window(dr.window_handles[-1])

# 切换到iframe：driver.switch_to.frame('frame_name')（frame的name属性）、driver.switch_to.frame(1)（索引）、
# ————driver.switch_to.frame(dr.find_element_by_tag_name('iframe'))
# iframe切换回主页面： driver.switch_to.default_content()
# iframe1切换到内部iframe2：先切换到iframe1再切换到iframe2
# 切换到父级iframe： driver.switch_to.parent_frame()
# iframe等待：隐性等待可以等元素加载出来（可以等iframe加载出来，但不会等其内部元素加载出来→→显式等待,并切换进去）
# iframe_elem = driver.find_element_by_xpath('//iframe[@src]')  # 先定位到iframe元素
# WebDriverWait(driver,30,poll_frequency=0.5).until(
#     expected_conditions.frame_to_be_available_and_switch_to_it(iframe_elem)
# )
#
# # 切换到弹窗alert并点击按钮：
# driver.switch_to.alert.accept()  # 接受
# driver.switch_to.alert.dismiss()  # 取消
# # alert等待（不用传参，一个页面中alert只有一个）
# WebDriverWait(driver,30,poll_frequency=0.5).until(
#     expected_conditions.alert_is_present(iframe_elem)
# )


"""===================================鼠标操作==============================================="""
# # 鼠标操作：能找到元素，元素不一定可点(悬浮+点击)
# driver = webdriver.Chrome()
# elem1 = driver.find_element_by_xpath('input[@id="110"]')
# elem2 = driver.find_element_by_xpath('input[@id="110"]')
# from selenium.webdriver import ActionChains
# action_chains = ActionChains(driver)
# # - 左击
# elem1.click()
# ActionChains(driver).click(elem1).perform()
# # 按住不动 ActionChains(driver).click_and_hold(elem)
# # - 双击
# ActionChains(driver).double_click(elem1).perform()
# # - 悬停
# action_chains.move_to_element(elem1).perform()
# # - 拖曳
# ActionChains(driver).drag_and_drop(elem1,elem2).perform()
# # - 右击
# ActionChains(driver).context_click(elem1).perform()
# # 链式调用：
# # click(elem1),.double_click(elem1)等等只是将操作指令加到调用列表中，perform才是执行这些指令（直接看源码）
# ActionChains(driver).click(elem1).double_click(elem2).perform()    # 连续添加指令的条件是前一个指令返回对象本身(return self)，
# # 这样才能继续加入其他指令.perform()没有返回self

# 动作链条：拼装各个操作，然后一次性一起执行
# _actions = []
# def a1():
#     print("a1")
# def a2():
#     print("a2")
# def perform():
#     for action in _actions:
#         action()
# _actions.append(a1)
# _actions.append(a2)
# perform()

# 键盘操作：使用send_keys(Keys.键盘按键)
# driver = webdriver.Chrome("./chromedriver.exe")
# driver.get("https://www.baidu.com")
# # elem1 = driver.find_element_by_xpath('input[@id="110"]')
# elem2 = driver.find_element_by_xpath('//input[@id="kw"]')
# from selenium.webdriver.common.keys import Keys
# elem2.send_keys("文本内容")
# elem2.send_keys(Keys.ENTER)
# elem2.submit()   # 数据提交的三种操作：click()提交键、按回车键提交数据、submit() form类型的表单


# 下拉框操作：select操作
# 选择select元素：点击option元素，或者通过Select类操作
# 点击,单选
driver = webdriver.Chrome("chromedriver.exe")
driver.get("file:///D:/Pythonauto/Python_Workspace/web/testweb.html")
# option1 = driver.find_element_by_xpath('//option[@value="xx2"]')
# option1.click()

# Select，可多选
sel1 = driver.find_element_by_xpath('//select[@name="select1"]')
from selenium.webdriver.support.select import Select
s = Select(sel1)

s.select_by_value("xx2")
sleep(1)
s.select_by_visible_text("选项1")
sleep(1)
s.select_by_index(2)


if __name__ == '__main__':
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions
    # from selenium import webdriver
    from selenium.webdriver import ActionChains
    # import time
    # dr = webdriver.Chrome('./chromedriver.exe')
    # dr.get('https://www.baidu.com')
    # dr.find_element('id','kw').send_keys('柠檬班')
    # dr.find_element('xpath',"//*[@id='su']").click()
    # wait = WebDriverWait(dr,20,poll_frequency=0.5)    # 设置定时器
    # locator = ('xpath','//*[text()="lemon.ke.qq.com/"]')
    # elem = wait.until(expected_conditions.presence_of_element_located(locator=locator))  # 等待元素出现，返回该元素
    # print(elem.text)
    # print(dr.current_url)
    # elem.click()
    # print(dr.window_handles)
    # dr.switch_to.window(dr.window_handles[-1])
    # print(dr.current_url)
    # time.sleep(2)
    # # ele1 = dr.find_element_by_link_text("设置")
    # # print(ele1.text)
    # ele2 = dr.find_element_by_id("kw")
    # # ac = ActionChains(dr)
    # # ac.move_to_element(ele1).click(ele2).perform()
    # ele2.send_keys("110")
    # ele2.submit()



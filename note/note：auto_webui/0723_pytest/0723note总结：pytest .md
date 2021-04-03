## pytest 特性

### 标记 mark

- 注册一个标签：pytest.ini

 ```python
[pytest]
markers =
    success122
    fail
    
log_format = %(asctime)s %(levelname)s %(message)s
log_date_format = %Y-%m-%d %H:%M:%S
 ```

 

- 标记测试函数/测试方法/测试类
  - @pytest.mark.tagname    标记
  - 标记整个类，则在类上面加 @pytest.mark

- 调用被标记用例 
  - pytest -m "tagname"    运行标记的用例
  - 调用被标记用例时，如果要有逻辑运算的标记，要加双引号
    - and  必须同时具备两个标签
    - or  只需要满足其中的一个标签，就会运行
    - not    "success and not demo"


### 数据驱动
```python
# unitest：
@ddt.ddt
class TestClass()....
	@ddt.data(*test_data_list)
	def  test_fangfa（self, test_info）
		pass

# pytest: data_list=[{}, {}, {}]
class TestClass()...
	@pytest.mark.paramatrize("**test_info**", data_list):
	def test_demo(**test_info**):
		pass
```
#### 数据驱动注意事项
在使用pytest.mark.paramatrize 做数据驱动的时候，pytest 和 unittest 不兼容：

- 如果使用 pytest 的数据驱动装饰器，测试类不能继承 unittest.TestCase，否则就需要用ddt做数据驱动。同时断言也不能用unitest的断言self.assert，需要使用Python自带的assert
- 如果要使用unittest写用例,  就要用 unittest 的数据驱动ddt



### 断言

pytest的断言可以直接使用的 python 内置的关键字 assert





## 认知

### pytest 两个功能不能和unittest兼容

- paramatrize  数据驱动

- fixture  测试夹具

- hook

  此外都是兼容的

### pytest 和 unittest 共用

- unittest 去编写用例
  - ddt
  - setUptearDown
  - self.assertTrue()

- pytest 运行用例
  - 自动收集
  - 用例筛选
  - 测试报告
  - 测试插件

### pytest和unittest的优劣

“unittest 过时了，pytest 才是王道”？

- unittest是标准库
  - 不需要安装；标准库不存在和 python 版本不兼容的问题。 
- pytest是三方库
  - 好用；但存在更新修复bug不及时，与Python版本不兼容的问题





## pytest——add

https://www.cnblogs.com/poloyy/tag/Pytest/

#### pytest运行

```
4、运行模块.测试类.某个方法
pytest test_today-transaction::TestTrans::test_trance_success
5、-m 标记表达式
pytest -m login
6、-q 简单打印，只打印测试用例的执行结果
pytest -q start.py
7、-s 详细打印
pytest -s start.py
8、-x 遇到错误时停止测试
pytest start.py -x
9、--maxfail=num，当用例错误个数达到指定数量时，停止测试
pytest start.py --maxfail=1
10、-k 匹配用例名称
执行测试用例名称包含http的所有用例
pytest -s -k http start.py
不包含http的所有用例
pytest -s -k "not http" start.py
同时匹配不同的用例名称
pytest -s -k "method or weibo" start.py
11、pycharm运行

# cmd运行：
pytest
	--reruns 2 --reruns-delay 5 
	-m error_test11 
	-s 
	--html=ceshi.html

# ide内使用脚本运行：
pytest.main(["--reruns","2","--reruns-delay", "5",
	"-m error_test11", 
	"-s", 
	"--html=ceshi.html"])

# 参数说明：pytest插件库：http://plugincompat.herokuapp.com

# 捕获所有输出（如print()）:-s, 不加的话输出信息就不会显示
pytest.main(["--html={}.html".format(ts), "-m demo","-s"])

# 测试报告
安装模块：pip install pytest-html
使用：pytest -m "demo and not smoke" --html=report.html

# 重运行
安装：pip install pytest-rerunfailures
调用： --reruns reruntimes    --reruns-delay delaytime
pytest --reruns 2 --reruns-delay 5
pytest.main(["--reruns","5"])

# -q 简化报告
```

<img src=".\img/pycharm运行.png" alt="image-20210118000655160" style="zoom:25%;" />

#### pytest-repeat

```
# 安装
		pip3 install pytest-repeat -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

# 使用1：重复执行2次 --count=2
		pytest --count=2 

# 使用2：重复执行mark标记的用例 @pytest.mark.repeat(5)   
# 重复标记的用例时mark.repeat优于count
    # test_.py
    @pytest.mark.repeat(5)
    def test_repeat():
        print("测试用例执行")
    # cmd：
    pytest

# 重复的顺序 --repeat-scope=class
    # function：默认，对每个用例重复执行后再执行下一个用例
    # class：以class为用例集合单位，重复执行class里面的用例，再执行下一个
    # module：以模块为单位，重复执行模块里面的用例，再执行下一个
    # session：重复整个测试会话，即所有测试用例的执行一次，然后再执行第二次
```

#### pytest-html

```
# 安装 
		pip3 install pytest-html -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
# 使用：css独立，分享报告时会丢失样式
		pytest --html=report.html
# 使用：合并样式
		pytest --html=report.html --self-contained-html

```

#### pytest-rerunfailures

```
# 安装
		pip3 install pytest-rerunfailures -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
# 使用
    命令行参数：--reruns n（重新运行次数），--reruns-delay m（等待运行秒数）
    装饰器参数：reruns=n（重新运行次数），reruns_delay=m（等待运行秒数）
# 重新运行所有失败的用例（运行失败的fixture或setup_class也将重新执行）
		pytest --reruns 3 --reruns-delay 5 -s
# 指定测试用例在测试失败时重新运行
    #.py：
    @pytest.mark.flaky(reruns=5) 
    def test_example():
        import random
        assert random.choice([True, False, False]) 
    # cmd：
    pytest

# 注意：指定了用例的重新运行次数，对这些用例设置的--reruns会被覆盖 
    @pytest.mark.repeat(3)
    @pytest.mark.flaky(reruns=4,reruns_delay=2)
    def test_example():
    	import random
    	assert random.choice([True, False, False])
    	
# repeat不会重新实例化fixtrue, rerun则会
```

 #### 前置后置

```
pytest提供了类似unittest中的setup、teardown的方法：
    模块级别：setup_module、teardown_module
    函数级别：setup_function、teardown_function，不在类中的方法
    类级别：setup_class、teardown_class
    方法级别：setup_method、teardown_method
    方法细化级别：setup、teardown

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__title__  =
__Time__   = 2020-04-06 11:40
__Author__ = 小菠萝测试笔记
__Blog__   = https://www.cnblogs.com/poloyy/
"""
import pytest


def setup_module():
    print("=====整个.py模块开始前只执行一次:打开浏览器=====")


def teardown_module():
    print("=====整个.py模块结束后只执行一次:关闭浏览器=====")


def setup_function():
    print("===每个函数级别用例开始前都执行setup_function===")


def teardown_function():
    print("===每个函数级别用例结束后都执行teardown_function====")


def test_one():
    print("one")


def test_two():
    print("two")


class TestCase():
    def setup_class(self):
        print("====整个测试类开始前只执行一次setup_class====")

    def teardown_class(self):
        print("====整个测试类结束后只执行一次teardown_class====")

    def setup_method(self):
        print("==类里面每个用例执行前都会执行setup_method==")

    def teardown_method(self):
        print("==类里面每个用例结束后都会执行teardown_method==")

    def setup(self):
        print("=类里面每个用例执行前都会执行setup=")

    def teardown(self):
        print("=类里面每个用例结束后都会执行teardown=")

    def test_three(self):
        print("three")

```

#### fixtrue

```
把 return 改成 yield 实现前置和后置
 测试夹具使用：作为测试方法的形参根据scope值不同，该方法所属类、所属模块会在运行前后执行夹具代码 
  def test_login_error(self, test_info, fixtrue_driver)
  	fixtrue_driver.find....... 	
  # 架构：所有测试夹具放在conftest.py文件中，pytest调用夹具时会自己从该文件中获取相应代码
  
# 相比提供的前后置条件，优点：
		命名方式灵活，不局限于 setup 和teardown 这几个命名
		conftest.py 配置里可以实现数据共享，不需要 import 就能自动找到fixture
		scope="module" 可以实现多个.py 跨文件共享前置
		scope="session" 以实现多个.py 跨文件使用一个 session 来完成多个用例

# fixtrue定义
		# 参数说明
    @pytest.fixture(scope="function", params=None, autouse=False, ids=None, name=None)
    def test():
        print("fixture初始化的参数列表")

        scope：可以理解成fixture的作用域，默认：function，还有class、module、package、session四个【常用】
        autouse：默认False，需要用例手动调用该fixture；如果True，所有作用域内的测试用例都会自动调用该fixture
        name：默认装饰器的名称，同一模块的fixture相互调用建议写个不同的name
    
    # fixtrue定义时依赖其他fixtrue
    @pytest.fixture(scope="session")
    def open():
        print("===打开浏览器===")

    @pytest.fixture
    # @pytest.mark.usefixtures("open") 不可取！！！不生效！！！
    def login(open):
        # 方法级别前置操作setup
        print(f"输入账号，密码先登录{open}")

# fixtrue调用
		将fixture名称作为测试用例函数的输入参数
		测试用例加上装饰器：@pytest.mark.usefixtures("fixture_name")；可以叠加使用，先执行的放在底层
		fixture设置autouse=True
		
# fixture的实例化顺序
    较高 scope 范围的fixture（session）在较低 scope 范围的fixture（ function 、 class ）之前实例化【session > 						package > module > class > function】
    具有相同作用域的fixture遵循测试函数中声明的顺序，并遵循fixture之间的依赖关系【在fixture_A里面依赖的fixture_B优先实例					化，然后到fixture_A实例化】
    自动使用（autouse=True）的fixture将在显式使用（传参或装饰器）的fixture之前实例化
    
# fixtrue+yield
		yield注意事项
        如果yield前面的代码，即setup部分已经抛出异常了，则不会执行yield后面的teardown内容
        如果测试用例抛出异常，yield后面的teardown内容还是会正常执行

# fixtrue传参

# 传单个参数
# indirect=True：此参数把 login 当成一个fixtrue函数去执行，而不是一个参数，且将data当做参数传入函数
import pytest

@pytest.fixture()
def login(request):
    name = request.param
    print(f"== 账号是：{name} ==")
    return name


data = ["pyy1", "polo"]
ids = [f"login_test_name is:{name}" for name in data]


@pytest.mark.parametrize("login", data, ids=ids, indirect=True)
def test_name(login):
    print(f" 测试用例的登录账号是：{login} ")

# 不用indirect
import pytest

data = ["pyy1", "polo"]
ids = [f"login_test_name is:{name}" for name in data]

@pytest.mark.parametrize("login", data, ids=ids)
def test_name(login):
    print(f" 测试用例的登录账号是：{login} ")

# 执行结果failed、error：
		# error是执行前置fixtrue时的断言失败和报错、包括执行用例时前置fixtrue找不到；	
		# failed是执行用例时的断言失败和报错
# fixture里：断言失败、抛出异常，error；用例里调用的fixture不存在也会error
# 用例里：断言失败、抛出异常，failed:
# 测试用例的代码有异常，包括主动抛出异常或代码有异常，都算failed
# 当测试用例调用的fixture有异常，或传入的参数有异常的时候，都算error
# 如果一份测试报告中，error的测试用例数量越多，说明测试用例质量越差
# @pytest.mark.xfail(raises=ZeroDivisionError)
```

#### conftest.py

```
# 实际开发场景
多个测试用例文件（test_*.py）的所有用例都需要用登录功能来作为前置操作，那就不能把登录功能写到某个用例文件中去了
conftest.py:单独管理一些全局的fixture
# conftest.py配置fixture注意事项
# 名称固定、pytest会默认读取conftest.py里面的所有fixture、测试用例文件中不需要手动import conftest.py，pytest会自动查找
# conftest.py只对同一个package下的所有测试用例生效：
不同目录可以有自己的conftest.py（处理前置条件），一个项目中可以有多个conftest.py
外层fixture实例化=》内层fixture实例化，同名时后者会覆盖前者
```

![image-20210202123633002](/Users/edz/PycharmProjects/test_code/note/web自动化测试/0723_pytest/img/conftest相关.png)

 #### allure

```
reporting:
  --alluredir=DIR       Generate Allure report in the specified directory (may not exist)
  --clean-alluredir     Clean alluredir folder if it exists
  --allure-no-capture   Do not attach pytest captured logging/stdout/stderr to report
reporting 报告相关参数

--alluredir=DIR 指定报告的目录路径
--clean-alluredir 如果已经存在报告，就先清空它
--allure-no-capture 不加载 logging/stdout/stderr 文件到报告

带上 clean-alluredir 参数重新执行用例

pytest --alluredir ./report/allure_report --clean-alluredir
allure serve ./report/allure_report
```



#### log：

https://www.cnblogs.com/superhin/p/11677408.html

```
# 记录日志
# Pytest默认捕获WARNING以上日志消息，在每个失败的测试结果概要中，捕获的log信息和stdout、stderr信息使用相同的方式，分块显示。
----------------------- Captured stdlog call ----------------------
test_reporting.py    26 WARNING  text going to logger
----------------------- Captured stdout call ----------------------
text going to stdout
----------------------- Captured stderr call ----------------------
text going to stderr
==================== 2 failed in 0.02 seconds =====================

## 设置格式：pytest.ini
[pytest]
log_level = INFO
log_format = %(asctime)s %(levelname)s %(message)s
log_date_format = %Y-%m-%d %H:%M:%S

## 实验结果不可用：
    ## 可以更改捕获的日志消息的日志级别。这由caplog夹具支持：
    def test_foo(caplog):
        caplog.set_level(logging.INFO)
        pass
    ## 默认情况下，该级别是在根记录器上设置的，但为方便起见，还可以设置任何记录器的日志级别：
    def test_foo(caplog):
        caplog.set_level(logging.CRITICAL, logger="root.baz")

## 禁止对失败用例进行stdout、stderr及日志捕获：
pytest --show-capture=no



# 实时日志
# 通过将log_cli配置选项设置为true，pytest将在直接将日志记录发送到控制台时输出日志记录
------------ live log setup ----------------------------------------
[WARNING  2021-01-19 03:28:25  ] conftest.py  logger line:46  msg:logging.logger
[INFO  2021-01-19 03:28:25,192  ] logging_handler.py  line:65  msg:登录成功, 账号：17386049001
[INFO  2021-01-19 03:28:25  ] logging_handler.py  info line:65  msg:登录成功, 账号：17386049001
------------ live log call ------------------------------------------
[INFO  2021-01-19 03:28:25  ] test_today-transaction.py  test_trance_success line:21  msg:执行用例1
PASSED
tests/test_today-transaction.py::TestTrans::test_trance_success[test_info1] 
------------ live log call ------------------------------------------
[INFO  2021-01-19 03:28:25  ] test_today-transaction.py  test_trance_success line:21  msg:执行用例2
PASSED
tests/test_today-transaction.py::TestTrans::test_trance_success[test_info2] 

## 设置格式：
[pytest]
log_cli = True
log_cli_level = WARING
log_cli_format =
log_cli_date_format = 



# 文件日志
[pytest]
log_file = ./logs/test.log
log_file_level
log_file_format
log_file_date_format
```



#### mark

```
# pytest.mark.skip

  # 跳过测试函数，类，类方法
  @pytest.mark.skip(reason="不执行该用例！！因为没写好！！")
  def test_case02():
      print("我是测试用例22222")

  # 测试函数、类、类方法执行时跳过
  def test_function():
      n = 1
      while True:
          print(f"这是我第{n}条用例")
          n += 1
          if n == 5:
              pytest.skip("我跑五次了不跑了")

  # 跳过模块
  # pytest.skip(msg="",allow_module_level=False)
  import sys
  import pytest

  if sys.platform.startswith("win"):
      pytest.skip("skipping windows-only tests", allow_module_level=True)
    


```




"""命名"""
# 类名、异常		XxxxXxxx  				大驼峰
# 常量	XXXX_YYYY    					全大写
# 模块、包、函数、变量	xxxx_xxxx		下划线或者小驼峰

"""特殊注释"""
# todo(name@mail.com):大师法师打发斯蒂芬 标记注释
# :type  解释器标识
num1:list = 3
num2 = 3  #type:list # 解释器会把str当做列表的形式，.会自动补全列表的方法和属性
# num1.append()
# num2.count()

# todo:接口测试基础框架—logging日志管理
"""接口测试基础框架"""
# unittest+Excel+ddt+logging+yaml

# TODO:logging日志模块
# 日志的形式：文件、console输出
# 日志的作用：记录bug和程序运行信息→定位bug、调试
"""logging日志模块：日志获取"""
# —日志级别和控制台输出：五种打印日志的方法，logging模块默认跟踪warning及其上的级别
# ——————DEBUG，输出详细运行情况，用于调试代码。					.debug()
# ——————INFO，输出重要运行情况，用于确认程序运行是否按预期进行	.info()
# ——————WARNING 潜在的问题（如“警告：内存不足”）				.warning()
# ——————ERROR 发生了错误，不过程序可以正常运行					.error()
# ——————CRITICAL，严重错误，程序终止							.critical()
# 使用logging打印可以体现程序运行逻辑
# logging运行逻辑图：py文件（执行代码，打印级别）————日志收集器————日志输出器（控制台或者文件）

import logging

#
# list1 = [110,112,119,120,10086]
#
# for num in range(5):
# 	logging.debug("debug：num={}".format(num))
# 	print(num)
# 	for id in range(10,50,10):
# 		logging.debug("debug：num={}".format(num))
#
#
# print(list1)
# logging.info("info：====")
#
#
# if 110 in list1:
# 	logging.warning("'110'跑进了list1列表")
# 	logging.error("error:打印的内容")
# 	logging.critical("critial:打印的内容")
#

# todo:日志收集器：输出到控制台
# 创建收集器对象，设置收集器收集等级
root_logger = logging.getLogger("list1")
root_logger.setLevel("DEBUG")

# todo:日志输出器：输出到控制台
# 创建输出处理器handler，并设置输出等级
stream_handler = logging.StreamHandler()
stream_handler.setLevel("INFO")		# 输出器只能输出收集器收集的信息

# 收集器加载输入器
root_logger.addHandler(stream_handler)

# 使用日志收集器获取日志
root_logger.debug("debug 级别的日志")
root_logger.info("info 级别的日志")
root_logger.warning("warning 级别的日志")
root_logger.error("error 级别的日志")
root_logger.critical("critical 级别的日志")

# todo:日志输出器：输出到文件
file_handler = logging.FileHandler('log.txt',encoding="utf-8")
file_handler.setLevel("INFO")
root_logger.addHandler(file_handler)


"""日志输出格式化"""
# 常用格式模板：
fmt ='%(asctime)s-%(filename)s-->line:%(lineno)d-%(levelname)s:%(message)s'
# 创建格式对象
formatter = logging.Formatter(fmt)
# 添加到输出器
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)


# 获取日志并格式化打印、写入文件
root_logger.debug("debug 级别的日志")
root_logger.info("info 级别的日志")
root_logger.warning("warning 级别的日志")
root_logger.error("error 级别的日志")
root_logger.critical("critical 级别的日志")

# todo 封装：
"""函数封装"""
def get_logger():
	"""
	参数，等级，fmt，文件：filename
	:return:
	"""
	logger=logging.getLogger()
	return logger

"""类封装
重点：要区分清楚：继承关系，	包.类，	包.函数，	类.成员
logging
logging.logger
logging.getLogger()		→返回RootLogger(Logger)对象，指定name则返回Logger对象
logging.Handler()	logging.StreamHandler()
logging.Formatter()		→Formatter对象
logger.addHandler()
logger.setLevel()
logging.Handler.setLevel()
logging.Handler.setFormatter()
"""
# print(type(logging.getLogger("1")))

class MyLogger(logging.Logger):
	def __init__(self,):
		"""参数，等级，fmt，文件：filename
		"""
		# 收集器
		logger = logging.getLogger()
		# 输出器
		handler = logging.FileHandler()
		logger.addHandler(handler)


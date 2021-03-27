"""接口文档："""
# URL格式：http://ip:port/futureloan/apiName
# ——————http://120.78.128.25:8766/futureloan/member/register
# 路径信息可以放到配置文件中，因为项目运行过程它是不会变化的。但是不同的项目会有不同的路径
# ————不放到yaml中？yaml中存放静态数据
# ————可以放到一个py模块中

"""json：-->str"""
# json 是一种与语言无关的数据交换的格式，
# ————格式：一个对象用{}表示、一对属性之间用:来分隔；一个数组用[]符号
# ————json格式的字符串用双引号、空为null、布尔值为true、false（全小写）

# json是用按js语言规则写的一种特殊标记的字符串，所以在其他语言中不能直接使用→json模块
# ————#如：d_dict=eval（'"mobile_phone"：true，"pwd"："12345678"，"type"：11'）
# ————在Python中会因为true被识别为引用而报错→需要用json模块来读取json格式的文本

# json模块：
import json

row_data = '{"pwd":"123456","user":"aria","is_student":true}'  # -->json格式的Python-str对象
print(type(row_data), row_data)
# 将json格式的python字符串对象转为Python字典对象：
dict_data = json.loads(row_data)  # -->python-dict对象
print(type(dict_data), dict_data)
# 将Python字典转化为json格式的Python字符串：
json_data = json.dumps(dict_data)  # -->json格式的Python-str对象
print(type(json_data), json_data)

# 总结：loads、dumps：<class 'dict'> dict ↔ <class 'str'> json-str
# ————dumps返回的不是json对象，而是json格式的字符串对象
# ————如果测试数据用json格式来写，加载数据时要用json.loads()来转换格式。
# ————如果接口入参是json格式，request.request(**,json )里json需要接收json字符串，需要用loads()来转换json字符串为字典后传入


"""logger使用："""
# 用途：日志文件用来记录错误和运行日志(info级上)，debug日志一般输出到控制台
# 用法：在关键的信息点记录日志——logger.error()、logger.info()

"""操作MySQL数据库："""
# ————测试注册成功用例需要在数据库进行验证、需要使用数据库没有的注册账号
# 操作数据库需要使用db-api，现在用pymysql:
# ————接口：base_url:http://120.78.128.25:8766/futureloan
# ————MySQL链接信息： 主机 120.78.128.25，port 3306，用户 future ，密码 123456
# ————连接数据库表futureloan.member

import pymysql
import copy

# a.建立连接
conn = pymysql.connect(
	host='120.78.128.25',
	port=3306,
	user='future',
	password='123456',
	charset='utf8',  # 不能使utf-8
	# database = 'future',
	cursorclass=pymysql.cursors.DictCursor  # 设置游标返回的数据类型为字典
)

# b.建立一个游标对象
cursor = conn.cursor()

# c.使用execute()执行sql语句
cursor.execute('SELECT * FROM futureloan.member where mobile_phone = "1" LIMIT 10;')
cursor2 = copy.copy(cursor)


# d.使用fetch进行查询数据：
# ————返回元组元素型元组（（）,（）,...），
# ————或者字典元素型列表[{},{},...]
# cursor.fetchone()		# 返回游标位置后的第一行数据
# cursor.fetchmany(5)		# 游标位置后指定长度数据
# cursor.fetchall()  	# 返回cursor.rownumber后的余下所有数据
# ————如果数据为空，fetch返回一个空元组
# 使用.rownumber操作游标位置：
# cursor.rowcount	# 返回游标队列里数据的总行数(该数值由cursor.execute()时赋值)
# cursor.rownumber		# 返回游标的位置：0，表示下一个fetchone为第一行数据，可以自己设置
# ————重复读取数据？新建游标并执行sql/copy未fetch的对象/设置游标位置rownumber的值

print(cursor.rowcount)
print(cursor.rownumber)
res = cursor.fetchall()
print(res)
print(cursor.rowcount)
print(cursor.rownumber)
cursor.rownumber = 3
cursor.rowcount = 3
print(cursor.rowcount)
print(cursor.rownumber)
res = cursor.fetchmany(5)
print(res)
print(cursor.rowcount)
print(cursor.rownumber)
cursor.execute('SELECT * FROM futureloan.member LIMIT 10;')
print(cursor.rowcount)

# e.关闭
cursor.close()  # 关闭游标，游标不能再执行数据库语句，但仍然是可读的（该对象仍然存在）。
# cursor2.close()
# cursor3.close()
conn.close()

"""参数化"""
# 使用python字符串方法进行参数化

"""数据中间层封装：middler ware"""
# 1. 初始化直接用配置文件
# 2. 封装数据中间层的目的：和项目有关系，不需要重复写大段代码
# 封装内容：config、yaml、logger、excel


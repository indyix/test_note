# 1.函数创建和调用
"""
def functionname(parameterlist1):    函数名：用于调用函数；
    ['''comments''']                函数注释，说明函数功能、传递的参数的作用，相对于def缩进
    [functionbody]                  pass：占位符

functionname(parameterlist2)
"""


def weekday():
    import datetime
    print("今天是星期{}".format(datetime.datetime.now().weekday()))


weekday()

# 2.形参和实参
'''
形参：定义函数时的参数1
实参：调用函数时传递的参数2
值传参：实参为不可变对象，函数调用不会改变实参的值：
    改变形参的值时新建了不同的内存地址的对象给形参param1，对实参prz无改变
引用传参：实参为可变对象，函数调用会改变实参的值。：
    把内存地址传了过去,：在函数里param1和pryy指向相同的内存地址,改变了该内存地址的值就改变了实参的值
（！！）通常要避免对引用参数的直接操作：赋值
'''


def link(param1):
    param1 += "jojo"
    print("函数内:", param1, id(param1))


# 值传参
prz = "dio哒"
print("传参前：", prz, id(prz))
link(prz)
link(prz)
print(prz)
print("传参后：", prz, id(prz))

# 引用传参
pryy = ["the world！"]
print("传参前：", pryy, id(pryy))
link(pryy)
link(pryy)
print(pryy)
print("传参后：", pryy, id(pryy))

# 3.位置传参、关键字传参、默认参数值
"""
调用函数时：
# 位置参数，调用时不指定接收实参的形参，会按顺序传参
#       要求：数量和依序位置一致，不然会报错
# 关键字参数：调用时指定接收实参的形参
# 定义函数时：
# 默认参数，以param=value的形式放在形参列表尾部
"""


def paramlink(name, stage, event, emotion="哈哈哈!!!"):
    print("{}在{}{},{}".format(name, stage, event, emotion))


# 位置传参：  #TypeError
# paramlink("cxk", "篮球场","唱、跳", "rap","music!")
# 关键字传参:
paramlink(name="太阳", event="爆炸了", emotion="amazing!", stage="仙女座星云", )
# 默认参数值：
paramlink("蔡徐申", "游泳池", "唱、跳、rap")

# 4 对参数的补充：
""" 
1. founctionname.__defaults__   查看函数的默认值参数的当前值
2. 可变对象作为函数参数默认值时，调用函数时对默认参数的修改会得到遗留
（！！）所以通常默认参数必须指向不可变对象，使每次调用函数有固定值, 如：kb1=None
"""
print(paramlink.__defaults__)


def kb(kb1=[1, 2]):
    kb1.append("33")
    print("当前的默认值是{},kb1的值是{}".format(kb.__defaults__, kb1))


kb()
kb()

# 5.可变参数*parameter 和**parameter
""" 
*parameter 调用函数时可接收任意个实参，并作为列表传递给parameter
    定义：def func(*para)
    调用：func("a",1,2,True)         func(列表/元组/集合)   func(*列表/*元组/*集合)
**parameter 调用函数时可接收任意个关键字参数，并作为字典传递给parameter
    调用：func(k1=v1, k2=v2, k3=v3)    func(**(字典型元组))    func(**{字典})

"""


def funckb(*tuple0):
    print(tuple0)


funckb(1, 2, "e", ["s,", True])
funckb([1, 2, 3, 4])
funckb({1, 2, 3, 4})
funckb(("a", "b", 1, 2, 3))

# 6.返回值
"""返回零个为None，返回多个为元组"""

# 7.局部变量和全局变量
"""
全局变量：函数外定义的变量能在函数内使用，并且是运行时最先被实例化的；
函数内定义的变量名和函数外定义的重合时，在函数内对该变量的操作不影响外部的变量
函数内定义的变量名被global修饰后，可以在外部使用，但这个变量只有在函数被执行时才会实例化
顺序：全局>global>局部
"""


def func1():
    print(1, message)  # b,  打印1


message = 1  # a,  全局变量，message为1


def func2():
    global message
    message = None  # c, message为空
    print(2, message)  # d, 打印空
    message = "haha"  # e， 为haha
    print(3, message)  # f, 打印haha


func1()
func2()
print(4, message)  # g, 打印haha

# 8. 匿名函数
"""
    @ 功能：笔记：dict、set
    @ author：古城
    @ create：20200422 01:00
"""

# 字典dict：也称关联数组、散列表(hash)
# 特点：“无序可变”，元素为键值对  key:value
#       没有索引（无序）(python3.6以上dict是有序的)
#       key唯一且不可变且不能用list、dict, 出现两次则只记住后一个值
#       value无限制（可变）

# 0. i1 = 5      i2 = i1 表示使i2指向i1指向的内存地址(5的id地址)，但两者并不是同一个引用，
i2 = i1 = 5
print(i2 == i1)
i2 = 6
print(i2 == i1)
# == 比较的是两者指向的对象的value值/实例,而不是地址值
x1 = 5
x2 = 5
print(id(x1), id(x2), x1 == x2)
y1 = [1, 2, "sd"]
y2 = [1, 2, "sd"]
print(id(y1), id(y2), y1 == y2)


class TestClass:
    def __init__(self):
        pass


s1 = TestClass()
s2 = s1
print(id(s1), id(s2), s1 == s2)
s2 = TestClass()
print(id(s1), id(s2), s1 == s2)

# 1. 创建字典
# 通过 {}，键值间用:
dict1 = {1: "阿尔法", 2: "赛普西斯"}
# 通过dict()函数
# 使用 = 构成多个键值对，键不能用数字
dict2 = dict(username="伊卡洛斯", pw="123456")
print(dict2)
# 使用一个字典型元组((k1,v1), (k2, v2),(k3, v3))
dict3 = dict(((1, "阿尔法"), (2, "赛普西斯"), (3, "艾娃")))
print("两元元组构成键值对", dict3)
# 使用zip()函数:zip(list1, list2)
dict4 = dict(zip([1, 2, 3], ["a", "b", "c"]))
print("zip:", dict4)
# 空字典
dict0a = {}  # 空字典
dict0b = dict.fromkeys([1, 2, 3, 4])  # 空值字典
# 2. 删除字典
del dict1  # 删除字典
dict2.clear()  # 清空字典
p3 = dict3.pop(2)  # 删除指定键的元素，并返回被删除的键值对的值
print("pop删除指定键值对并返回键值对的值", dict3, p3)
p4 = dict4.popitem()  # 删除一个元素，并返回该键值对元组
print("popitem删除键值对并返回键值对元组：", dict4, p4)
# 3. 访问字典
dict5 = {1: "asd", 2: "qwe", 3: "zxc"}
print("字典名：", dict5)  # 通过字典名
print("通过键名访问字典元素的键值：", dict5[3])  # 通过键名
print(dict5.get(5, "没有这个键名"))  # 通过dict.get(key[,无key时返回值])
# 遍历字典
for item in dict5.items():
    print(item)  # .items()      每个item是一个元组
for k1, v1 in dict5.items():
    print(k1, v1)  # .items()      每个k1，v1是元组的元素
print(dict5.keys())  # .keys()   返回keys
print(dict5.values())  # .values() 返回values
# 4. 删增改字典元素
del dict5[1]
dict5[4] = "asdadd"
dict5[4] = "asdmodify"
print("删增改字典元素", dict5)
# 5. 字典推导式
dict6 = {i: i ** i for i in range(4)}  # {0:1, 1:1, 2:4, 3:9 }    注：0**0处理为1
print(dict6)

# 集合set和frozenset，用{}
# 特点：无序、元素唯一
# set是可变集合、frozenset是不可变集合

# 1. 创建set:元素唯一、无序
set1 = {1, 1, "战列巡洋舰", "虚空光辉舰", True}  # 使用{}
set0 = set()  # 空集合                        # 空集合要用set()，不能用{}
set2 = set([1, 1, 3, 5, 6])  # set(iterable),推荐方法
print("set元素唯一且无序：", set0, set1, set2)
# 2. 增删集合的元素
set2.add("added")  # .add(元素) 增加元素
# set2.add([1, 5, 6])            # 不能使用可迭代对象作为.add()的参数,因为不能hash()
del set1
set2.pop()  # .pop() 对于有索引的对象不指定参数时等价于.pop(-1)，对于dict需要指定key，set则不指定
print("set2被pop后", set2)
set2.remove(3)
set2.clear()
list00 = [1, 2, 3, 4, 5, 6, 7]
print(list00.pop())
# 集合运算
set3 = {5, 6, "a", "b", True}
set4 = {"a", "b", 1, "中国雷达"}
print("交集：", set3 & set4)  # 交集，True→1
print("并集：", set3 | set4)  # 并集，1→True
print("差集：", set4 - set3)  # 差集
print("对称差集：", set3 ^ set4)  # 对称差集

# 其他（预习视频）
'''1：空字典'''
# d = {}
# print(type(d))
'''2：key不能用list和dict类型'''
d1 = {1: 10, 0.02: 0.022, 'name': ['a', 'b', 'c'], ('tuple1',): {1: 1}, }
# []:2}  #TypeError: unhashable type: 'list'
# print(d1)
'''3：元素存储是无序：指输出顺序不同于插入值的顺序,要想有序可用Ordereddict'''
# for i,k in d1.items():
#     print(i,k)
'''4：访问元素，根据key和value'''
# print(d1[1])
'''5:key唯一（1→True，0→Flase,遇到重复的key，会用前面的key和后面的value）'''
d2 = {1: 10, 0: 0.022, True: ['a', 'b', 'c'], False: {1: 1}, }
# print(d2)
# print(len(d2))
'''6:遍历字典.items()、.keys()、.values()'''
##.fromkeys()
d3 = dict.fromkeys(['key1', 'key2', 'key3'])  ##以列表元素为key创建值为空的字典
# 字典元素操作：
d4 = {1: 'python29', 'teacher': ['sekiro', 'niho', 'dmc'], 'vip': {'A': '路人甲', 'B': '路人乙', 'C': '张三'},
      'score': (88, 99, 100)}
##查：根据key进行查询、d.get(key[,default])：default，key不存在时返回这个元素，缺省为None
print(d1, '\n', d2, '\n', d3, '\n', d4)
'''
改：dict[oldkey] = newvalue
增：dict[newkey] = newvalue
删：dict.pop(key)删除键值对，  dict.clear()清空字典，  dict.popitem()随机删除某个键值对'''
'''其它用法：'''
# items()   以列表返回可遍历的键值对元组数组
# print(d4.items())
# print(type(d4.items()))
# keys()    以列表返回字典所有的键
# print(d4.keys())
# print(type(d4.keys()))
# values()  以列表返回字典所有的值
# pop(key)  按key删除指定键值对
# d4.pop(1)
# del dict[key]   按key删除指定键值对
# del d4['teacher']
print(d4)

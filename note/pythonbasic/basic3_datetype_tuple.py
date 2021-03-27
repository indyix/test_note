"""
    @ 功能：笔记：tuple
    @ author：古城
    @ create：20200422 01:00
"""
# tuple: 不可变序列，元素可重复，特点是“内部元素有序不可变”，相比列表可以作为字典的键
# 数据类型？储存数据用的
# 使用场景：保存程序中不可修改的内容
# 注意：数据类型的“不可变”，是指作为引用数据类型的变量在栈中指向的内存地址不可变。
    # 如tuple("a",[1,2,3])[1][2] = 5是可行的，tuple仍指向ram("a")、ram([1,2,3])，但[1,2,3]的指向中ram(3) 变成了ram(5)

# 1.创建元组：通过赋值语句创建：小括号不是必须的，单元素要加逗号，
tupleb = ()                     # 空元组
tuple0 = ("t",)                 # 单元素元组
tuple1 = (1,0,0.0002,'str',True,True,False,(1,),[2,],{'key1':'15'},{'set1','set2'})     # 使用()
tuple2 = 1,0,0.0002,'str',True,True,False,(1,),[2,],{'key1':'15'},{'set1','set2'}  # 使用 ,
tuple3 = tuple(range(3, 10, 2))
tuple4 = tuple([1, "a", True])                 # 使用tuple()函数和可迭代序列
tuple5 = tuple(x for x in range(10))            # 使用元组推导式
tuple3_3 = tuple(tuple(x for x in range(3)) for y in range(3))  #套用元组推导式：二维元组
print("二维元组：", tuple3_3)
# 2.删除元组：
del tuple1
# 3.编辑元组：
    # 3.1 元组元素不可编辑
        # 如tuple2[5] = "edittuple"会报错，列表的切片赋值 .append() .extend() .insert() .remove() .pop()等操作元素的方法也不能用
    # 3.2 但元组本身是可以“编辑”的
tuple2 = 1,0,0.0002,'str',True,True,False,(1,),[2,],{'key1':'15'},{'set1','set2'},"after"   # 通过重新赋值编辑整个元组
tuple2 = tuple2 + ("add",)              # 通过 + 进行元组整体间的拼接（不能拼接元组和其他序列）
# 4.访问元组：
print(tuple2)                   # 通过元组名访问整体
print(tuple2[4])                # 通过索引访问元素
print(tuple2[3:7:1])            # 通过切片访问元素
    # 遍历元素： enumerate() 将一个可遍历的数据对象组合为一个具有下标的索引序列,序列的元素是二元素的tuple
print(list(enumerate(tuple2)))
print(type(list(enumerate(tuple2))[1]))
for index0, item0 in enumerate(tuple2):
    if index0 == 9:
        print(item0)

l3 = [1,2,3,4]
l3[0:3] = [3,4,5]
print("列表可以用切片进行赋值", l3)
# 5.拆包：
s1, s2, s3 = (["a", "b"], 2, ("PI", ))
print(s1, s2, s3)


# 其他（预习视频）
''' 1：空元组,长度0'''
# t1 = ()
# print(type(t1))
# print(len(t1))
''' 2：一元素元组要在后面加上逗号，不然会按元素的数据类型进行识别'''
# t2 = (1,)
# print(type(t2))
# print(len(t2))
''' 3：元组元素可以是任意数据类型'''
# t3 = (1,0.0002,'str',True,(1,),[2,],{'key1':'15'},{'set1','set2'})
# print(type(t3))
# print(len(t3))
''' 4 元组的操作：特性：有序不可变（有序：有索引号；不可变：元素值不能更改和删除）'''
t4 = (1,0,0.0002,'str',True,True,False,(1,),[2,],{'key1':'15'},{'set1','set2'})
# print(t4[-2].get('key1')[1])      #嵌套取值
# print(t4[2:7:2])                   #切片tuple[start:end:step]
# 常用方法：
    ##获取元素的索引值.index(元素)
# print(t4.index(0.0002))     #结果：2
# print(t4.count(1))          #结果是：3：把1当做True来计数了
# print(t4.count(0))          #结果是：2：把0当做False来计数了



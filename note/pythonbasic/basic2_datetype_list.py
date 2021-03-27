# coding = utf-8
# auth: SSRGray
# 列表list：使用最频繁的数据类型，可以完成大多数的集合类的数据结构实现。元素支持数字型、字符型、列表、元组等数据类型
# 与元组的不同：列表可变、单元素不用加逗号
#特性
''' 1：空列表,长度0'''
# t1 = []
# print(type(t1))
# print(len(t1))
''' 2：一元素列表不用在后面加上逗号'''
# t2 = [1]
# print(type(t2))
# print(len(t2))
''' 3：列表元素可以是任意数据类型'''
# t3 = [1,0.0002,'str',True,(1,),[2,],{'key1':'15'},{'set1','set2'}]
# print(type(t3))
# print(len(t3))
''' 4 列表的操作：特性：有序可变（有序：有索引号；可变：元素值可增删改）'''
t4 = [1,0,0.0002,'str',True,True,False,(1,),[2,'asd'],{'key1':'15'},{'set1','set2'}]
''' ##  访问元素：索引和切片'''
# print(t4[-2].get('key1')[1])      #嵌套取值
# print(t4[2:7:2])                   #切片tuple[start:end:step]
# print(t4[::-1])                    #倒序输出
''' ## 增加元素.append(元素)  .insert(index,元素)   .extend(iterable)   加号 '''
# t4.append('+1')             #每次调用在尾部增加且只能增加一个元素
# t4.insert(2,'insert')       #指定位置插入，其他元素后挪
# t4.extend(('a','b','c'))    #后接合并列表
# t4=[1,2,3] + t4             #连接号合并列表
# t4[-7].append('efg')
# print(t4)
''' ## 修改元素:用赋值语句'''
# t4[1] = 'alpha'
# print(t4)
''' ## 删除元素.pop(index)  .clear()    .remove(value)'''
# t4.pop(1)                       #删除指定索引的元素，不指定则删除最后一个
# t4.clear()                      #清空列表
# t4.remove(0)
# print(t4)
# print(t4.clear())
# print(t4.pop(-1))                 #注意：str.pop(index) 会删除str中指定索引的位置的字符，同时会返回被删除的value
                                    #而.clear()、.remove(value)  等往往返回是None
''' ## 其它用法：'''
     ## 获取元素的索引值    .index(元素)  .count(元素)   sum()
print(t4.index(0.0002))   # 结果：2      确定元素所在索引位置
print(t4.count(1))          # 结果是：3：把1当做True来计数了   统计列表里该元素的个数
print(t4.count(0))          # 结果是：2：把0当做False来计数了
print(sum([1, 2, 3]))       # sum()
    ## 排序
        # .sort(reverse = True)  降序排列原变量
        # sorted(iterable, reverse = Flase)  返回升序排列的结果，默认升序, 不改变原变量
lists = [1,3,1,5,4]  # ["s", "b","a"]
lists.sort()
print(lists)
listj = sorted(lists, reverse=True)
print(listj)

# -*- conding: utf-8 -*-
# @Author   : SSRGray
'''for循环:可遍历所有序列的项目和可迭代对象
格式：
for item in iterable：
    circle_body
'''

for item in 'faster':
    print(item)
'''注意 in dict 时默认访问keys，相当于 in dict.keys()  '''
odd_sum = 0
for i in range(1,11,2):
    odd_sum += i
print(odd_sum)
# range(m,n,k)，生成m起到n-1步长为k的可迭代对象range
print(type(range(1,2)))
# 嵌套
matrix = [(1,2,3),('a','b','c'),([1],(2,),{3:'san'})]
for xindex in matrix:
    for yindex in xindex:
        print(str(yindex),end = ',')
    print()
'''不换行输出end = 'sep'   '''

# 练习
# 输出九九乘法表
for y1 in range(1,10):
    for x1 in range(1,y1+1):
        print('{}×{}={}'.format(x1,y1,y1*x1),end=' ')
    print()
# 冒泡算法
list1 = [10,9,11,5,23]
## 算法分析：
## 第一轮:相邻两两比较，较大的放后面
## 第二轮:相邻两两比较，较大的放后面
## ...
## ...                                   共len(list1)-1轮
for i in range(len(list1)-1):
    for j in range(len(list1)-1):
        if list1[j] > list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
print(list1)
## 提高性能:
for i in range(len(list1)-1):
    for j in range(0,len(list1)-1-i):
        if list1[j] > list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
print(list1)
# 1,2,3,4能组成多少个不重复数字的三位数？
## 个位，ge 十位，shi 百位，bai
count = 0
L=[]
for ge in range(1,5):
    for shi in range(1,5):
        for bai in range(1,5):
            if ge!=shi and shi!=bai and ge!=bai:
                L.append(100*bai+10*shi+ge)
                count += 1
print("共有{}个数符合要求：{}".format(count,L))
# 打印三角形:
     #    *         #算法：总行数-i个空格+2*i-1个*
     #   ***
     #  *****
     # *******
all_line = 10
for hang in range(1,all_line+1):
    for lie1 in range(1,all_line+1-hang):
        print(' ',end='')
    for lie2 in range(1,2*hang):
        print('*',end='')
    print()
# 打印圆：打印图形：算法a^2+b^2<=r^2
for i in range(1,10):
    for j in range(1, 10):
        if (i-5)*(i-5)+(j-5)*(j-5)<=16:
            print('正',end='')
        else:
            print('　',end='')
    print()


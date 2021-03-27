# -*- conding: utf-8 -*-
# @Author   : SSRGray

# Python运算符：算术运算符、比较（关系）运算符、赋值运算符、逻辑运算符、成员运算符、
# 位运算符、身份运算符、运算符优先级

'''1. 算术运算符：+ - * / % '''
''' 数字型变量运算'''
'''+   字符串拼接，列表拼接'''
# print('sss' + 'aaa')
# print([1, 2, 3] + [4, 5, 6])
'''  *  多次输出'''
# print('射惠主义好啊！' * 3)
''' %   模运算、取余运算'''
# print(int(10086.123 / 1 % 10))  # 取个位/1
# print(int(10086.123 / 10000 % 10))  # 取万位/10000
# print(int(10086.123 / 0.01 % 10))  # 取百分位/0.01
'''2. 赋值运算符：= += -= *= /= '''
'''3. 关系运算符：> >= < <= == !=，可用于字符串之间'''
# print('get' == 'Get')     #False
# print(0 == False)         #True 0==Flase，1==True
# print(False == 0)         #True
# print([] == False)        #False
# print(() == False)        #False
'''4. 逻辑运算符：and     or     not '''
'''5. 成员运算符：in      not in'''
# print('1' in '10086') #True
# print('p' not in (1,2,'python')) #True

'''
针对字典，判断的是key是否存在： in dict 等价于 in dict.keys()
判断是否在values里用： in dict.values()  '''


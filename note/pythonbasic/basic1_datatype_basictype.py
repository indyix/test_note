#coding=utf-8
# 基本数据类型和字符串相关函数
# 用数据类型:数字、布尔值、字符串shr、元组tuple、列表list、字典、集合set
##数字:整数int、浮点数float
    #查看变量类型：type()
##布尔值bool：True、Flase（首字母大写）
    #非零值、非空字符串、非空元组、非空列表、非空字典---->True
    #零、空序列（空字符串、空元组、空列表、空字典）、None、自定义对象的实例---->Flase
##字符串str：
    #嵌套时，单引号双引号可相互嵌套，三引号可嵌套两者
    #空字符串''，拼接+，支持转义字符\：\n、\r、\t
        #不转义：\\，r''，R''
    #str有索引值用以访问字符串元素字符str[0]，从0到length-1，反序从-1到-length
str1 = '10086'
print(str1[-5]==str1[0]) if str1 == False else print('15')
#切片函数，访问序列中一定范围的元素
    #格式sname[start:end:step]
    #取左不取右:从start起每step取一个取完索引值end-1后结算
    #负数从尾部-1往前算
str1_2 = 'hello py thon'
print(str1_2[4:10:1])
str1_3 = '0123456789a'
print(str1_3[:3])
print(str1_3[::5])
print(str1_3[-11:-4:2])
print(str1_3[6:8]+str1_3[9:13])
#字符串格式化:P145：
    #占坑格式为%s字符串、%d十进制整数、%f浮点数，%x、%c、%e、%%
tembfh = '姓名：%s，    年龄：%d，    金额：%f   。'   #定义模板
person = ('张三',18,500.59)                       #要转化的内容
print(tembfh%('张三',18,500.59))
print(tembfh%person)
print('adress:%s,sex:%s,age:%d'   %   ('地址','性别',18))   #输出：  格式 % 内容
person2 ='adress:%s,sex:%s,age:%d'   %   ('地址','性别',18)
print(person2)          #可以直接将 格式%元组 输入给变量

    #format()方法：需要用{}占位，调用的{}必须都有传值(传入内容量>占位符)
        #格式：{[index][:[fill]aligin][sign][#][width][.precision][type]}
        #index索引号要么全有要么全无，对应传入索引值从0开始、[:[fill填充]aligin对齐方式<>=]  [type:s、d、f、c、%、]
        #rg：    "gsm:'tcm'<5.2s"

person3 = tembfh.format('张三',18,500.59)
print(person3)#格式化没生效
temdkh = '姓名：{:s}，    年龄：{:d}，    金额：{:f}'
person4 = temdkh.format('张三',18,500.59)
print(person4)
print('姓名：{:s}，    年龄：{:d}，    金额：{:f}'.format('张三',18,500.59))
                    #输出： 格式.format(内容)
# def xxb():
#     name = input('name:')
#     age = input('age:')
#     address = input('adress:')
#     hobby = input('hobby:')
#     salary = float(input('salary'))
#     work_year = input('work_year')
#     print('''your information is:
#         name:{1}
#         age:{2}
#         address:{3}
#         hobby:{4}
#         salary:{5:0>8.5f}
#         work_year:{6}'''.format(name,age,age,address,hobby,salary,work_year,work_year))
# xxb()
# 字符串常用函数
str1_4 = 'hello python1 hahaha  *\n'
# 检索字符串
    # .find() :检索是否包含指定字符串，有则返回第一个的首字符的索引，否则返回-1
        #格式  str.find('索引字符'[,start[,end]])         注意：起始位置不会改变索引值，是改变检索的始终点
    # .index() 同.find()，但要查找的内容不存在时会抛出异常，
    # .rindex()，同.index()，但从右边开始查找
print(str1_4.find('py')+str1_4.find('ss')+str1_4.find('h',3))
    # .count() 返回指定字符串在目标字符串中出现的次数          str.count('sub'[,start[,end]])
    # .replace()改变某个字符后返回，默认全改变（原变量不变,也不能通过切片改变）
print(str1_4.count('h')-str1_4.count('o',7))
print(str1_4.replace('h','k'))
print(str1_4)
# 操作元素返回字符串
    # .split()以分隔符分割字符串，返回一个列表    str.split([sep[,maxsplit]])，
        # 不指定分隔符sep时按空白符(' '、\n、\t)分割且连接在一起的空白符只分割一次；指定则遇到一次分割一次
        # maxsplit，最多分割次数
    # join()返回以分隔符分隔合并的字符串  sep.join(iterable)
url = ','.join(['http://yuming/login','post',"参数1","参数2"])
print(url)
print(url.split(',',2))
print(''.join(["555","aaa"]))
print(range(1,10,3))
    # range() 返回的是一个可迭代对象
    # .strip()，去掉首尾的指定符号，不指定则去掉空白符，指定则去掉指定字符串
        # 左侧？lstrip()，右侧？rstrip()
        # 只能去掉首尾的字符。去掉全部的某个字符？用split()按字符分隔后再用""进行join()
print(str1_4.strip())
print(str1_4.strip('*'))
print(str1_4.strip('\n'))
    # upper()、lower()，全大写、小写返回，swapcase()大小写互换
    # 切片：截取字符串并返回str[start:end:step]
    # len()字符串长度
print(len(str1_4))
    # startwith()、endwith()，以关键字符开头、结尾则返回True，否则返回Flase
    # isdigit()，只包含数字型字符则返回TRUE，否则Flase
    # islower()、isupper()
print(str1_4.startswith('e'))
print(str1_4.startswith('e',1))
print(str1_4.endswith('n'))
print(str1_4.endswith('n',5,12))
print(str1_4.isdigit())
print('111'.isdigit())
    # .encode()字符串编码后返回（简中为gb2312）
        # 格式：str.encode([encoding='utf-8'][,errors='strict'])
            # encoding指定要转成的格式，errors指定错误处理方式：strict抛出异常、ignore忽略非法字符、replace用？代替非法字符
            # 默认为utf-8，和strict,b''表bytes对象
    # .decode()解码；解码采用的字符编码要和编码时一致
remmf = 'rem是我老婆'
remmf_engbk=remmf.encode(encoding='gbk',errors='replace')
print('编码：',remmf_engbk)
remmf_degbk=remmf_engbk.decode(encoding='gbk',errors='replace')
print('解码：',remmf_degbk)
print('不同编码规则：',remmf_engbk.decode(encoding='utf-8',errors='replace'))  #不同编码规则
        # ps：python中字符串str有两种形式：
            # Unicode字符（ASCII或其他，在内存中显示为unicode字符：rem是我老婆）
            # bytes（二进制数据，在网络传输和磁盘储存用bytes类型： b'rem\xca\xc7\xce\xd2\xc0\xcf\xc6\xc5'）

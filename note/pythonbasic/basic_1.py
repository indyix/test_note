#标识符：数字、字母、下划线；不能用数字开头；不能包含关键字
#标识符包含：项目名、模块名、包名、类名、函数名、变量名
    #python是弱类型语言，变量数据类型可直接通过赋值来声明
import keyword

print(keyword.kwlist)
    #变量名：1)要见名知意,2)引用变量前要先声明
age = 10
nianling = 20
class_2019 = 50
#行和缩进：用行控制代码起始；缩进表示层级
if age <18:
    print("younger")
else:
    print('older')
#引号
    #表字符串
s_1="第一行"\
"被拼接的行"
s_2="zfc2"
s_3='''注释1
换行'''
    #三引号能表内容全为字符串：包括空格、换行，可用于注释多行代码
print(s_3)
    #双引号、单引号可用\拼接，可用于注释单行代码
print(s_1)
# 注释快捷键：Ctrl+/
#输出print
print('''111
222
333''','h2',"h3")
#输入input
s = input("please input")
print(s)



#作业：
"""
一、下面那些不能作为变量？
1、find     2、 _num    3、7val        4、add.       5、def     
6、pan      7、-print   8、open_file   9、FileName   10、9prints  
11、INPUT   12、ls      13、user^name  14、list1     15、str_
16、_888    17、is      18、true       19、none      20、try  
二、请描述一下变量的命名规范，（简单题）
三、python如何如何添加注释
四、把学的python基本语法，总结成笔记（以后每次课都要整理）

"""
#答案：
"""
一：
不符合命名格式：7val    add.     -print     9prints   user^name   is 
使用关键字：def is try
二：
组成为字母、数字和下划线，不能以数字开头且不能使用系统关键字。
三：
方法：  #注释内容     或者直接用字符串进行注释
四：
今天基本语法总结：print()、input()、print(keyword.kwlist)
"""



# -*- conding: utf-8 -*-
# @Author   : SSRGray
#if循环

'''条件循环：
while 条件表达式:
    循环体
    '''
# while True 死循环
# while Flase 不循环
# while []/()/{}/'' 不执行
# while [1]/(2,)/{1:'name'}  死循环
#结束死循环的方法：
import random

''' 应用A：条件不恒定：1.引入变量在循环体内改变；2.变量与while后面的条件相结合；'''
# # 1.
# count = 3
# while count:
#     print(count)
#     count -=1
# #2.
# count1 = 10  #询问次
# ct = 0    #满足条件的人数
# while count1:
#     count1 -= 1
#     sex = input("are you a girl?y/n")
#     if sex == 'y':
#         age = input('age in 10~12?y/n')
#         if age == 'y':
#             ct += 1
# print(ct)

''' 应用：条件固定：1.引入bresk和continue；2.添加内部判断条件'''
#1.break
# i = 0
# while True:
#     i += 1
#     if i%2 == 0:
#         continue
#     else:
#         print('第' + str(i) + '次打印')
#     if i == 9:
#         break


# 练习：人机对拳:“猜拳娶老婆！！”
role_dict = {1:'羽川翼',2:'小鸟游六花',3:'蕾姆'}
cq_dict = {1:'剪刀',2:'石头',3:'布'}
# score0 平局次数；score1 玩家胜次；score2 对手胜次
score1 = score2 = score0 = 0
print('game start!')
# 选择对手
pc_index = int(input("选择你的对手:1:'羽川翼',2:'小鸟游六花',3:'蕾姆'"))
print("你的对手是{}".format(role_dict[pc_index]) + '：')
while True:
# 玩家出拳
    cq = int(input("请出拳：1:'剪刀',2:'石头',3:'布'"))
    print("出拳："+cq_dict[cq])
# 对手出拳
    pccq = random.randint(1,3)
    print(role_dict[pc_index], '出拳:', cq_dict[pccq])

# 判断胜负
#   1剪刀2石头3布   玩家赢 -2 or 1
# 玩家：1   2   3
# 对手：3   1   2
#      -2   1   1
#                     对手赢-1 or 2
# 玩家：1    2    3
# 对手：2    3    1
#      -1   -1    2

    if (cq-pccq) in (-2, 1):
        score1 += 1
        print('you win！')
    elif (cq-pccq) in (-1, 2):
        score2 += 1
        print('you lose！')
    else:
        print('no winer。')
        score0 += 1
# 是否继续？
    again = input('again?y/n')
    if again == 'y':
        continue
    else:
        print('你赢了{}次, {}赢了{}次, 平局{}次'.format(score1, role_dict[pc_index], score2, score0))
        if score1-3 > score2:
            print('恭喜你！{}是你老婆了(>.<)!!!!'.format(role_dict[pc_index]))
        break


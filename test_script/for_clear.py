import random


choice=['杜易训','王倩龙', '司宇豪','段紫薇','刘智博','肖洒','杨宇航','胡志衍','刘俊雄','陈佩华','胡云翥']
alloc={0:1,1:1,2:2,3:2,4:2,5:2}
tasks=[
'周一、周三、周五垃圾处理+茶水桶清理+日常消毒',
'周二、周四、周六垃圾处理+茶水桶清理+日常消毒',
'周六擦拭大门玻璃',
'周六所有绿植打理+浇水+办公室地面打扫+会议室等公区整理',
'周六茶水桶+饮水机清理',
'周六清理碎纸机打印机小票+办公室消毒+咖啡机清理']

if __name__ == '__main__':
    print('乔迁：监督完成任务及协助')
    for i in range(6):
        task=tasks[i]
        workers ="+".join([choice.pop(random.randint(0, len(choice) -1)) for p in range (alloc[i])])

        print(workers+':'+task)
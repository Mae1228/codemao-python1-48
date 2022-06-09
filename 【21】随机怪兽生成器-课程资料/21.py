''''''
'''
len(列表)：获取列表的长度
列表嵌套：列表中的元素也可以是列表
    访问元素：列表[下标][下标]
列表.pop(下标)：移除列表中的一个元素，再返回该元素的值
            如果缺省下标默认移除最后一个元素
a,b=b,a：实现变量a与变量b的交换变量的值
练习题：
    A 
    B 
    B       C


'''

'''练习1'''
# import random
# mylist=[1,45,'a','fd',3,'s']
# a=random.randint(0,len(mylist)-1)
# print(mylist[a])




'''练习2'''
# import random
# name=['时空魔神', '海底猿人', '植物怪兽', '火山怪鸟', '刺客超兽']
# where=['猪圈', '厕所里', '房顶上', '办公室']
# doing=['引起大规模停电', '抄作业', '喜极而泣', '偷西瓜', '玩火自焚', '倒立狂奔']
# n=random.randint(0,len(name)-1)
# w=random.randint(0,len(where)-1)
# d=random.randint(0,len(doing)-1)
# print(name[n],'在',where[w],doing[d])





'''访问元素'''
# mylist=[['阿短','编程猫','绿豆'],'绿豆',['阿短','编程猫']]
# print(mylist[2][0])
# print(mylist[2])





'''练习3'''
# mylist=[['codemao',5],['列表',2],0]
# print(mylist[0][1],mylist[1][1],mylist[2],mylist[0][0])





'''pop()'''
# mylist=[['阿短','编程猫','绿豆'],'绿豆',['阿短','编程猫']]
# x=mylist[0].pop(2)
# y=mylist.pop(2)
# print(x,y,mylist)




'''练习4'''
# mylist=[['codemao',5],['列表',2],0]
# a=mylist[0].pop(1)
# b=mylist[1].pop(1)
# c=mylist.pop(2)
# d=mylist[0].pop(0)
# print(a,b,c,d)
# print(mylist)




'''a,b=b,a'''
# a=3
# b=7
# print('初始值：',a,b)
# a,b=b,a
# print('交换后：',a,b)




'''变量交换'''
# a=3
# b=7
# print('初始值：',a,b)
# t=a
# a=b
# b=t
# print('交换后：',a,b)





'''项目'''
# import random
# mylist = [['时空魔神', '海底猿人', '植物怪兽', '火山怪鸟', '刺客超兽'],
#           ['猪圈', '厕所里', '房顶上', '办公室'],
#           ['引起大规模停电', '抄作业', '喜极而泣', '偷西瓜', '玩火自焚', '倒立狂奔']]
# temp=[[],[],[]]
# while True:
#     if len(mylist[0]) !=0 and len(mylist[1]) !=0 and len(mylist[0]) !=0 :       #三个子列表都不为空
#         a=input('***Press Enter***见证怪兽的时刻到了：')
#         if a=='':
#             n=random.randint(0,len(mylist[0])-1)        #下标
#             w=random.randint(0,len(mylist[1])-1)
#             d=random.randint(0,len(mylist[2])-1)
#             name=mylist[0].pop(n)       #删除并记录
#             where=mylist[1].pop(w)
#             doing=mylist[2].pop(d)
#             temp[0].append(name)        #添加到新列表中存储
#             temp[1].append(where)
#             temp[2].append(doing)
#             print(name,'在',where,doing)
#         else:
#             break
#     else:
#         if len(mylist[0]) == 0:
#             mylist[0],temp[0]=temp[0],mylist[0]
#         if len(mylist[1]) == 0:
#             mylist[1],temp[1]=temp[1],mylist[1]
#         if len(mylist[2]) == 0:
#             mylist[2],temp[2]=temp[2],mylist[2]




'''---------------------------------------------------------------------------------------------------------------------------'''




















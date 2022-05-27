''''''
'''
常用调试命令：
    p 变量名
        打印当前变量的值
    c：continue
        继续执行直到遇到下一条断点语句
    s：step
        执行下一条语句，若为函数调用，则只执行函数的第一句，进入函数中
    n：next
        执行下一条语句，若为函数调用，则执行函数全部内容
    q：quit
        退出调试并结束运行

布尔类型时计算：
    True：对应的数字是1
    False：对应的数字是0

random.choice()：传入列表，元组或字符串，返回随机选择的元素


'''

'''p 变量名'''
# import pdb
# a=1
# pdb.set_trace()
# for i in range(10):
#     a+=i





'''练习1'''
# def thief_is():
#     for i in ['a','b','c','d']:
#         a=i!='a'
#         b=i=='c'
#         c=i=='d'
#         d=i!='d'
#         # print(a,b,c,d)
#         h=a+b+c+d
#         if h == 3:
#             print('thief is',i)
#             break
#
# thief_is()






'''random.choice()'''
# import random
# print(random.choice([1,2,3,5,9]))
# print(random.choice((1,2,3,5,9)))
# print(random.choice('随机选择元素'))






'''练习2'''
# import random
# def luckynums(numlist):
#     lst=[]
#     for i in range(len(numlist)):
#         for j in range(i+1,len(numlist)):
#             lst.append(numlist[i]+numlist[j])
#     return lst
#
# def luckycouple(numlist,lucky):
#     for i in range(len(numlist)):
#         for j in range(i+1,len(numlist)):
#             if numlist[i]+numlist[j]==lucky:
#                 return numlist[i],numlist[j]
#
# numlist = [7, 11, 2, 15, 21, 14]
# print('球员有：',numlist)
# res=luckynums(numlist)
# print('幸运数字有：',res)
# lucky=random.choice(res)
# print('幸运数字为：',lucky)
# print('两名幸运球为：',luckycouple(numlist,lucky))






'''练习3'''
# import time
# import random
# def luckynums(numlist):
#     lst=[]
#     for i in range(len(numlist)):
#         for j in range(i+1,len(numlist)):
#             lst.append(numlist[i]+numlist[j])
#     return lst
#
# def luckycouple(numlist,lucky):
#     for i in range(len(numlist)):
#         for j in range(i+1,len(numlist)):
#             if numlist[i]+numlist[j]==lucky:
#                 return numlist[i],numlist[j]
#
# def luckycouple2(numlist,lucky):
#     for i in range(len(numlist)):
#         a=lucky-numlist[i]
#         if a in numlist:
#             return numlist[i],a
#
# numlist = [7, 11, 2, 15, 21, 14]
# print('球员有：',numlist)
# res=luckynums(numlist)
# print('幸运数字有：',res)
# lucky=random.choice(res)
# print('幸运数字为：',lucky)
# t1=time.perf_counter()
# print('方法一：两名幸运球为：',luckycouple(numlist,lucky))
# t2=time.perf_counter()
# print(t2-t1)
# t3=time.perf_counter()
# print('方法二：两名幸运球为：',luckycouple2(numlist,lucky))
# t4=time.perf_counter()
# print(t4-t3)





'''-----------------------------------------------------------------------------------------------------------------------------------------'''























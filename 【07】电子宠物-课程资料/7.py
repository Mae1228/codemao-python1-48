''''''
'''
while循环：循环结构可以让计算机重复执行某些特定的操作
    语法表示：
        while 判断条件:
            条件为真（循环体）
        条件为假
    循环体：重复内容

死循环：
    无限循环，指永远无法结束的循环，循环结构下方的语句永远不会被执行
    造成死循环情况：
        判断条件设置不合理
        判断条件永远成立True
    语法表示：
        while True/判断条件:
            条件为真（循环体）

break：退出循环
    只能再循环结构中使用，否则计算报错
    执行break语句则退出循环执行循环外的语句

random.randint(小,大)：随机产生一个整数
    必须在顶部写上import random
            
练习题：
    B
    B
    B

'''

'''练习1'''
# a=1
# while a<4:
#     print(a)
#     a+=1
# print('数完了')






'''练习2'''
# a=1
# while True:
#     print(a)
#     if a==50:
#         break
#     a+=1






'''项目'''
# # 导入随机库
# import random
# #初始化
# t=100       #体力
# n='fish'    #名字
# egg=0       #当下产卵量
# eggs=0      #总产卵量
# #输出
# print('小金鱼'+n+'陪你玩耍！')#拼接：逗号，加号
# #循环
# while True:
#     if t<=0:
#         print('太累了，不行了')
#         break
#     if t>200:
#         print('吃的太多，受不了了')
#         break
# # 输入
#     a=input('要小金鱼'+n+'做什么:')
# #三种情况的判断：多分支 if elif  else
#     if a == 'eat':
#         t+=random.randint(10,15)
#         print('什么东西，真香')
#     elif a == 'lay':
#         t-=random.randint(15,20)
#         egg=random.randint(10,20)
#         eggs+=egg
#         print('产下了' + str(egg) + '颗卵')
#     else:
#         print('哎？'+n+'不知道这是什么意思呀')
# #输出总产卵量
# print('产卵总数:' + str(eggs))


'''---------------------------------------------------------------------------------------'''













































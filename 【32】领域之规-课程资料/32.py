''''''
'''
python中，变量有全局变量和局部变量之分
    局部变量：定义在函数内部的变量，只能在其被定义的函数内访问
    全局变量：定义在函数外部的变量，可以在整个程序范围内访问
    
变量的作用域：在一个python程序中可以直接访问某个变量的区域范围

函数的参数（形参）：局部变量，只能在该函数内部访问和使用
函数外部定义的变量：全局变量，可以在定义该变量之后的任何地方使用，包括函数内部

局部作用域：函数内部
全局作用域：函数外部
函数内部（局部作用域）可以直接访问函数外部（全局作用域）的全局变量，但若想在函数内部修改全局变量的值，需要使用关键字global进行声明
    global只能声明不能赋值





'''

'''局部变量和全局变量'''
# def myfun(a,b):
#     return a+b
#
# c=myfun(2,3)
# print(a,b,'之和等于',c)





'''形参：局部变量'''
# def myfun(a,b):
#     print('a+b等于',a+b)
#
# myfun(2,3)




'''练习1'''
# import random
# def lucky_ball():
#     flag=random.randint(1,9)
#     ball=[]
#     for i in range(1,51,1):
#         if i%flag == 0:
#             ball.append(i)
#     return flag,ball
# res=lucky_ball()
# # print(res)
# print('随机幸运球编号为',res[0],'的倍数：',res[1])





'''函数外定义变量'''
# c=3
# def myfun():
#     for i in range(c):
#         print(i)
#
# myfun()
# print('-'*20)
# print(c)





'''练习2'''
# import random
# flag=random.randint(1,9)
# ball=[]
# def lucky_ball():
#     for i in range(1,51,1):
#         if i % flag == 0:
#             ball.append(i)
#     return ball
#
# print('随机幸运球编号为',flag,'的倍数：',lucky_ball())





'''global'''
# c=1
# def myfun(a,b):
#     global c
#     c=a+b
#     return c
#
# print('调用前，c的值为：',c)
# myfun(2,3)
# print('调用后，c的值为：',c)





'''练习3'''
# import random
# flag=random.randint(1,9)
# ball=[]
# total=0
# def lucky_ball():
#     global total
#     for i in range(1,51,1):
#         if i % flag == 0:
#             total+=1
#             ball.append(i)
#     # return total,ball
#
# lucky_ball()
# print('幸运球个数为：',total,'\n随机幸运球编号为',flag,'的倍数：',ball)





'''----------------------------------------------------------------------------------------------------------------------------------'''






































































































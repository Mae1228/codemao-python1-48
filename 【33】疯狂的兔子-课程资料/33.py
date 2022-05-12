''''''
'''
迭代：反复，在循环中逐步得到最终结果的过程，即每次循环的结果都有上次循环结果得来

递归：重复递推再重复回归的意思，在程序中函数直接或间接调用函数本身
    把这一步的问题推给前一（几）布去解决
    本质：
        把大问题逐步分解成规模小的子问题
    到最小子问题后，递推就可以结束了
    重点:
        调用函数本身
        有函数出口
        
多元赋值：元组赋值，将多个变量同时赋值的方法
    表达时可以省略小括号：
        (x,y,z) = (1,2,3)
        x,y,z = 1,2,3
        x,y = y,x

练习题：
    C 
    B   C
    A   D

'''

'''练习1'''
# def mysum1(number):
#     s=0
#     i=1
#     while i<=number:
#         s+=i
#         i+=1
#     return s
#
# print(mysum1(5))





'''练习2'''
# def mysum2(number):
#     if number == 1:
#         return 1
#     else:
#         return number+mysum2(number-1)
#
# print(mysum2(5))





'''多元赋值'''
# t1=0
# t2=1
# t1,t2=t2,t1+1
# print(t1,t2)





'''项目'''
# def rabbit1(number):#迭代
#     m1=1    #上上月
#     m2=1    #上月
#     if number == 1 or number == 2:      #number为当月
#         return 1
#     else:
#         for i in range(3,number+1,1):
#             # res = m1 +m2
#             # m1 = m2
#             # m2 = res
#             m1,m2 = m2,m1+m2
#         return m2
#
# def rabbit2(number):
#     if number == 1 or number == 2:
#         return 1
#     else:
#         return rabbit2(number-1)+rabbit2(number-2)
#
# print(rabbit1(5))
# print(rabbit2(5))





'''--------------------------------------------------------------------------------------------------------------------------------'''






































































































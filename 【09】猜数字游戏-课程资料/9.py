''''''
'''





'''

''''''













































# 0 1 2 3 4
# 有条件的while循环
# a=0
# while a <= 4:
#     print(a)
#     a+=1
# else:
#     print(11111)


# 死循环
# a=0
# while True:
#     print(a)
#     if a==4:
#         break
#     a+=1
# else:
#     print(22222)



# 有条件的while循环
# a=0
# while a <= 4:
#     a += 1
#     if a==3:
#         continue
#     print(a)
# else:
#     print(33333)



# 死循环   双分支if else    随机库 random
# import random
# print('开始猜数字游戏吧！')
# m=random.randint(0,10)     #谜底
# print(m)
# while True:
#     a=int(input('请输入一个数：'))
#     if m == a:
#         print('恭喜！猜对了！')
#         break
#     else:
#         print('猜错了')





# 有条件的循环   双分支if else    随机库 random
import random
print('开始猜数字游戏吧！')
m=random.randint(0,10)     #谜底
print(m)
c=1     #次数
while c <= 3:
    a=int(input('请输入一个数：'))
    if m == a:
        print('恭喜！猜对了！')
        break
    else:
        print('猜错了')
    c+=1




# 有条件的循环   多分支if elif  else    随机库 random
import random
print('开始猜数字游戏吧！')
m=random.randint(0,10)     #谜底
print(m)
c=1     #次数
while c <= 3:
    a=int(input('第'+str(c)+'次：'))
    if m == a:
        print('恭喜！猜对了！')
        break
    elif a > m:
        print('猜大了')
    else:
        print('猜小了')
    c+=1
else:
    print('正确数字是'+str(m)+',没有机会了...')

'''猜数字小游戏-练习包'''

# #条件循环练习
# i = 0
# while i < 5:
#     print(i)
#     i += 1

#while循环的else结构练习
i = 0
while i < 10:
    if i == 5:
        print('循环中断')
        break
    print(i)
    i += 1
else:
    print('循环顺利结束')

# #猜数字小游戏
# #调用随机库
# import random
# number = random.randint(0, 10)
# i = 1
# print('开始猜数字小游戏吧！')
# while i <= 3:
#     #变量灵活使用
#     send = '第' + str(i) + '次：'
#     message = int(input(send))
#     if message == number:
#         print('恭喜！猜对了！')
#         break
#     else:
#         print('不对哦')
#     i += 1
# #while循环的else结构使用
# else:
#     print('正确数字是' + str(number) + ',没有机会了...')
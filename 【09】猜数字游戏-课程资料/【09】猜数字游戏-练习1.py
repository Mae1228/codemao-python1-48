import random
r=6
print('开始猜数字游戏吧！')
while True:
    a=int(input('请输入一个数：'))
    if a==r:
        print('恭喜！猜对了！')
        break
    else:
        print('猜错了')

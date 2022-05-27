''''''
import random
r=random.randint(0,10)
print('开始猜数字游戏吧！')
i=1
while i <=3:
    a=int(input('请输入一个数：'))
    if a==r:
        print('恭喜！猜对了！')
        break
    else:
        print('猜错了')
    i+=1
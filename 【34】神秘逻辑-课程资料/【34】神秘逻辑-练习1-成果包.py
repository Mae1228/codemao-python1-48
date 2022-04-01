'''神秘逻辑-练习一'''
#迭代方法求解
def jiecheng(n):
    result=1
    for item in range(1,n+1):
        result*=item
    return  result
print(jiecheng(5))





#递归求解5的阶乘
def myfac(n):
    if n == 1:
        return 1
    else:
        return n * myfac(n - 1)

num = int(input('请输入数字：'))
print(myfac(num))
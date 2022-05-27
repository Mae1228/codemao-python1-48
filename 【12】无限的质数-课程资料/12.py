''''''
'''
质数：质数是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数
    除了1和本身，不能被其他数整除

标志位：变量当标志位，数值没有意义，表示一种状态

for循环嵌套：
    语法表示：
        for 变量1 in 序列：
            外层循环体
            for 变量2 in 序列：
                内层循环体
    执行顺序：外层循环每执行一次，内层循环都完整执行一遍，然后再继续执行外层循环

for...else...：
    语法表示：
        for 变量 in 序列:
            循环体
        else:
            else子句
        其他语句
    执行顺序：
        for循环正常执行完成后，继续执行else子句
        break则不执行else子句
        continue则会执行else子句





'''

'''练习1'''
# num=int(input('请输入数字：'))
# b=0
# for i in range(2,num):
#     if num%i==0:
#         b=1
# if b==0:
#     print(num,'是质数')
# else:
#     print(num, '不是质数')






'''练习2'''
# num=int(input('请输入数字：'))
# for i in range(2,num):
#     if num%i==0:
#         print(num, '不是质数')
#         break
# else:
#     print(num,'是质数')






'''练习3'''
# num1=int(input('请输入起始数：'))
# num2=int(input('请输入终止数：'))
# for j in range(num1,num2+1):
#     b=0
#     for i in range(2,j):
#         if j%i==0:
#             b=1
#     if b==0:
#         print(j,'是质数')






'''练习4'''
# num1=int(input('请输入起始数：'))
# num2=int(input('请输入终止数：'))
# for j in range(num1,num2+1):
#     for i in range(2,j):
#         if j%i==0:
#             break
#     else:
#         print(j,'是质数')






'''-----------------------------------------------------------------------------------------------------------------------------------------------'''







































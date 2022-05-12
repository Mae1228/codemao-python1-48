''''''
'''
三角形边长关系：任意两边之和大于第三边
    a+b>c and a+c>b and b+c>a

三角形周长和面积：
    三角形周长：三条边的长度之和
        C=a+b+c
    三角形面积：海伦公式
        p=(a+b+c)/2
        S=(p*(p-a)*(p-b)*(p-c))**0.5
        
round(数值,保留位数)：计算浮点数的近似值
    保留位数：保留到小数点后n位精度值，若缺省则默认保留到整数
    
return语句返回多个值：return语句用于退出函数，并返回一个或一组值
    语句格式：
        return a,b,......
    return语句以元组的形式返回多个值
        
各类三角形边长特性：
    等边三角形：三条边相等
        a==b==c
    等腰三角形：任意两条边相等
        a==b or a==c or b==c
    直角三角形：两条直角边的平方和等于第三条边的平方
        a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2

练习题：
    C 
    D
    A   B   C   D

'''

'''练习1'''
# def s_chack(a,b,c):
#     if a+b>c and a+c>b and b+c>a:
#         return True
#     else:
#         return False




'''round()'''
# print(round(5.463,2))
# print(round(5.463,1))





'''return语句返回多个值'''
# def myfun(a,b):
#     c=a+b
#     return a,b,c
#
# print(myfun(2,5))




'''练习2'''
# def c_s(a,b,c):
#     C=a+b+c
#     p = (a + b + c) / 2
#     S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#     S=round(S,1)
#     return C,S




'''练习3'''
# def s_type(a,b,c):
#     if a==b==c:
#         return '等边三角形'
#     elif a==b or a==c or b==c:
#         return '等腰三角形'
#     elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
#         return '直角三角形'
#     else:
#         return '普通三角形'





'''项目'''
# def s_chack(a,b,c):
#     if a+b>c and a+c>b and b+c>a:
#         return True
#     else:
#         return False
#
# def c_s(a,b,c):
#     C=a+b+c
#     p = (a + b + c) / 2
#     S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#     S=round(S,1)
#     return C,S
#
# def s_type(a,b,c):
#     if a==b==c:
#         return '等边三角形'
#     elif a==b or a==c or b==c:
#         return '等腰三角形'
#     elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
#         return '直角三角形'
#     else:
#         return '普通三角形'
#
# def main(a,b,c):
#     if s_chack(a,b,c)==True:
#         C=c_s(a,b,c)[0]
#         S=c_s(a,b,c)[1]
#         T=s_type(a,b,c)
#         return C,S,T
#     else:
#         return '不是三角形'
#
# print(main(5,5,5))
# print(main(5,5,6))
# print(main(3,4,5))
# print(main(3,2,6))





'''---------------------------------------------------------------------------------------------------------------------------------------------'''









































































































































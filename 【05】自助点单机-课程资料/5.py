''''''
'''
数据类型：
    数字：
        整数int：纯数字
        浮点数float：小数
    字符串str：使用引号来创建
    列表list：
    元组tuple：
    集合set：
    字典dict：

算数运算：
    +：
    -：
    *：
    /：返回浮点类型

复合运算：本身的值进行运算后再赋值给本身
    +=
    -=
    *=
    /=
    复合运算本质实际上是一种缩写形式
    x+=1   等价于   x=x+1
    
type(数据)：查看数据类型

input：默认是字符串类型

数据类型的转换：
    int(数据)：将数据转换为整数
        纯数字的字符串才能转成整数
    float(数据)：将数据转换为浮点数
        数字和小数点的字符串才能转换成浮点数
    str(数据)：将数据转换为字符串

练习题：
    C 
    A   B   C
    A 

'''

'''练习1'''
# a='111'
# b=222
# c=222.0
# print(type(a))
# print(type(b))
# print(type(c))






'''练习2'''
# a=input('请输入数字1：')
# b=input('请输入数字2：')
# print(a+b)





'''项目'''
# meal1 = '汉堡,薯条,可乐'
# meal2 = '鸡肉卷,沙拉,柠檬茶'
# food10 = '汉堡,鸡肉卷,牛肉面,三明治'
# food6 = '薯条,沙拉,花生米,可乐,柠檬茶,紫菜汤'
# yn=input('是否选择套餐（y/n）')
# if yn=='y':
#     tc=input('请选择套餐：')
#     if tc=='1':
#         print(meal1,'共20元')
#     elif tc=='2':
#         print(meal2, '共20元')
#     else:
#         print('请输入正确的套餐')
# elif yn=='n':
#     money=0
#     cp1=input('请选择菜品1：')
#     cp2=input('请选择菜品2：')
#     cp3=input('请选择菜品3：')
#     if cp1 in food6:
#         money+=6
#     elif cp1 in food10:
#         money+=10
#     if cp2 in food6:
#         money+=6
#     elif cp2 in food10:
#         money+=10
#     if cp3 in food6:
#         money+=6
#     elif cp3 in food10:
#         money+=10
#     print(cp1,cp2,cp3,'共',money,'元')
# else:
#     print('输入错误')






'''-------------------------------------------------------------------------------------------------------------------------------'''











































'''自助点单机-练习包'''
"""
接收变量练习：
使用两次input()方法，接收键盘输入的两个数字，并分别打印出他们的数据类型(type()方法)。
"""
a = input("请输入一个数字：")
b = input("请再输入一个数字：")

print("第一个数字的数据类型是：",type(a))
print("第二个数字的数据类型是：", type(b))


"""
接收并运算练习：
在练习一的基础上，将接收到的两个数字，进行加法运算，打印出他们的和。
"""
#未转化数据类型前：
print(a+b)

#转换数据类型之后：
a=int(a)
b=int(b)
print(a+b)
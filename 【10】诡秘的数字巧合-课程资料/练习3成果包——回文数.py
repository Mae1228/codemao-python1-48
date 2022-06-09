'''练习3成果包——回文数'''
'''
编写程序帮助阿短来判定一个正整数是否为回文数。

输入一个三位以上的正整数，输出是否为回文数提示信息。
如：
Input：
输入数字：12121
Output：
12121 是回文数
'''

# #回文数判断方法一：
number = int(input('输入数字：'))
numberStr = str(number)
newStr = ''
i = len(numberStr) - 1
#使用循环，将numberStr倒序放入newStr中
while i >= 0:
    newStr += numberStr[i]
    i -= 1
if newStr == numberStr:
    print(number, '是回文数')
else:
    print(number, '不是回文数')


# #回文数判断方法二
# number = int(input('输入数字：'))
# numberStr = str(number)
# head = 0
# tail = len(numberStr) - 1
# #使用循环，比较相对应的头和尾数字是否相同
# while True:
#     if numberStr[head] != numberStr[tail]:
#         print(number, '不是回文数')
#         break
#     head += 1  # 头标志向后移
#     tail -= 1  # 尾标志向前移
#     if head >= tail:
#         print(number, '是回文数')
#         break

# 题目: 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同






# 思路1: 获取到各个位上的数字 然后按照回文数的概念进行比较
# num1 = int(input(">>>:"))
# ge_wei = num1 % 10
# shi_wei = num1 // 10 % 10
# qian_wei = num1 // 1000 % 10
# wan_wei = num1 // 10000
# if ge_wei == wan_wei and shi_wei == qian_wei:
#     print(f"{num1}是回文数")
# else:
#     print(f"{num1}不是回文数")
# # 思路2: 逆序后的数字与原来的数字比较
# num2 = input(">>>:")
# new_num2 = num2[::-1]
# if num2 == new_num2:
#     print(f"{num2}是回文数")
# else:
#     print(f"{num2}不是回文数")


# 思路3: 通过字符串的操作判断个位与万位相同，十位与千位相同
# num3 = input(">>>:")
# flag = True  # 用来判断是否为回文数
# for i in range(int(len(num3) / 2)):
#     if num3[i] != num3[-i - 1]:
#         flag = False
#         break
# if flag:
#     print(f"{num3}是回文数")
# else:
#     print(f"{num3}不是回文数")
#

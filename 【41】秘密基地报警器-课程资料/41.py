''''''
'''
异常：程序在执行中因出现错误或者发生非正常的情况而影响程序的正常执行
try...except...：
    当程序发生异常时我们需要进行捕获和处理，否则程序会终止执行
    语法表示：
        try:
            可能发生异常的代码
        except 异常类型名称:
            发生异常时执行的代码
        异常类型名称可缺省

常见的异常：
    Exception：所有内置的非系统退出类异常
    IOError：输入、输出操作失败
    ImportError：导入模块失败
    NameError：未声明、初始化对象
    SyntaxError：语法错误
    TypeError：类型不匹配
    ValueError：传入无效的参数值
    ZeroDivisionError：除数为零异常

多个异常的捕获和处理：
    一个try语句可以组合多个except语句，分别处理不同的异常
    一个except语句也可以同时处理多个异常，这些异常将被放在一个元组里
    若想在except子句中访问捕获到的具体异常信息，可在except语句后使用as
    语法表示：
        try:
            可能发生异常的代码
        except 异常类型名称 as 变量:
            发生异常时执行的代码
        except (异常类型名称1,异常类型名称2,...) as 变量:
            发生异常时执行的代码
        
try...except...else...：
    else语句时可选的，else子句将在try子句没有发生任何异常的时候执行
    语法表示：
        try:
            可能发生异常的代码
        except 异常类型名称:
            发生异常时执行的代码
        else:
            没有异常时执行的代码
        
try...except...else...finally...：
    finally语句可以直接与try语句组合，也可以跟在try...except...else...组合的后面，不管是否发生异常，finally子句都将执行
    语法表示：
        try:
            可能发生异常的代码
        except 异常类型名称:
            发生异常时执行的代码
        else:
            没有异常时执行的代码
        finally:
            不管有无异常都会执行的代码
        
练习题：
    C 
    C
    B 
    

'''

'''除数异常'''
# print(3/0)





'''try...except...'''
# try:
#     i=int(input('输入一个整数：'))
#     print(3/i)
# except ZeroDivisionError:
#     print('出现异常，除数不能为0！')





'''多个try...except...'''
# try:
#     i=int(input('输入一个整数：'))
#     print(3/i)
# except ZeroDivisionError as e:
#     print('除数异常：',e)
# except ValueError as e:
#     print('值异常：',e)
# try:
#     i=int(input('输入一个整数：'))
#     print(3/i)
# except (ZeroDivisionError,ValueError) as e:
#     print('出现异常：',e)





'''try...except...else...'''
# try:
#     i=int(input('输入一个整数：'))
#     print(3/i)
# except ZeroDivisionError:
#     print('出现异常，除数不能为0！')
# else:
#     print('未发生异常')






'''try...except...else...finally...'''
# try:
#     i=int(input('输入一个整数：'))
#     print(3/i)
# except ZeroDivisionError:
#     print('出现异常，除数不能为0！')
# else:
#     print('未发生异常')
# finally:
#     print('运算结束')






'''项目'''
# import random
# lst=[]
# for i in range(50):
#     lst.append(i)
# print(lst)
# li = []
# a = int(input('请输入抽检成员数量：'))
# def check_zero(a):
#     for i in range(a):
#         c=random.randint(0,len(lst)-1)
#         m=lst[c]
#         if m not in li:
#             li.append(m)
#             lst.remove(m)
#     try:
#         for i in li:
#             b=3/i
#     except ZeroDivisionError:
#         print('发现zero星密探闯入基地！')
#     else:
#         print('未发现可以人员，基地一切正常！')
#     finally:
#         print('抽检成员详情为：',li)
#
# check_zero(a)






'''练习题'''
# try:
#     n=float(input('hhh:'))
#     print(n*2)
# except TypeError:
#     print(11)
# except ValueError:
#     print(2222)
# except ZeroDivisionError:
#     print(33333)
# except SyntaxError:
#     print(4444)





'''-------------------------------------------------------------------------------------------------------------------------------------'''




















































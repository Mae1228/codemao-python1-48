''''''
'''
函数：
    一段命名了的代码，可以实现某一些功能，我们通过调用函数即可执行相应代码
内置函数：
    print()    input()     range()
自定义函数：
    以def开头定义函数
    自定义函数名：
        应避开python中的保留字，如：if、True、and等
        import keyword
        print(keyword.kwlist)
    函数中的代码块里面至少有一条语句
    语法格式：
        def 函数名():
            语句1
            语句2
            ......
        
        函数名()
位置参数：
    调用函数时，按照定义函数的参数数量和位置（顺序）传入的参数
    语法格式：
        def 函数名(参数a,参数b,......):
            语句1
            语句2
            ......
        
        函数名()
返回值：
    函数返回的值
    return语句用于退出函数并返回函数的返回值
    return语句可缺省，若缺省则函数返回None
    语法格式：
        def 函数名(参数a,参数b,......):
            语句1
            语句2
            ......
            return 变量/常量/表达式......
        
        变量=函数名()
默认参数：
    定义函数时，设定了默认值的一个或多个参数，它必须在位置参数后
    调用函数时，可以传递值给默认参数，也可以不传（保留默认值）；传默认参数也要按照它们的位置传递
    语法格式：
        def 函数名(参数a,参数b,......,参数m=0,参数n=1,......):
            语句1
            语句2
            ......
        
        函数名()    
练习题：
    B
    A 
    A   C   D

'''

'''调用函数'''
# print('hello world')
# msg=input()
# range(0,5)





'''关键字'''
# import keyword
# print(keyword.kwlist)




'''练习1'''
# def f():
#     print('执行我的第一个函数')
#
# f()





'''位置参数的函数'''
# def myfun(a,b,c):
#     print(c,b,a)
#
# myfun(1,2,3)





'''练习2'''
# def f(a,b):
#     print(a+b)
#
# f(10,30)




'''练习3'''
# def myadd(a,b):
#     return a+b
# res=myadd(100,20)
# print(res)
#
# def myadd(a,b):
#     c=a+b
# res=myadd(100,20)
# print(res)





'''默认参数的函数'''
# def myfun(a,b=2,c=3):
#     print(a,b,c)
#
# myfun(1,0)
# myfun(4,5,6)
# myfun(7)





'''项目'''
# def myrange(start,end,step=1):
#     li=[]
#     while start<end:
#         li.append(start)
#         start+=step
#     return li
#
# for i in myrange(0,16):
#     print(i)
# for i in myrange(2,17,2):
#     print(i)




'''--------------------------------------------------------------------------------------------------------------'''













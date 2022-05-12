''''''
'''
max(数字1,数字2,......)：求最大值的函数
max(列表/元组/字符串/字典/集合/......)
    
min(数字1,数字2,......)：求最小值的函数
min(列表/元组/字符串/字典/集合/......)

sorted(数字1,数字2,......)：排序函数
sorted(列表/元组/字符串/字典/集合/......,reverse=True)
    reverse是关键值参数，reverse参数默认值为False，即升序

round(浮点数/除法表达式/......)：近似值函数
round(浮点数/除法表达式/......,保留位数)
    round()函数中保留位数是默认参数，默认值为None，即返回最接近传入数值的整数

形参：形式参数，定义函数时设置的参数
实参：实际参数，调用函数时传入的参数
参数：形参和实参
    
'''

'''练习1'''
# t=(1,-4,-5,64,78,12,0,3,3.5,3)
# def mymax(li):
#     m=li[0]
#     for i in li:
#         if i>m:
#             m=i
#     return m
#
# print('最大值是：',mymax(t))





'''max()'''
# lst=[2,4,1]
# x=max(lst)
# print(x)
# y=max(3,5,1)
# print(y)





'''练习2'''
# t=(1,-4,-5,64,78,12,0,3,3.5,3)
# def mymin(li):
#     m=li[0]
#     for i in li:
#         if i<m:
#             m=i
#     return m
#
# print('最小值是：',mymin(t))




'''min()'''
# lst=[2,4,1]
# x=min(lst)
# print(x)
# y=min(3,5,0)
# print(y)





'''练习3'''
# t=(1,-4,-5,64,78,12,0,3,3.5,3)
# def mymax(li):
#     m=li[0]
#     for i in li:
#         if i>m:
#             m=i
#     return m
#
# def mymin(li):
#     m=li[0]
#     for i in li:
#         if i<m:
#             m=i
#     return m
#
# def mysorted(li,reverse=False):
#     li=list(li)
#     lst=[]
#     if reverse==False:#升序
#         while len(li) != 0:
#             m=mymin(li)
#             lst.append(m)
#             li.remove(m)
#     else:
#         while len(li) != 0:
#             m=mymax(li)
#             lst.append(m)
#             li.remove(m)
#     return lst
#
# print('升序排列：',mysorted(t))
# print('降序排列：',mysorted(t,True))





'''sorted()'''
# lst=[2,4,1]
# x=sorted(lst,reverse=True)
# print(x)
# y=sorted(lst)
# print(y)





'''练习4'''
# def myround(a,b=0):
#     x=int(a*10**(b+1))
#     f=x%10
#     if f>4:
#         x+=1
#     x1=x//10
#     m=x1/(10**b)
#     return m
#
# a1=float(input('请输入要取近似值的浮点数：'))
# a2=int(input('请输入要保留小数点后的位数：'))
# print(a1,'取近似值后的结果是：',myround(a1,a2))





'''round()'''
# num=3.14159
# x=round(num,3)
# print(x)
# y=round(num)
# print(y)




'''参数'''
# def myfun(x):   #形参
#     return x+1
#
# myfun(3)   #实参





'''--------------------------------------------------------------------------------------------------------------------------------------------------------------'''















































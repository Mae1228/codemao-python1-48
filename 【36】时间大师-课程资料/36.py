''''''
'''
time.sleep(秒数)：定时等待

time.perf_counter()：
    一般用于测量程序的运行时长，返回浮点类型的秒数
    该函数未设定实践的参考点（起始时间），需连续调用并做差
    
2.02e-05表示2.02*0.00001

时间元组：python包含9组时间值的元组
    0：年，如2022
    1：月，如1-12
    2：日，如1-31
    3：时，如0-23
    4：分，如0-59
    5：秒，如0-61（含闰秒）
    6：一周的第几天，如0-6（0是周一）
    7：一年的第几天，如0-366
    8：夏令时，如0（否）、1（是）或-1（未知）

time.mktime(时间元组)：
    接收时间元组作为参数，返回当地时间的浮点秒数（时间戳）
    时间元组应该为1970年1月1日8点之后的时间

time.localtime(时间戳)：
    接收时间戳（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组
    时间戳：浮点秒数，缺省时默认为又time()返回的当前时间
    
os.system('cls')：
    清除控制台在本命令之前输出的内容
    语法格式：
        import os
        os.system('cls')
    



'''

'''perf_counter()'''
# import time
# t0=time.perf_counter()
# for i in range(10):
#     print(i,end=' ')
# t1=time.perf_counter()
# print('\n',t1-t0)






'''练习1'''
# import time
# def rabbit1(number):
#     m1=1
#     m2=1
#     if number == 1 or number == 2:
#         return 1
#     else:
#         for i in range(3,number+1,1):
#             m1,m2=m2,m1+m2
#         return m2
#
# def rabbit2(number):
#     if number == 1 or number == 2:
#         return 1
#     else:
#         return rabbit2(number-1)+rabbit2(number-2)
#
# t1=time.perf_counter()
# print(rabbit1(20))
# t2=time.perf_counter()
# print('迭代法运行时长为：',t2-t1)
# t3=time.perf_counter()
# print(rabbit2(20))
# t4=time.perf_counter()
# print('迭代法运行时长为：',t4-t3)





'''mktime()'''
# import time
# t=(2020,3,12,0,0,0,0,0,0)
# str_time=time.mktime(t)
# print(str_time)





'''localtime()'''
# import time
# struct_time=time.localtime(1500000000)
# print(struct_time)
# s_t=time.localtime()
# print(s_t)





'''练习2'''
# import time
# dic = {
#     0: '星期一',
#     1: '星期二',
#     2: '星期三',
#     3: '星期四',
#     4: '星期五',
#     5: '星期六',
#     6: '星期日',
# }
# a=input('输入日期（例 2020-3-12）:').split('-')
# # print(a)
# y,m,d=map(int,a)
# t=(y,m,d,0,0,0,0,0,0)
# f=time.mktime(t)
# # print(f)
# l=time.localtime(f)
# # print(l)
# w=dic[l[6]]
# day=l[7]
# # print(w,day)
# print('当天是',w,',是当年的第',day,'天')






'''os.system('cls')'''
# import os
# print('hhhh')
# os.system('cls')
# # print('\033c', end='')





'''练习3'''
# import time
# import os
# def t(a,b,c):
#     return str(a)+':'+str(b)+':'+str(c)
#
# def main():
#     while True:
#         os.system('cls')
#         tup=time.localtime()
#         h=tup[3]
#         m=tup[4]
#         s=tup[5]
#         print(t(h,m,s))
#         time.sleep(1)
#
# main()





'''--------------------------------------------------------------------------------------------------------------------------------------------------'''














































































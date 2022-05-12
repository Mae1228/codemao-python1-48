''''''
'''
Python 使用对象模型来存储数据，构造的任何类型的值都是一个对象（比如我们创建的整数：26，字符串：“hello world”，列表：[1, 2, 3] 等都是对象）。
对象可以理解为保存在内存中的一段具有固定格式的数据，所有的 Python 对象都拥有三个特性：身份（ID），类型 和 值。
    （1）标识用于返回唯一地标识一个对象，通常对应对象在计算机内存中的位置。使用内置函数id(obj1)可以返回对象obj1的标识。
    （2）类型用于表示对象所属的数据类型（类）。使用内置函数type(obj1)可以返回对象obj1所属的数据类型。
    （3）值：对象代表的数据
time:
    time.perf_counter()
    time.mktime((2022,4,1,12,0,0,0,0,0))
    time.localtime(150000000)
datetime包是基于time包的一个高级包， 为我们提供了多一层的便利。
datetime可以理解为date和time两个组成部分。
    date是指年月日构成的日期(相当于日历)，
    time是指时分秒微秒构成的一天24小时中的具体时间(相当于手表)。
date.today()：返回当前的日期对象
date(2222,4,1)：返回该天的日期对象            
res.days：截取日期差对象的天数
date.isoweekday(日期对象)：以整数形式返回某日期是星期几，星期一为1，星期日为7
calendar.month(2022,4)：传入某年某月，返回该月的日历多行字符串
calendar.calendar(2022)：传入某年，返回该年的日历多行字符串


'''
'''date.today()'''
# from datetime import date
# a=date.today()
# print(a)
# # print(type(a))




'''date(2020,6,28)'''
# from datetime import date
# b=date(2022,4,15)
# print(b)
# # print(type(b))




'''日期差对象'''
# from datetime import date
# a=date.today()
# b=date(2022,5,25)
# res1=b-a
# # print(res1)
# print('日期相差：')
# print(res1.days)




'''date.isoweekday(日期对象)'''
# from datetime import date
# a=date.today()
# week1=date.isoweekday(a)
# # print(week1)
# # print(type(week1))
# b=date(2022,5,4)
# week2=date.isoweekday(b)
# # print(week2)
# print('今天星期：'+str(week1))





'''假期倒计时'''
# from datetime import date
# a=date.today()
# print(a)
# w=date.isoweekday(a)
# print(w)
# b=date(2022,6,8)
# c=date(2022,7,15)
# print('今天是：%s 星期：%d'%(a,w))
# print('距离考试还有：%d天'%(b-a).days)
# print('距离暑假还有：%d天'%(c-a).days)




'''calendar.month(2022,4)'''
# import calendar
# print(calendar.month(2022,4))



'''calendar.calendar(2022)'''
# import calendar
# print(calendar.calendar(2022))




'''练习2'''
# import calendar
# y=int(input('请输入开始月份：'))
# m1=int(input('请输入开始月份：'))
# m2=int(input('请输入结束月份：'))
# if m1==m2:
#     print(calendar.month(y,m1))
# else:
#     for i in range(m1,m2+1):
#         print(calendar.month(y,i))
#         print('*'*20)




'''练习3'''
# from datetime import date
# partyDate = {
#     '编程猫':  date(2020, 3, 9),
#     '渝小帅':  date(2020, 4, 8),
#     '温温':    date(2020, 5, 15),
#     '欧阳涂涂':date(2020, 5, 21),
#     '叶清秋':  date(2020, 6, 14),
#     '高欢':    date(2020, 8, 8),
#     '边磊':    date(2020, 9, 11),
#     '丛子柒':  date(2020, 9, 20),
# }
# dList=[]
# for k,v in partyDate.items():
#     week=date.isoweekday(v)
#     print(week)
#     if week==3 or week==7:
#         dList.append(k+str(v))
# print(dList)
# print('可以去参加的生日party有：'+' '.join(dList))



'''---------------------------------------------------------------------------'''
























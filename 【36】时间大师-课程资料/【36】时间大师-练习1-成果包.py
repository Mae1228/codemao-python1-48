import time
print(time.time())
print(time.ctime())
print(time.gmtime())
# timeStr='2018-01-26 12:55:20'
# print(time.strptime(timeStr,"%Y-%m-%d %H:%M:%S"))
# 迭代法
def rabbit1(number):
    m1 = 1
    m2 = 1
    if number == 1 or number == 2:
        return 1
    else:
        for x in range(3, number + 1):
            m1, m2 = m2, m1 + m2
        return m2

# 递归法
def rabbit2(number):
    if number == 1 or number == 2:
        return 1
    else:
        return rabbit2(number - 1) + rabbit2(number - 2)

t0 = time.perf_counter()
print(rabbit1(30))
t1 = time.perf_counter()
print('迭代法运行时长为：',t1-t0)

t2 = time.perf_counter()
print(rabbit2(30))
t3 = time.perf_counter()
print('递归法运行时长为：',t3-t2)






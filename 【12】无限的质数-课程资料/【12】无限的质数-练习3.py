'''无限的质数-阶段3'''

#用for循环判断是否为质数
number = int(input('请输入数字:'))
for j in range(2, number):
    if number % j == 0:
        print(number, '不是质数')
        break
else:
    print(number, '是质数')


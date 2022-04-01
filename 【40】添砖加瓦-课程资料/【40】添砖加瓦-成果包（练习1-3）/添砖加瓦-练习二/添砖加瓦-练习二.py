'''添砖加瓦-练习二'''

#导入mymax模块中的所有函数
from compare.mymax import *

#直接调用mymax()函数,完成top3()函数
def top3(lst):
    res = []
    for i in range(3):
        temp = mymax(lst)
        res.append(temp)
        lst.remove(temp)
    return res


def get_lst():
    ipt = input('请输入列表，各个值之间用空格隔开：')
    res = list(map(int,ipt.split(' ')))
    return res


temp = get_lst()
print('原列表：',temp)
print('前三名：',top3(temp))

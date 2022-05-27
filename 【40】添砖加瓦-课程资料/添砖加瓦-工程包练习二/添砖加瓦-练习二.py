'''添砖加瓦-练习一'''

#导入mymax模块
from compare.mymax import mymax
#调用mymax模块中的mymax()函数,完成top3()函数
def get_lst(s):
    # s_lst=s.split(' ')
    # n_lst=[]
    # for i in s_lst:
    #     n_lst.append(int(i))
    n_lst=list(map(int,s.split(' ')))
    return n_lst

def top3(li):
    t_list=[]
    for i in range(3):
        m=mymax(li)
        t_list.append(m)
        li.remove(m)
    return t_list

a=input('请输入列表，各个值之间用空格隔开：')
res=get_lst(a)
print('原列表：',res)
print('前三名：',top3(res))
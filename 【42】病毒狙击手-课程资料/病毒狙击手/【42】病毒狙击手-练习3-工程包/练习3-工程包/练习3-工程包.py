'''
练习3-工程包
t: 包含病毒的文件内容
b: 病毒名称
bd: 病毒种类列表
sniped: 从文件bd_butler.txt中消灭掉的病毒名称及数量信息,存储格式为(b,num)
'''

def snipe_bd(t, b):
    num = t.count(b)
    if num > 0:
        t = t.replace(b, '')  # 把butler.txt文件内容中的病毒名称删除掉
    else:
        raise ValueError('num值为0')  # 如果统计某种病毒数量为0，即sum==0，抛出ValueError异常
    return num, t

bd = ['SARS', 'MERS', 'COVID-19']
sniped = []

'''
练习2-工程包
t: 包含病毒的文件内容
b: 病毒名称
'''

def snipe_bd(t, b):
    num = t.count(b)
    if num > 0:
        t = t.replace(b, '')  # 把butler.txt文件内容中的病毒名称删除掉
    return num, t


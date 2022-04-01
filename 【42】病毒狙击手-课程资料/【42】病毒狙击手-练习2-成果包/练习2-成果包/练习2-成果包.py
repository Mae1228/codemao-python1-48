'''练习2-成果包'''

def snipe_bd(t, b):
    num = t.count(b)
    if num > 0:
        t = t.replace(b, '')
    return num, t

try:
    f = open('bd_butler.txt', 'r')
except IOError:
    print('没有找到文件!')
else:
    print('病毒狙击开始！')
    t = f.read()
    f.close()
    snipe = snipe_bd(t, 'SARS')
    num = snipe[0]
    print('病毒狙击结束，狙击详情为：', ('SARS', num))



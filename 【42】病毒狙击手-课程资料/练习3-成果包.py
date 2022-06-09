'''练习3-成果包'''

def snipe_bd(t,b):
    num = t.count(b)
    if num > 0:
        t = t.replace(b, '') 
    else:
        raise ValueError('num值为0') 
    return num,t

bd = ['SARS', 'MERS', 'COVID-19']
sniped = []
try:
    f = open('bd_butler.txt', 'r')
except IOError:
    print('没有找到文件!')
else:
    print('病毒狙击开始！')
    t = f.read()
    f.close()
    for b in bd:
        try:
            snipe = snipe_bd(t, b)
            num = snipe[0]
            sniped.append((b,num))
        except ValueError:
            print('未发现病毒：',b)
    print('病毒狙击完成,狙击详情为：', sniped)



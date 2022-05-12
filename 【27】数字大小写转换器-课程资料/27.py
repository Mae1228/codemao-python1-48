''''''
'''

'''




'''项目'''
dic={
    '0':'零',
    '1':'壹',
    '2':'貮',
    '3':'叁',
    '4':'肆',
    '5':'伍',
    '6':'陆',
    '7':'柒',
    '8':'捌',
    '9':'玖'
}
dic2={
    0:'元',
    1:'拾',
    2:'佰',
    3:'仟',
    4:'万',
    5:'拾万',
    6:'佰万',
    7:'仟万',
    8:'亿',
    9:'拾亿',
    10:'佰亿',
    11:'仟亿'
}
a=int(input('输入数字:'))
a_str=str(a)
a_list=list(a_str)
print(a_list)
dic_list=[]
for i in a_list:
    dic_list.append(dic[i])
print(dic_list)
dic2_list=[]
for i in range(len(a_list)):
    dic2_list.append(dic2[i])
print(dic2_list)
dic2_list.reverse()
print(dic2_list)
d_list=[]
for i in range(len(a_list)):
    d_list.append(dic_list[i])
    d_list.append(dic2_list[i])
print(d_list)
d_str=''.join(d_list)
print(d_str)




'''-------------------------------------------------------------------------------------------------------------'''
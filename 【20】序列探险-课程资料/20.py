''''''
'''
list(字符串)：可以将字符串转换为列表
字符串.join(列表)：将列表中的元素以指定的字符连接生成一个新的字符串
                列表中的元素必须是字符串类型，非空列表
列表.reverse()：方向排序列表中的元素

集合：用于存储多个数据，但是数据不可重复并且无序
    创建：
        非空集合：{}
                set()
        空集合：set()
    特点：数据不可重复，可以实现字符串、列表等序列的去重
成员运算符：
    in 
    not in        

'''

'''list()'''
# s='hello codemao !'
# li=list(s)
# print(li)





'''练习1'''
# a = '朝千两轻辞里岸舟白江猿已帝陵声过彩一蹄万云日不重间还住山，。，。'
# s=''
# # print(a[0:len(a):4])
# for i in range(0,4,1):
#     s += a[i:len(a):4]
# # print(s)
# print(list(s))




'''join()'''
# mylist=['1','2','3','4','5']
# s='#'.join(mylist)
# print(s)





'''reverse()'''
# mylist=[1,'hello','3','codemao']
# mylist.reverse()
# print(mylist)




'''练习2'''
# mylist = ['。', '山', '重', '万', '过', '已', '舟', '轻', '，', '住', '不', '啼', '声', '猿', '岸', '两',
#     '\n', '。', '还', '日', '一', '陵', '江', '里', '千', '，', '间', '云', '彩', '帝', '白', '辞', '朝']
# mylist.reverse()
# # print(mylist)
# s=''.join(mylist)
# print(s)





'''集合'''
# set1={1,'hello',3}
# set2=set('abcdefg')
# set3=set()
# set4={}
# print(type(set4))





'''集合去重'''
# mylist=['a','a','b','c','d','c']
# se=set(mylist)
# print(mylist,se,sep='\n')




'''练习3'''
# mylist = ['阿短', '绿豆', 'codemao', '小可', '美美', '佩奇', '乔治',
#           '小可', '大熊', '美美', '希希', '乔治', '阿瑶', '雪儿', '婷婷']
# # 遍历列表去重
# li=[]
# for i in mylist:
#     if i not in li:
#         li.append(i)
# print(li)
# # 集合去重
# se=set(mylist)
# se=list(se)
# print(se)




'''------------------------------------------------------------------------------------------------------------------------------------'''
























































































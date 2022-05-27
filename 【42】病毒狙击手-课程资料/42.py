''''''
'''
OIError一般发生在对文件进行操作时：
    打开一个不存在的文件
    读取模式下向文件写入内容
    访问文件但不满足该文件的设置权限

raise语句：
    抛出一个指定的异常
    语法表示：
        raise 异常名称(异常描述信息)
    为了能够捕获raise抛出的异常，except语句后需要使用与raise语句后相同的异常名称
        
str.isdigit()：用于检测字符串是否只由数字组成，返回值为True或False    








'''

'''练习1'''
# filelist=['file.txt','fille.txt']
# for i in filelist:
#     try:
#         f=open(i,'r')
#     except IOError:
#         print('没有找到文件！')
#     else:
#         t = f.read()
#         f.close()
#         print(t)






'''练习2'''
# def snipe_bd(t,b):
#     num=t.count(b)
#     if num>0:
#         t=t.replace(b,'')
#     return num,t
#
# try:
#     f=open('bd_butler.txt','r')
# except IOError:
#     print('没有找到文件！')
# else:
#     print('病毒狙击开始！')
#     s=f.read()
#     a,b=snipe_bd(s,'SARS')
#     print("病毒狙击结束，狙击详情为：('SARS',%d)"%a)






'''raise语句'''
# try:
#     a=input('输入一个数字：')
#     if not a.isdigit():
#         raise ValueError('a必须是数字')
# except ValueError as e:
#     print('引发异常：',e)





'''练习3'''
# def snipe_bd(t,b):
#     num=t.count(b)
#     if num>0:
#         t=t.replace(b,'')
#     else:
#         raise ValueError('num值为0')
#     return num,t
#
# bd=['SARS','MERS','COVID-19']
# n_bd=[]
# try:
#     f=open('bd_butler.txt','r')
# except ValueError:
#     print('没有找到文件！')
# else:
#     print('病毒狙击开始！')
#     s = f.read()
#     f.close()
#     for i in bd:
#         try:
#             a,b=snipe_bd(s,i)
#             n_bd.append((i,a))
#         except ValueError:
#             print('未发现病毒：',i)
#     print('病毒狙击完成，狙击详情为：',n_bd)






'''-------------------------------------------------------------------------------------------------------------------------------------'''
















































































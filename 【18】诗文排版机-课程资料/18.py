''''''
'''
str.split(分隔符,分割次数)：将一个字符串按照指定的分隔符分成多个字串
    分隔符：可以包含多个字符
    分割次数：子串的个数最多是（分割次数+1），若不指定，则分割次数没有限制
\n：换行符，其中\是转义字符
f.read()：一次性读取全部内容
f.readline()：读取一整行，包括'\n'字符
f.write(字符串)：将字符串写入文件
f.readlines()：读取所有行，并返回每行内容组成的序列
f.writelines(字符序列)：将字符序列写入文件



'''
'''str.split()'''
# s='我 爱 北京 天安门'
# for i in s.split(' '):
#     print(i)
#
#
# for i in s.split(' ',2):
#     print(i)




'''\n'''
# a='我爱学编程'
# b='我爱学\n编程'
# print(a)
# print(b)




'''练习一'''
# with open('静夜思.txt','r') as f:
#     t=f.read()
# print(t)
# with open('静夜思1.txt','w') as f2:
#     for i in t.split(' '):
#         f2.write(i+'\n')





'''练习二'''
# with open('静夜思1.txt','r') as f:
#     t1=f.readline()
#     t2=f.readline()
#     t=f.read()
# print(t1)
# print(t2)
# print(t)
# with open('静夜思2.txt','w') as f2:
#     f2.writelines('  '+t1)
#     f2.writelines('唐朝 '+t2)
#     f2.writelines(t)





'''练习三'''
# with open('绝句.txt','r') as f:
#     t=f.readlines()
# print(t)
# with open('绝句1.txt','w') as f2:
#     for i in t:
#         if i!='\n':
#             f2.write(i)






'''-------------------------------------------------------------------------------------------------------------------'''









































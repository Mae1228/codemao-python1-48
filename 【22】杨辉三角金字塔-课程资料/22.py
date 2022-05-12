''''''
'''
\t：制表符，对齐表格数据的各列
    字符串类型
str.center(字符串宽度,填充字符)：返回一个居中的原字符串，默认填充字符为空格

'''

'''练习1'''
# list4=[1,3,3,1]
# list5=[]
# for j in range(0,len(list4),1):
#     if j == 0:
#         list5.append(1)
#     else:
#         res=list4[j]+list4[j-1]
#         list5.append(res)
# list5.append(1)
# print(list5)





'''练习2'''
# l=[]
# for i in range(0,9,1):
#     if i == 0:
#         l.append([1])
#     elif i == 1:
#         l.append([1,1])
#     else:
#         li=[]
#         for j in range(0,len(l[i-1]),1):
#             if j == 0:
#                 li.append(1)
#             else:
#                 res=l[i-1][j]+l[i-1][j-1]
#                 li.append(res)
#         li.append(1)
#         l.append(li)
# # print(l)
# for x in l:
#     print(x)




'''\t'''
# print('张三\t李四\t王五')
# print('158cm\t175cm\t187cm')




'''练习3'''
# l=[]
# for i in range(0,9,1):
#     if i == 0:
#         l.append([1])
#     elif i == 1:
#         l.append([1,1])
#     else:
#         li=[]
#         for j in range(0,len(l[i-1]),1):
#             if j == 0:
#                 li.append(1)
#             else:
#                 res=l[i-1][j]+l[i-1][j-1]
#                 li.append(res)
#         li.append(1)
#         l.append(li)
# # print(l)
# for x in l:
#     s=''
#     for y in x:
#         s+=str(y)+'\t'
#     print(s)





'''center()'''
# test='abcdefghijklmnopqrstuvwxyz'
# print(test.center(60))
# print(test.center(60,'*'))
# print(test.center(31,'-'))





'''练习4'''
# l=[]
# for i in range(0,9,1):
#     if i == 0:
#         l.append([1])
#     elif i == 1:
#         l.append([1,1])
#     else:
#         li=[]
#         for j in range(0,len(l[i-1]),1):
#             if j == 0:
#                 li.append(1)
#             else:
#                 res=l[i-1][j]+l[i-1][j-1]
#                 li.append(res)
#         li.append(1)
#         l.append(li)
# # print(l)
# for x in l:
#     s=''
#     for y in x:
#         s+=str(y)+'   '
#     print(s.center(60))





'''-------------------------------------------------------------------------------------------------'''















































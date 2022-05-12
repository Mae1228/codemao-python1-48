''''''
'''
列表嵌套：
    每一个内层列表代表一条横向的道路，内层列表中每个元素道标一个路口
    元素的索引代表路口的坐标，元素的数值代表从（0，0）点到该点的路线方案数

map()函数：
    根据参数中提供的函数对指定序列做映射
    序列中每个元素都会调用参数中提供的函数
    语法格式：
        map(函数名,序列)
        函数名：不带括号及其参数

str.split(分割符,分割次数)：
    把指定字符串分成多个子字符串，并以列表进行返回
    分隔符：不写默认是空格
    分割次数：不写默认是全部分割

练习题：
    B
    C 
    
'''

'''map()'''
# a=map(int,['1','2','3'])
# for i in a:
#     print(i)
#
# a1,a2,a3=map(int,['1','2','3'])
# print(a1,a2,a3)





'''项目'''
# a=input('请输入学校坐标（例：9 9）：').split()
# print(a)
# n,m=map(int,a)
# print(n,m)
# lst=[]
# for i in range(n+1):
#     l=[]
#     for j in range(m+1):
#         l.append(0)
#     lst.append(l)
# print(lst)
# k=int(input('请输入施工路口数（例：1）：'))
# for i in range(k):
#     b=input('请输入施工路口坐标，注意0<x<n且0<y<m（例：4 4）：').split()
#     x,y=map(int,b)
#     lst[x][y]=-1        #标志位：表示封路点
#     lst[x-1][y]=-1
#     lst[x+1][y]=-1
#     lst[x][y-1]=-1
#     lst[x][y+1]=-1
# print(lst)
# for i in range(n+1):
#     for j in range(m+1):
#         if i == 0 and j == 0:
#             lst[i][j] = 1
#         elif i != 0 and j == 0:  #横坐标轴上
#             if lst[i][j] == -1:
#                 lst[i][j] = 0
#             else:   #左侧方案数
#                 lst[i][j] = lst[i-1][j]
#         elif i == 0 and j != 0:     #纵坐标轴上
#             if lst[i][j] == -1:
#                 lst[i][j] = 0
#             else:   #上侧的方案数
#                 lst[i][j] = lst[i][j-1]
#         else:
#             if lst[i][j] == -1:
#                 lst[i][j] = 0
#             else:   #左侧方案数+上侧的方案数
#                 lst[i][j] = lst[i-1][j]+lst[i][j - 1]
# print(lst)
# print(lst[n][m])





'''--------------------------------------------------------------------------------------------------------------------------------'''


















































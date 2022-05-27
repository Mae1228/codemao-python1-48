''''''
'''
列表：
    用于按照一定顺序存储多个或者一组数据
    列表中的元素可以是不同的数据类型
    空列表内没有任何内容
    列表要素：方括号[]、逗号,
    列表是一种序列，可以使用for循环进行遍历
索引：访问单个元素
    是序列中元素的位置编号，也叫下标
    语法表示：变量[索引]    
切片：访问多个元素
    用于截取序列中指定区间的元素值
    语法表示：变量[起始索引:结束索引:步长]
            起始变量：取值时包含该索引，如果缺省代表从0开始
            结束索引：取值时不包含该索引，如果缺省代表从序列末尾结束
            步长：每个步长个数据项中取出一个数据值，如果缺省代表步长是1
list.append(数据元素)：用于在列表末尾添加新的数据
list.remove(数据元素)：用于移除列表中某个值的第一个匹配项
                    移除的元素不存在则会报错            
成员运算符：
    in：存在
    not in：不存在
练习题：
    C 
    C   D 
    错误    


'''
'''练习一'''
# mylist=['c','o','d','e','m','a','o']
# for i in mylist:
#     print(i)




'''练习二'''
# s='hello codemao'
# print(s[8])
# print(s[6:10:1])
# print(s[0:13:2])




'''练习三'''
# s='hello codemao !'
# mylist=[]
# for i in s:
#     if i != ' ':
#         mylist.append(i)
# mylist.remove('!')
# print(mylist)




'''项目'''
# book_list = ['哈利波特', '流浪地球', '封神演义', '三国演义', '红楼梦', '西游记', '水浒传']
# while True:
#     print('end:结束管理图书 0：展示书单 1：借书 2：还书')
#     do=input('你好！要图书助手帮你做什么:')
#     if do=='0':
#         print('目前有图书:')
#         for i in book_list:
#             if '#' not in i:
#                 print(i)
#     elif do=='1':
#         j_book=input('要借哪本书:')
#         if j_book in book_list:
#             j_person=input('请登记借书人姓名:')
#             book_list.append(j_book+'#'+j_person)
#             book_list.remove(j_book)
#             print('借书成功！')
#         else:
#             print('没有此书或此书已被借走！')
#     elif do=='2':
#         h_book=input('要还哪本书:')
#         h_person=input('请核对借书人:')
#         if h_book+'#'+h_person in book_list:
#             book_list.append(h_book)
#             book_list.remove(h_book+'#'+h_person)
#             print('还书成功！')
#         else:
#             print('请检查书名或借书人信息是否正确！')
#     elif do=='end':
#         break





'''--------------------------------------------------------------------------------------------------------'''































































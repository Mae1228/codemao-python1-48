''''''
'''
水仙花数：一个三位数，各位数字的立方和等于其本身

len(数据)：返回字符、列表等长度或个数

字符串索引：[]
    正向索引（正向递增）：0  1  2  ...  长度-1
    反向索引（反向递减）：-长度 ...  -3  -2  -1
    
**：幂运算
    2**4 = 2*2*2*2  

while循环嵌套：
    将内循环看作一条单独语句，其执行结束后，外循环才可继续执行
    内循环执行结束则外循环才执行一次
    
回文数：正读反读都能读通的句子

    
    

'''

'''len()'''
# str='123567'
# print(len(str))






'''字符串索引'''
# str='12我3学4F'
# print(str[3])
# print(str[-4])






'''**'''
# a=2
# b=a**3
# c=a*a*a
# print(b)
# print(c)






'''练习1'''
# a=int(input('输入数字：'))
# astr=str(a)
# s=0     #和
# i=0     #索引
# while i<len(astr):
#     s+=int(astr[i])**3
#     i+=1
# if a==s:
#     print(a,'是水仙花数')
# else:
#     print(a, '不是水仙花数')






'''练习2'''
# a1=int(input('输入起始数：'))
# a2=int(input('输入终止数：'))
# while a1<=a2:
#     astr=str(a1)
#     s=0     #和
#     i=0     #索引
#     while i<len(astr):
#         s+=int(astr[i])**3
#         i+=1
#     if a1==s:
#         print(a1,'是水仙花数')
#     a1+=1






'''练习3：左右居中'''
# a=int(input('输入数字：'))
# astr=str(a)
# t=0
# w=len(astr)-1
# while True:
#     if t>=w:
#         print(a, '是回文数')
#         break
#     if astr[t] != astr[w]:
#         print(a,'不是回文数')
#         break
#     t+=1
#     w-=1






'''练习4：左右居中while...else...'''
# a=int(input('输入数字：'))
# astr=str(a)
# t=0
# w=len(astr)-1
# while t<w:
#     if astr[t] != astr[w]:
#         print(a,'不是回文数')
#         break
#     t+=1
#     w-=1
# else:
#     print(a, '是回文数')







'''练习5：正读反读'''
# a=int(input('输入数字：'))
# astr=str(a)
# s=''    #记录反向字符串
# i=len(astr)-1
# while i>=0:
#     s+=astr[i]
#     i-=1
# # print(s)
# if s==astr:
#     print(a,'是回文数')
# else:
#     print(a, '不是回文数')






'''-------------------------------------------------------------------------------------------------------------------------------'''



a=int(input('输入数字：'))
astr=str(a)
s=''        #反向的字符串
i=len(astr)-1       #索引  下标
while i >= 0:
    s+=astr[i]
    i-=1
print(s)
if s==astr:
    print(a,'是回文数')
else:
    print(a, '不是回文数')




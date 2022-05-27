''''''
'''
continue：跳过，结束本次循环，立即进入下一次循环
        循环体中continue下方分所有代码均被跳过
        只能在循环体中使用
continue和break的异同点：
     相同点：都是只能在循环体中使用
     不同点：continue是跳过本次循环，重新执行循环体的内容
            break是退出循环，执行循环外面的内容  


'''
'''练习1'''
# a=int(input('请输入应付多少：'))
# y=100-a
# while True:
#     if y==0:
#         break
#     if y>=50:
#         y-=50
#         print(50)
#     elif y>=20:
#         y-=20
#         print(20)
#     elif y>=10:
#         y-=10
#         print(10)
#     elif y>=5:
#         y-=5
#         print(5)
#     elif y>=1:
#         y-=1
#         print(1)



'''练习2'''
# a=int(input('请输入应付多少：'))
# m=0
# while True:
#     sq=input('收钱：')
#     if sq=='end':
#         break
#     m+=int(sq)
# print('实际收款：',m)
# y=m-a
# while True:
#     if y==0:
#         break
#     if y>=50:
#         y-=50
#         print(50)
#     elif y>=20:
#         y-=20
#         print(20)
#     elif y>=10:
#         y-=10
#         print(10)
#     elif y>=5:
#         y-=5
#         print(5)
#     elif y>=1:
#         y-=1
#         print(1)



'''练习3'''
# a=int(input('请输入应付多少：'))
# m=0
# while True:
#     sq=input('收钱：')
#     if sq=='end':
#         break
#     m+=int(sq)
# print('实际收款：',m)
# y=m-a
# m50=m20=m10=m5=m1=0
# while True:
#     if y==0:
#         break
#     if y>=50:
#         y-=50
#         m50+=1
#     elif y>=20:
#         y-=20
#         m20+=1
#     elif y>=10:
#         y-=10
#         m10+=1
#     elif y>=5:
#         y-=5
#         m5+=1
#     elif y>=1:
#         y-=1
#         m1+=1
# if m50!=0:
#     print('50元 X',m50)
# if m20!=0:
#     print('20元 X',m20)
# if m10!=0:
#     print('10元 X',m10)
# if m5!=0:
#     print('5元 X',m5)
# if m1!=0:
#     print('1元 X',m1)




'''continue'''
# a=0
# while a<10:
#     a+=1
#     if a%4==0:
#         continue
#     print(a)




'''练习4'''
# a=int(input('请输入一个数：'))
# while a<1000:
#     a+=1
#     if a % 7 ==0 and '7' in str(a):
#         continue
#     print(a)
# print('幸运”7“游戏结束！')



'''--------------------------------------------------------------------------------------------------------------------'''































































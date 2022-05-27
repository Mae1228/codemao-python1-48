''''''
'''
分支结构的嵌套：分支结构一条分支上嵌套另一个分支结构
    语法表示：
        if 判断条件1:
            条件1为真
            if 判断条件2:
                条件2为真
            else:
                条件2为假
        else:
            条件1为假
            if 判断条件3:
                条件3为真
            else:
                条件3为假

比较运算符：
    ==：相等
    !=：不相等
    >=：大于等于，如3>=3为真
    <=：小于等于
    >：大于
    <：小于


'''

'''练习1'''
# yh = '锂电池'
# khs = '作业纸、塑料'
# cy = '鱼骨、炒米饭、鸡蛋壳'
# qt = '大棒骨、渣土、污染纸'
# message = input('请输入要丢弃的垃圾：')
# if message in yh:
#     print('有害垃圾')
# elif message in khs:
#     print('可回收垃圾')
# elif message in cy:
#     print('厨余垃圾')
# elif message in qt:
#     print('其他垃圾')
# else:
#     print('我不知道是什么东西')






'''练习2'''
# yh = '锂电池'
# khs = '作业纸、塑料、电池'
# cy = '鱼骨、炒米饭、鸡蛋壳'
# qt = '大棒骨、渣土、污染纸'
# message = input('请输入要丢弃的垃圾：')
# if message in khs:
#     print('可回收垃圾')
# elif message in yh:
#     print('有害垃圾')
# elif message in cy:
#     print('厨余垃圾')
# elif message in qt:
#     print('其他垃圾')
# else:
#     print('这个我还不会判断呢')






'''练习3'''
# a=input('您要丢弃的垃圾是：')
# if '骨' in a:
#     if a == '大棒骨':
#         print('其他垃圾')
#     else:
#         print('厨余垃圾')
# else:
#     print('这个我还不会判断呢')






'''练习4'''
# xb=input('请输入您的性别：')
# tz=int(input('请输入您的体重：'))
# sg=int(input('请输入您的身高：'))
# if xb == '男':
#     c1=tz-(sg-100)
#     if c1>3:
#         print('胖了')
#     elif c1<-3:
#         print('瘦了')
#     else:
#         print('标准')
# elif xb == '女':
#     c2 = tz - (sg - 110)
#     if c2 > 3:
#         print('胖了')
#     elif c2 < -3:
#         print('瘦了')
#     else:
#         print('标准')
# else:
#     print('输入性别错误')




























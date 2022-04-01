# 匿名函数语法结构：
# lambda 参数1、参数2、参数3：表达式
# 特点
# 1、使用lambda关键字去创建
# 2、没有名字的函数
# 3、匿名函数冒号后面的表达式有且只有一个，注意是表达式而不是语句。
# 4、匿名函数自带return，而这个return 的结果就是表达式计算后的结果。
# 缺点
# lambda 只能是单个表达式，不是一个代码块，lambda 设计只是为了满足简单函数的场景，仅仅能封装有限的逻辑，复杂逻辑实现不了，必须使用def来处理。

def computer(x,y):
    return x+y
    pass
print(computer(10,45))
m=lambda x,y:x+y
print(m(23,19))

result=lambda a,b,c:a*b*c
print(result(12,34,4))

age=25
print("可以参军" if age>18 else'继续上学')
# 可以替换日常双分支语句
functTest=lambda x,y:x if x>y else y
rs=(lambda x,y:x if x>y else y)(16,12)
varsRs=lambda x:(x**2)+890
print(functTest(12,2))
print(rs)
print(varsRs(10))
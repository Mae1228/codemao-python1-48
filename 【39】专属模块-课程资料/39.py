''''''
'''
__pycache__的意义：
    因为第一次执行代码的时候，Python解释器已经把编译的字节码放在__pycache__文件夹中，
    这样以后再次运行的话，如果被调用的模块未发生改变，那就直接跳过编译这一步，
    直接去__pycache__文件夹中去运行相关的 *.pyc 文件，大大缩短了项目运行前的准备时间。

__init__.py 的三个核心作用：
    作为包的标识，不能删除。
    用来实现模糊导入
    导入包实质是执行__init__.py 文件，可以在__init__.py 文件中做这个包的初始化、以及需要统一执行代码、批量导入。

if __name__ == '__main__'作用：
    如果if __name__ == '__main__' 所在模块是被直接运行的，则该语句下代码块被运行，
    如果所在模块是被导入到其他的python脚本中运行的，则该语句下代码块不被运行。
    
模块：一个包含代码的文件，其后缀名是.py，在同一个文件夹下（相对路径）的模块可以直接调用

导入模块：
    import 模块1        import 模块1 as a 
    模块1.函数1()        a.函数1()        

导入多个模块：
    import 模块1,模块2,模块3
    模块1.函数1()
    模块2.函数2()
    模块3.函数3()

包：把相关功能的模块放在一个文件夹，这个文件夹就是一个包，包中还可以包含子包

包与普通文件夹不同的是：
    包内必须包含一个名为__init__.py的文件，在import包时，__init__.py中的代码会自动被执行

导入包中的模块：
    import 包1.子包1.模块1       import 包1.子包1.模块1 as a      
    包1.子包1.模块1.函数1()       a.函数1()     

t.setheading(角度)：以坐标系为基准，设置海龟朝向为某个角度
t.left、t.right(旋转角度)：以海龟当前朝向为基准，向左\向右旋转某个角度

练习题：
    A 
    B
    B
    
'''

'''专属模块-成果包-codemao_head\features\eyes2.py'''
# # 导入绘图工具箱
# import turtle as t
# # 眼睛函数
# def codemao_eyes():
#     #右眼
#     t.hideturtle()
#     t.penup()
#     t.goto(45, -12)
#     t.pendown()
#     t.fillcolor('white')
#     t.begin_fill()
#     t.circle(26)
#     t.end_fill()
#
#     t.penup()
#     t.goto(45, -4)
#     t.pendown()
#     t.fillcolor('black')
#     t.begin_fill()
#     t.circle(18)
#     t.end_fill()
#
#     t.penup()
#     t.goto(50, 20)
#     t.pendown()
#     t.fillcolor('white')
#     t.begin_fill()
#     t.circle(6)
#     t.end_fill()
#
#
#     #左眼--眨眼
#     t.pensize(5)
#     t.penup()
#     t.goto(-45,-4)
#     t.setheading(20)
#     t.pendown()
#     t.forward(30)
#     t.setheading(160)
#     t.forward(30)
#     t.pensize(1)
#     t.setheading(0)
#
# if __name__ == '__main__':
#     codemao_eyes()




'''专属模块-成果包-codemao_head\features\mouth2.py'''
# # 导入绘图工具箱
# import turtle as t
# # 嘴巴函数
# def codemao_mouth():
#     t.pensize(5)
#     t.pencolor('red')
#     t.setheading(0)
#     t.penup()
#     t.goto(0, -60)
#     t.right(45)
#     t.pendown()
#     t.circle(20, 90)
#     t.setheading(180)
#     t.penup()
#     t.goto(0, -60)
#     t.left(45)
#     t.pendown()
#     t.circle(-20, 90)
#     t.hideturtle()





'''------------------------------------------------------------------------------------------------'''



































































































































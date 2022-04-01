'''专属模块-成果包-mask.py'''

# 导入绘图工具箱
import turtle as t
p = t.Pen()
p.hideturtle()
p.speed(10)

# 面具函数
def codemao_mask():
    '''右侧胡须面罩'''
    p.setheading(0)
    p.penup()
    p.goto(0, -15)
    p.right(20)
    p.pendown()
    p.fillcolor('red')
    p.begin_fill()
    p.circle(150, 45)
    p.goto(100, 0)
    p.end_fill()
    p.penup()
    '''左侧胡须面罩'''
    p.setheading(180)
    p.penup()
    p.goto(0, -15)
    p.left(20)
    p.pendown()
    p.fillcolor('red')
    p.begin_fill()
    p.circle(-150, 45)
    p.goto(-100, 0)
    p.end_fill()
    p.penup()
    '''上方面罩'''
    p.setheading(90)
    p.penup()
    p.goto(0, -15)
    p.fillcolor('red')
    p.begin_fill()
    p.goto(100, 0)
    p.pendown()
    p.circle(100, 180)
    p.penup()
    p.goto(0, -15)
    p.end_fill()
    p.penup()
    p.setheading(0)
'''专属模块-成果包-codemao_head\features\nose.py'''

# 导入绘图工具箱
import turtle as t
p = t.Pen()
p.hideturtle()
p.speed(10)

# 鼻子函数'''
def codemao_nose():
    p.setheading(90)
    p.penup()
    p.goto(0, -28)
    p.right(60)
    p.pendown()
    p.fillcolor('orange')
    p.begin_fill()
    p.forward(16)
    p.left(90)
    p.circle(16, 120)
    p.left(90)
    p.forward(16)
    p.end_fill()
    p.penup()
    p.setheading(0)

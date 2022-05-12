'''专属模块-成果包-codemao_head\outline.py'''

import turtle as t
p = t.Pen()
p.hideturtle()
p.speed(10)

# 头部轮廓函数
def codemao_outline():
    p.setheading(0)
    p.penup()
    p.goto(0, -100)
    p.pendown()
    p.fillcolor('floral white')
    p.begin_fill()
    p.circle(100)
    p.end_fill()
    p.penup()
    p.setheading(0)
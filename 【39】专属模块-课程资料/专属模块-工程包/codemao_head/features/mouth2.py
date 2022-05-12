'''专属模块-成果包-codemao_head\features\mouth2.py'''

# 导入绘图工具箱
import turtle as t

# 嘴巴函数


def codemao_mouth():
    t.pensize(5)
    t.pencolor('red')
    t.setheading(0)
    t.penup()
    t.goto(0, -60)
    t.right(45)
    t.pendown()
    t.circle(20, 90)
    t.setheading(180)
    t.penup()
    t.goto(0, -60)
    t.left(45)
    t.pendown()
    t.circle(-20, 90)
    t.hideturtle()

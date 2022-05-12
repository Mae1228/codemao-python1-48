'''专属模块-成果包-codemao_head\features\mouth.py'''

# 导入绘图工具箱
import turtle as t

# 嘴巴函数
def codemao_mouth():
    t.penup()
    t.goto(-20, -60)
    t.pendown()
    t.right(90)
    t.fillcolor('red')
    t.begin_fill()
    t.circle(20, 180)
    t.end_fill()
    t.setheading(180)
    t.forward(40)
    t.hideturtle()


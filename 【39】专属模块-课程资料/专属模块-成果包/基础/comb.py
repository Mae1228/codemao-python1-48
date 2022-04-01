'''专属模块-成果包-comb.py'''

# 导入绘图工具箱
import turtle as t
p = t.Pen()
p.hideturtle()
p.speed(10)

# 发冠函数'''
def codemao_comb():
    p.setheading(72)
    p.penup()
    p.goto(0, 0)
    p.forward(100)
    p.pendown()
    p.right(30)
    p.fillcolor('orange')
    p.begin_fill()
    p.circle(25, 150)
    p.circle(-100, 18)
    p.circle(-60, 20)
    p.circle(-20, 30)
    p.left(130)
    p.circle(35, 60)
    p.circle(20, 30)
    p.circle(-15, 70)
    p.end_fill()
    p.penup()
    p.setheading(0)

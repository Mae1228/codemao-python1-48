'''专属模块-成果包-logo.py'''

# 导入绘图工具箱
import turtle as t
p = t.Pen()
p.hideturtle()
p.speed(10)

# logo函数
def codemao_logo():
    p.setheading(35)
    p.penup()
    p.goto(0, 30)
    p.pendown()
    p.fillcolor('orange')
    p.begin_fill()
    p.forward(55)
    p.left(110)
    p.forward(55)
    p.left(70)
    p.forward(55)
    p.left(110)
    p.forward(55)
    p.end_fill()
    p.penup()
    p.goto(-19, 36)
    p.write('编', font=("Arial", 31, 'bold'))
    p.setheading(0)

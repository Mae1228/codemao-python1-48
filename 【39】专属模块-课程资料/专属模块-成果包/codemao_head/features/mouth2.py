'''专属模块-成果包-codemao_head\features\mouth2.py'''

# 导入绘图工具箱
import turtle as t

def codemao_mouth():
     # 猫嘴
    t.penup()
    t.setheading(0)
    t.pensize(5)
    t.pencolor('red')
    t.goto(0, -50)
    t.pendown()
    t.right(45)
    t.circle(20, 90)
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.left(180)
    t.circle(-20, 90)
    t.hideturtle()
# codemao_mouth()
# t.done()




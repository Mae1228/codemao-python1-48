'''专属模块-成果包-codemao_head\features\eyes2.py'''

# 导入绘图工具箱
import turtle as t

# 眼睛函数
def codemao_eyes():
    t.hideturtle()
    t.penup()
    t.goto(45, -12)
    t.pendown()
    t.fillcolor('white')
    t.begin_fill()
    t.circle(26)
    t.end_fill()

    t.penup()
    t.goto(45, -4)
    t.pendown()
    t.fillcolor('black')
    t.begin_fill()
    t.circle(18)
    t.end_fill()

    t.penup()
    t.goto(50, 20)
    t.pendown()
    t.fillcolor('white')
    t.begin_fill()
    t.circle(6)
    t.end_fill()

    # 眨眼睛
    t.penup()
    t.pensize(5)
    t.goto(-25, 10)
    t.pendown()
    t.left(150)
    t.forward(35)
    t.penup()
    t.goto(-25,10)
    t.pendown()
    t.right(-45)
    t.forward(35)
    # t.done()


if __name__ == '__main__':
    codemao_eyes()

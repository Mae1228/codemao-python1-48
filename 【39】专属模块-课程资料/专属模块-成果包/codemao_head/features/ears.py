'''专属模块-成果包-codemao_head\features\ears.py'''

# 导入绘图工具箱
import turtle as t
p = t.Pen()
p.hideturtle()
p.speed(10)

# 耳朵函数'''
def codemao_ears():
    #右侧
    p.setheading(27)
    p.penup()
    p.goto(0, 0)
    p.forward(100)
    p.left(35)
    p.pendown()
    p.fillcolor('floral white')
    p.begin_fill()
    p.circle(80, 40)
    p.left(70)
    p.circle(80, 40)
    p.end_fill()
    #左侧
    p.setheading(180 - 27)
    p.penup()
    p.goto(0, 0)
    p.forward(100)
    p.right(35)
    p.pendown()
    p.fillcolor('floral white')
    p.begin_fill()
    p.circle(-80, 40)
    p.right(70)
    p.circle(-80, 40)
    p.end_fill()
    p.penup()
    p.setheading(0)

if __name__ == '__main__':
    codemao_ears()
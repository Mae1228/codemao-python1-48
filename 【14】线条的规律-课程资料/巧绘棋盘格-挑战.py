'''巧绘棋盘格-挑战'''

#调用turtle模块
import turtle as t
#绘制棋盘格的竖线，通过设置步长去改变每条竖线的起/终点坐标
for x in range(-90, 91, 10):
    t.penup()
    t.goto(x, -90)
    t.pendown()
    t.goto(x, 90)
#绘制棋盘格的横线，通过设置步长去改变每条横线的起/终点坐标
for x in range(-90, 91, 10):
    t.penup()
    t.goto(-90, x)
    t.pendown()
    t.goto(90, x)
t.hideturtle()
t.done()




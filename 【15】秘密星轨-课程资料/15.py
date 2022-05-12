''''''
'''
t.circle(半径,弧长)：
    半径：
        正数：圆心在海龟左侧
        负数：圆心在海龟右侧
    弧长：不写默认是360
        正数：向着海龟的方向前进
        负数：向着海龟的方向后退
填充三剑客：
    t.fillcolor(颜色字符串)
    t.begin_fill()
    t.end_fill()
填充区域为起点和终点连线后所围成的封闭图形

    


'''
'''实践一'''
# import turtle as t
# t.speed(0)
# i=1
# while i<=360:
#     t.forward(1)
#     t.left(1)
#     i+=1
# t.hideturtle()
# t.done()




'''实践二'''
# import turtle as t
# t.circle(100,270)
# t.hideturtle()
# t.done()




'''实践三'''
# import turtle as t
# t.circle(-100,180)
# t.hideturtle()
# t.done()




'''实践四:1'''
# import turtle as t
# t.circle(100,-90)
# t.hideturtle()
# t.done()




'''实践四:2'''
# import turtle as t
# t.left(180)
# t.circle(-100,90)
# t.hideturtle()
# t.done()




'''填充三剑客'''
# import turtle as t
# t.fillcolor('orange')
# t.begin_fill()
# t.circle(100,270)
# t.end_fill()
# t.done()





'''实践五'''
# import turtle as t
# t.fillcolor('cyan')
# t.begin_fill()
# t.circle(-100,180)
# t.end_fill()
# t.done()




'''项目'''
# import turtle as t
# import random
# t.speed(10)
# t.pencolor('black')
# t.penup()
# t.goto(-400,-400)
# t.pendown()
# t.fillcolor('black')
# t.begin_fill()
# i=1
# while i<=4:
#     t.forward(800)
#     t.left(90)
#     i+=1
# t.end_fill()
# t.pencolor('cyan')
# j=1
# while j<=50:
#     t.penup()
#     t.goto(0,0)
#     r=random.randint(1,400)
#     h=random.randint(1,360)
#     t.forward(r)
#     t.left(90)
#     t.pendown()
#     t.circle(r,h)
#     j+=1
# t.hideturtle()
# t.done()




'''circle螺旋线'''
# import turtle as t
# t.speed(0)
# i=1
# while i<=200:
#     t.circle(i,180)
#     i+=10
# t.hideturtle()
# t.done()





'''----------------------------------------------------------------------------------'''











import turtle as t
t.penup()
t.goto(-400,-400)
t.pendown()
t.fillcolor('black')
t.begin_fill()
i=1
while i<=4:
    t.forward(800)
    t.left(90)
    i+=1
t.end_fill()


t.done()


















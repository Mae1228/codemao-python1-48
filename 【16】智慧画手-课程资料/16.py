''''''
'''
随机产生小数：uniform(小,大)
随机产生整数：randint(小,大)
RGB色彩体系：范围是0~1，0代表最暗，1代表最亮
    R：红色
    G：绿色
    B：蓝色
t.colormode(数值)：构成颜色三元组的 r, g, b 数值必须在 0..数值范围之内
'''
'''circle螺旋线'''
# import turtle as t
# t.speed(0)
# for i in range(0,200,10):
#     t.circle(i,180)
# t.hideturtle()
# t.done()


'''多彩繁星'''
# import turtle as t
# import random
# t.speed(0)
# t.pencolor('black')
# t.fillcolor('black')
# t.penup()
# t.goto(-300,-300)
# t.pendown()
# t.begin_fill()
# for i in range(4):
#     t.forward(600)
#     t.left(90)
# t.end_fill()
# for i in range(100):
#     r=random.uniform(0,1)
#     g=random.uniform(0,1)
#     b=random.uniform(0,1)
#     x=random.randint(-300,300)
#     y=random.randint(-300,300)
#     size=random.randint(1,5)
#     t.penup()
#     t.goto(x,y)
#     t.pensize(size)
#     t.pencolor(r,g,b)
#     t.pendown()
#     t.forward(1)
# t.hideturtle()
# t.done()




'''斑马圆'''
# import turtle as t
# t.speed(0)
# r=100
# for i in range(10):
#     if i%2==0:
#         t.fillcolor('black')
#     else:
#         t.fillcolor('white')
#     t.begin_fill()
#     t.circle(r)
#     t.end_fill()
#     r-=10
# t.hideturtle()
# t.done()




'''----------------------------------------------------------------------------------------------'''






'''circle螺旋线'''
# import turtle as t
# t.speed(0)
# i=1
# while i<=201:
#     t.circle(i,180)
#     i+=10
# t.hideturtle()
# t.done()





'''多彩繁星'''
# import turtle as t
# import random
# t.speed(0)
# t.pencolor('black')
# t.fillcolor('black')
# t.penup()
# t.goto(-300,-300)
# t.pendown()
# t.begin_fill()
# i=1
# while i<=4:
#     t.forward(600)
#     t.left(90)
#     i+=1
# t.end_fill()
# j=1
# while j<=100:
#     r=random.uniform(0,1)
#     g=random.uniform(0,1)
#     b=random.uniform(0,1)
#     x=random.randint(-300,300)
#     y=random.randint(-300,300)
#     size=random.randint(1,5)
#     t.penup()
#     t.goto(x,y)
#     t.pensize(size)
#     t.pencolor(r,g,b)
#     t.pendown()
#     t.forward(1)
#     j+=1
# t.hideturtle()
# t.done()




'''斑马圆'''
# import turtle as t
# t.speed(0)
# r=100
# i=1
# while i<=10:
#     if i%2==1:
#         t.fillcolor('black')
#     else:
#         t.fillcolor('white')
#     t.begin_fill()
#     t.circle(r)
#     t.end_fill()
#     r-=10
#     i+=1
# t.hideturtle()
# t.done()






'''-----------------------------------------------------------------------------------------------------------------------------'''



'''
画了10个圆
黑色（不能被2整除）：1 3 5 7 9
白色（能被2整除）：2 4 6 8 10

数%2==0

圆不断变小：半径变小

'''
import turtle as t
t.speed(0)
i=1     #次数
r=100       #半径
while i <= 10:
    if i % 2==0:
        t.fillcolor(1,1,1)
    else:
        t.fillcolor(0,0,0)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    i+=1
    r-=10
t.hideturtle()
t.done()














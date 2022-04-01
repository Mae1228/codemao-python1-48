'''光速搬运工-成果包'''

#复制图片
with open('房子.png', 'rb') as p:
    pic = p.read()
with open('房子副本.png', 'wb') as p2:
    p2.write(pic)



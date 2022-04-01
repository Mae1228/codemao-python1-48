''''''
'''
像素：组成图片的最小单位
img.open(文件名)：打开图片
img.load()：加载图片像素点的数据
img.size：获取图片的宽和高
img.show()：展示图片
img.save()：保存新图片
RGB色彩：范围时0~255，0代表最暗，255代表最亮
    R：红色
    G：绿色
    B：蓝色
    红色：(255,0,0)
    白色：(255,255,255)
    蓝色：(0,0,0)
元组tuple：有序存储多个内容，特点是不能修改
    t=(1,'2')
    t=tuple()
    t=(1,)
'''

'''图像修复工程师'''
# from PIL import Image
# img=Image.open('损坏的监控图像.png')
# width,height=img.size
# print(width,height)
# img_array=img.load()
# for x in range(width):
#     for y in range(height):
#         r=img_array[x,y][0]
#         g=img_array[x,y][1]
#         b=img_array[x,y][2]
#         img_array[x,y]=(r,0,0)
# img.show()





'''懵圈阿短反色'''
# from PIL import Image
# img=Image.open('懵圈阿短反色.png')
# width,height=img.size
# print(width,height)
# img_array=img.load()
# for x in range(width):
#     for y in range(height):
#         r=img_array[x,y][0]
#         g=img_array[x,y][1]
#         b=img_array[x,y][2]
#         r1=255-r
#         g1=255-g
#         b1=255-b
#         img_array[x,y]=(r1,g1,b1)
# img.show()




'''星月夜'''
# from PIL import Image
# img=Image.open('星月夜.png')
# width,height=img.size
# print(width,height)
# img_array=img.load()
# for x in range(width):
#     for y in range(height):
#         r=img_array[x,y][0]
#         g=img_array[x,y][1]
#         b=img_array[x,y][2]
#         r1=255-r
#         g1=255-g
#         b1=255-b
#         img_array[x,y]=(r1,g1,b1)
# img.show()




'''元组'''
# t1=(1,'2','%%%')
# print(type(t1))
# t2=tuple()
# print(type(t2))
# t3=(11)
# print(type(t3))
# t4=(1222,)
# print(type(t4))



'''------------------------------------------------------------------------------------------------'''











































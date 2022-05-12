''''''
'''
PIL库：图像处理库
像素：组成图片的最小单位
Image.open('路径及文件名')：读取图片文件
    相对路径：文件工作的位置，即项目和文件在同一个位置
    绝对路径：文件在电脑磁盘的位置
load()：加载图片文件，接收像素数据，可以通过坐标的形式查看
RGB色彩：一种通用的颜色标准，按照色光三原色来设计的
        亮度范围是：0~255，0代表最暗，255代表最亮
        R：红色
        G：绿色
        B：蓝色
size：获取图片的尺寸，第一个参数表示宽度，第二个参数表示高度
元组：有序，存放各种数据类型
    特性：元组是不可变的，无法对元组本身进行修改
    创建：
        t=(1,)
        t=tuple()
save('路径及新文件名')：保存图片文件
show()：展示图片文件
max(a,b,c)：获取元素中的最大值并返回
练习题：
    C 
    A 
    C 
'''

'''练习1'''
# from PIL import Image
# img=Image.open('steak.jpg')
# img_array=img.load()
# print(img_array[0,0])
# print(img_array[2,2])




'''练习2'''
# from PIL import Image
# img=Image.open('steak.jpg')
# img_array=img.load()
# width,height=img.size
# print(width,height)





'''练习3'''
# from PIL import Image
# img=Image.open('steak.jpg')
# img_array=img.load()
# img_array[0,0]=(255,0,0)
# img.show()
# img.save('red_steak.jpg')


'''元组'''
# t1=(1,'a',1.23)
# t2=tuple()
# t3=()
# print(type(t3))
# t4=(1)
# print(type(t4))
# t5=('1',)
# print(type(t5))





'''练习4'''
# from PIL import Image
# img=Image.open('steak.jpg')
# img_array=img.load()
# width,height=img.size
# for i in range(width):
#     for j in range(height):
#         img_array[i,j]=(0,0,255)
# img.show()
# img.save('blue_steak.jpg')



'''项目'''
# from PIL import Image
# img=Image.open('steak.jpg')
# img_array=img.load()
# width,height=img.size
# for i in range(width):
#     for j in range(height):
#         r=img_array[i,j][0]
#         g=img_array[i,j][1]
#         b=img_array[i,j][2]
#         m=max(r,g,b)
#         if m==r:
#             if r<=200:
#                 r+=55
#             else:
#                 r=255
#             img_array[i,j]=(r,g,b)
# img.show()
# img.save('new_steak.jpg')





'''---------------------------------------------------------------------------------------------------------------------'''









































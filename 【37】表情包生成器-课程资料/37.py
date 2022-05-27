''''''
'''
PIL库：图像处理库
    Image模块：
        PIL库基本模块，比如：加载图像和创建图像
    ImageDraw模块：
        提供了图像对象的简单2D绘制，如：文本、图像等 
    ImageFont模块：
        与ImageDraw模块的text()方法一起使用，用于设置字体

Image模块：
    open('路径及文件名')：读取图片
        相对路径：目标文件在项目的工作位置，及目标文件及项目在一个位置
        绝对路径：目标文件在电脑磁盘的位置 
    show()：显示图片
    save('路径及新文件名')：保存图片文件
   
ImageDraw模块：
    Draw()：
        创建一个绘制给定图像的对象。
        创建了一支用于在img上绘画的画笔 
    text(xy=(在图像中的坐标),text='绘制的文本',fill='文本的颜色')：
        在图像的给定位置绘制字符串（无法绘制中文）
        xy=文本的左上角（在图像中的位置）
            坐标系统：左上角(0,0)
        text=要绘制的文本
        fill=文本的颜色
            字符串或RGB元组，如：'red'、(255,0,0)

ImageFont模块：
    truetype('字体文件',字体大小)：
        加载TrueType字体文件（.ttf），并以给定大小创建一个字体对象
    
easygui库：简单用户图形界面
    multenterbox(msg='要显示的消息',title='窗口标题',fields='输入框名称列表或元组')：
        显示多个框，用户可以在其中输入文本
        返回值：用户输入所有文本（str）的列表，取消则返回NOne
        
练习题：
    B
    B        
    C

'''

'''练习2'''
# from PIL import Image
# img=Image.open('编程猫.png')
# img.show()
# img.save('编程猫2.png')





'''ImageDraw.Draw()'''
# from PIL import Image
# from PIL import ImageDraw
# img=Image.open('编程猫.png')
# draw=ImageDraw.Draw(img)
# img.show()
# img.save('新图片.png')






'''text()'''
# from PIL import Image
# from PIL import ImageDraw
# img=Image.open('编程猫.png')
# draw=ImageDraw.Draw(img)
# draw.text(xy=(300,400),text='test1',fill='red')
# draw.text(xy=(300,300),text='test2',fill=(255,255,0))
# img.show()
# img.save('新图片1.png')





'''ImageFont.truetype()'''
# from PIL import Image
# from PIL import ImageDraw
# from PIL import ImageFont
# img=Image.open('编程猫.png')
# draw=ImageDraw.Draw(img)
# font=ImageFont.truetype('simhei.ttf',35)
# draw.text(xy=(300,400),text='中文test1',fill='red',font=font)
# draw.text(xy=(300,300),text='test2',fill=(255,255,0))
# img.show()
# img.save('新图片2.png')





'''multenterbxo()'''
# import easygui as g
# fieldNames=('姓名','年龄','兴趣爱好')
# b=g.multenterbox(msg='输入个人信息',title='个人信息收集',fields=fieldNames)
# print(b)





'''表情包生成器'''
# from PIL import Image,ImageDraw,ImageFont
# import easygui as g
# names=('原图片(含后缀)','另存为(含后缀)','添加文字','文字大小','文字位置(x轴)','文字位置(y轴)')
# alist=g.multenterbox(msg='请填写信息',title='表情包生成器',fields=names)
# print(alist)
# size=int(alist[3])
# x=int(alist[4])
# y=int(alist[5])
# img=Image.open(alist[0])
# f=ImageFont.truetype('simhei.ttf',size)
# d=ImageDraw.Draw(img)
# d.text(xy=(x,y),text=alist[2],fill='red',font=f)
# img.show()
# img.save(alist[1])






'''----------------------------------------------------------------------------------------------'''























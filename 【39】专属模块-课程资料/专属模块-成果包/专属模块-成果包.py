'''专属模块-成果包'''

# 导入自定义模块(包)
import turtle as t   #导入系统工具包
import codemao_head.outline as outline # 第二种   导入相同文件夹的包
import codemao_head.features.ears as ears  # 导入相同文件夹里面的子包
import codemao_head.features.eyes as eyes
import codemao_head.features.mouth as mouth
import codemao_head.features.nose as nose
import mask, logo, comb # 第一种  相同文件夹里面的py模块




# 使用自定义模块(包)绘制编程猫勋章
outline.codemao_outline()
ears.codemao_ears()
comb.codemao_comb()
mask.codemao_mask()
eyes.codemao_eyes()
mouth.codemao_mouth()
nose.codemao_nose()
logo.codemao_logo()

# 画面停留
t.done()



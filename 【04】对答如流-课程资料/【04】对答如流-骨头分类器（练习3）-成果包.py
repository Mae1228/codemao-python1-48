'''练习3成果包——骨头分类器'''
'''
骨头分类器
其中有许多的垃圾都很难判断到底是哪一类，比如让人头疼的骨头：鱼骨、鸡骨、大棒骨
根据以上提示的骨头分类方式，制作骨头分类提示小帮手，输入要扔的垃圾，给出判定类型
如:
例1:
Input:
您要丢弃的垃圾是:鱼骨
Output:
这种小骨头，是属于厨余垃圾
例2:
Input:
您要丢弃的垃圾是:大棒骨
Output:
这个虽然来自厨房，但是属于其他垃圾哦
例3:
Input:
您要丢弃的垃圾是:气球
Output:
这个我还不会判断呢
'''
rubbish = input('您要丢弃的垃圾是:')
if '骨' in rubbish:
    if '大棒' in rubbish:
        print('这个虽然来自厨房，但是属于其他垃圾哦')
    else:
        print('这种小骨头，是属于厨余垃圾')
else:
    print('这个我还不会判断呢')


import jieba
sentence = '海口市美兰区编程猫超级可爱。'
words = jieba.cut(sentence,cut_all=False)
s = '/'.join(words)
print(s)


import jieba
sentence = '海口市美兰区编程猫超级可爱。'
words = jieba.cut(sentence)
s = '/'.join(words)
print(s)


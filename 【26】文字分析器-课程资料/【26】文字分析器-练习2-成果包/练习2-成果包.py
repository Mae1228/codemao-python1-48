import jieba
sentence = '编程猫超级可爱。'
jieba.load_userdict("dict.txt")
words = jieba.cut(sentence)
s = '/'.join(words)
print(s)


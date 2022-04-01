import jieba.analyse

with open('text.txt','r',encoding = 'utf-8') as f:
    sentence = f.read()
words = jieba.analyse.extract_tags(sentence, topK=10)
for i in words:
    print(i)


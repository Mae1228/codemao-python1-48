''''''
'''


'''
'''45项目'''
#词典加载
# def load_dict():
#     wordsDict={}
#     with open('wordsSpace.txt','r',encoding='utf-8') as f:
#         wordList=f.readlines()
#         # print(wordList)
#     for i in wordList:
#         wList=i.split('#')
#         # print(wList)
#         wordDict={
#             'NO.':wList[0],
#             'mean':wList[2]
#         }
#         # print(wordDict)
#         wordsDict[wList[1]]=wordDict
#     # print(wordsDict)
#     return wordsDict
#
# #单词查询
# def search_by_ENG(word):
#     try:
#         res=word+' '+wordsDict[word]['mean']
#     except:
#         res='Not fount'
#     return res
#
# #菜单
# def menu():
#     print('-'*30)
#     print('英译中查找单词功能请按：1')
#     print('退出功能请按：0')
#     print('-'*30)
#
#
# #主函数
# wordsDict=load_dict()
# menu()
# while True:
#     gn=input('输入想要使用的功能(#查看功能)：')
#     if gn=='1':
#         while True:
#             word=input('查找单词(按0返回)：')
#             if word=='0':
#                 break
#             res=search_by_ENG(word)
#             print(res)
#     elif gn=='#':
#         menu()
#     elif gn=='0':
#         break



'''--------------------------------------------------------------------------------------------------'''


#词典加载
def load_dict():
    wordsDict={}
    with open('wordsSpace.txt','r',encoding='utf-8') as f:
        wordList=f.readlines()
        # print(wordList)
    for i in wordList:
        wList=i.split('#')
        # print(wList)
        wordDict={
            'NO.':wList[0],
            'mean':wList[2],
            'link':wList[3][:-1]
        }
        # print(wordDict)
        wordsDict[wList[1]]=wordDict
    # print(wordsDict)
    return wordsDict

#单词查询
def search_by_ENG(word):
    try:
        res=word+' '+wordsDict[word]['mean']
        if wordsDict[word]['link']:
            res +=' 联想词：'+wordsDict[word]['link']
    except KeyError:
        res='Not fount'
    return res

# 联想词添加
def add_linked_words(word,addWord):
    wordsDict[word]['link']+=addWord
    wordsDict[word]['link']+=','
    return wordsDict

#词典保存
def save_dict():
    with open('wordsSpace.txt', 'w', encoding='utf-8') as f:
        for k,v in wordsDict.items():
            line=v['NO.']+'#'+k+'#'+v['mean']+'#'+v['link']+'\n'
            f.write(line)


#菜单
def menu():
    print('-'*30)
    print('英译中查找单词功能请按：1')
    print('添加联系词功能请按：2')
    print('退出功能请按：0')
    print('-'*30)




#主函数
wordsDict=load_dict()
menu()
while True:
    gn=input('输入想要使用的功能(#查看功能)：')
    if gn=='1':
        while True:
            word=input('查找单词(按0返回)：')
            if word=='0':
                break
            res=search_by_ENG(word)
            print(res)
    elif gn=='2':
        word=input('请输入目标单词：')
        addWord=input('请输入添加的联想词：')
        wordsDict=add_linked_words(word, addWord)#更新大字典
        print('添加成功！')
    elif gn=='#':
        menu()
    elif gn=='0':
        save_dict()
        break



































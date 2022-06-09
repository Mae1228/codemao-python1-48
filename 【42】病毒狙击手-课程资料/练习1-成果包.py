'''练习1-成果包'''

filelist = ['file.txt', 'fille.txt','file2.txt']
for name in filelist:
    try:
        f = open(name, 'r')
    except IOError:
        print('没有找到文件!')
    else:
        t = f.read()
        print(t)
        f.close()

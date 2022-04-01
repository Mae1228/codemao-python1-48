#递归实现树形结构的遍历
import os #引入文件操作模块
def findFile(file_Path):#定义文件路径函数
    listRs=os.listdir(file_Path)#得到该路径下所有文件夹
    print(listRs)  #返回列表类型
    for fileItem in listRs:
        full_Path=os.path.join(file_Path,fileItem)
        if os.path.isdir(full_Path):#判断是否是文件夹
            findFile(full_Path)  #如果是一个文件夹继续遍历
        else:
            print(fileItem) #直接打印文件名
    else:
        return
findFile('D:\\赵莹的')  #要遍历得文件路径，例如D:\\赵莹的

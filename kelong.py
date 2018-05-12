import os
"""
题目：复制目录到文件夹
dir:原文件目录
dir2:目标文件目录
"""
def listfile(dir,dir2):

    for file in os.listdir(dir):
        path = os.path.join(dir,file)   #拼接原目录的绝对路径
        path2 = os.path.join(dir2,file) #拼接目标目录的绝对路径

        if os.path.isdir(path): #判断原是文件还是目录
            os.makedirs(path2)  #创建相应的目标目录
            listfile(path,path2)    #递归调用listfile()函数

        if os.path.isfile(path):    #是文件就进行复制
            df = open(path, "rb")
            xf = open(path2, "wb")

            for line in df.readlines(): #依次读取每行
                xf.write(line)

            df.close()
            xf.close()

dir = r"E:\pycscs"
dir2 = r"E:\copy"
listfile(dir, dir2)
print('复制完成，请到dir2设置的目录中查看文件')
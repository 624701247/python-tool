import os
import shutil
import codecs
import time
import re
import socket

# 公用函数


######################################################################################################
# 获取我的ip地址
def getMyIp():
	myname = socket.getfqdn(socket.gethostname())
	myaddr = socket.gethostbyname(myname)
	return myaddr


######################################################################################################
# 获取文件的创建时间戳
def getCreateTime(filePath):
    timestamp = os.path.getmtime(filePath)
    return int(timestamp)


######################################################################################################
#创建目录结构
def mkdir(path):
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path) 
    return path


######################################################################################################
#拷贝或覆盖文件夹
def copyFolder(srcPath, destPath):
    mkdir(destPath)
    for path in os.listdir(srcPath):
        subSrcPath = os.path.join(srcPath, path)
        subDestPath = os.path.join(destPath, path)
        if os.path.isfile(subSrcPath):  
            coverFile(subSrcPath, subDestPath)
        else:
            if os.path.exists(subDestPath):    #删除子目录
                shutil.rmtree(subDestPath)
            copyFolder(subSrcPath, subDestPath)


######################################################################################################
# kone point : 双击运行，运行后不会自动关闭，停留等待用户输入参数
parm = input("没报错就是成功了，回车吧！")
print('你刚刚输入的是： ' + str(parm))

aa = input("回车关闭")
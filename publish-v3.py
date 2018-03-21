import os
import shutil
import codecs
import time

#检测脚本是否用了  let  
def checkHaLet(srcFile):
     with open(srcFile,"r", encoding='utf-8') as file:
        for line in file.readlines():
            if line.find('let') != -1:
                return True
        return False


#拷贝或覆盖单个文件
def coverFile(srcFilePath, destFliePath):
    if os.path.exists(destFliePath):
        os.remove(destFliePath)
    shutil.copy(srcFilePath, destFliePath)


#创建目录结构
def mkdir(path):
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path) 
    return path


# 打包egret
# param ver : 打包版本号
# return 打出来的包路径
def egretPublish(ver):
    curPath = os.getcwd()
    st = os.system('egret publish --version ' + ver)
    if st == 0:
        binPath = curPath + '\\bin-release\\web\\' + ver
        # print('打包成功：' + binPath)
        return binPath
    else :
        print('error: 打包失败！')
        return ''


#拷贝或覆盖文件夹
def copyFolder(srcPath, destPath):
    for path in os.listdir(srcPath):
        subSrcPath = os.path.join(srcPath, path)
        subDestPath = os.path.join(destPath, path)
        if os.path.isfile(subSrcPath):  
            coverFile(subSrcPath, subDestPath)
        else:
            if os.path.exists(subDestPath):    #删除子目录
                shutil.rmtree(subDestPath)
            copyFolder(subSrcPath, mkdir(subDestPath))


# 拷贝index.html 并添加版本号
def copyIndexHtml(srcFile, targetDir, newVer):
    hasAddVer = False
    targetfile = open(targetDir + '\index.html', "w+", encoding='utf-8')
    count = 0
    with open(srcFile,"r",encoding='utf-8') as file:
        for line in file.readlines():
            count = count + 1
            if line.find('var BIN_VER') != -1 and hasAddVer == False:
                targetfile.write('var BIN_VER = ' + newVer + '\n' )
                hasAddVer = True
            elif line.find('index.css') != -1:
                targetfile.write('<link rel="stylesheet" type="text/css" href="css/index.css?' + newVer + '" />\n' )
            else :
                targetfile.write(line) 
    targetfile.close()


# 拷贝index.less 并添加版本号、并编译less
def copyIndexLess(srcFile, targetDir, newVer):
    hasAddVer = False
    targetfile = open(targetDir + '\index.less', "w+", encoding='utf-8')
    count = 0
    with open(srcFile, "r", encoding='utf-8') as file:
        for line in file.readlines():
            count = count + 1
            if line.find('@ver') != -1 and hasAddVer == False:
                targetfile.write('@ver:"?' + newVer + '";\n' )
                hasAddVer = True
            else :
                targetfile.write(line) 
    targetfile.close()
    oldDir = os.getcwd()
    os.chdir(targetDir)
    st = os.system('lessc --clean-css --autoprefix index.less index.css')
    os.chdir(oldDir)
    if st == 0:
        return True
    else :
        return False


# default.res.json 资源添加版本号
def defaultResJson(tarFile, newVer):
    cont = ''
    with open(tarFile, "r", encoding='utf-8') as file:
        for line in file.readlines():
            if line.find('"url"') != -1:
                pos = line.rfind('"')
                cont += line[0:pos] + '?' + newVer + line[pos:len(line)]
            else:
                cont += line
    file.close()
    with open(tarFile,"w",encoding="utf-8") as changeFile:
        changeFile.write(cont)
    changeFile.close()
    


# git提交并推送
def gitPusher(path, log):
    isSucc = os.chdir(path)
    curPath = os.getcwd()
    if curPath == path:
        os.system('git add .')
        os.system('git commit -m ' + log)
        os.system('git push')
    else :
        print('error: 切换工作目录失败！')



'''
kone read me:
1、此py脚本放在egret工程的根目录下，
2、指定好游戏发布的git目录 gitPath，该git目录要先自己个git clone好
3、开发完运行此脚本,则会自动打包，然后拷贝新包文件到gitPath并提交、推送上git
4、该git有其他人改过要自己手动去同步
'''

############### start of python
gitPathH5 = 'E:\work\git-fac\kxbl(kone-test-prj'
prjPath = os.getcwd()
resVer = str(int(time.time())) # 资源版本号， 图片、声音、json等
print('资源版本号: ' + str(resVer))

# step 1: egret 打包 
lt = time.localtime(time.time())
egVer = str(lt.tm_mon) + '-' + str(lt.tm_mday) + '--' + str(lt.tm_hour) + '-' + str(lt.tm_min)
dirPath = egretPublish(egVer)
if dirPath == '':
    print("error : 打包失败！")
    os._exit(0)


# step 2: 拷贝 index.html 到包中， 并添加版本号    
filePath = prjPath + '\index.html'
if checkHaLet(filePath):
    print("error : index.html 有 let")
    os._exit(0)
copyIndexHtml(filePath, dirPath, resVer)


# step 3: 拷贝 public/carry.js 到包中
filePath = prjPath + '\public\carry.js'
if checkHaLet(filePath):
    print("error : carry.js 有 let")
    os._exit(0)
shutil.copy(filePath, mkdir(dirPath + '\public'))


# step 4: 拷贝 css/index.css 到包中
isSucc = copyIndexLess(prjPath + '\css\index.less', mkdir(dirPath + '\css'), resVer)
if isSucc == False:
    print('error : less 编译失败！')
    os._exit(0)


# step 5:  default.res.json 资源添加版本号
# 不能写成： '\resource\default.res.json' , 因为 \r  会被转义
defaultResJson(dirPath + '/resource/default.res.json', resVer)


# step 6: 拷贝其他引入的文件
# shutil.copy(prjPath + '\public\sarea.js', dirPath + '\public')  //拷贝其他js
# shutil.copy(prjPath + '\css\sarea.css', dirPath + '\css')   //拷贝其他css


# step 7: 拷贝包到对应git目录上
# copyFolder(dirPath, gitPathH5)


# step 8: 提交git
# gitPusher(gitPathH5, 'ver:' + ver)

############### end of python


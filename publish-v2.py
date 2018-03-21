import os
import shutil
import codecs
import time

# 打包egret
# return 打出来的包路径
def egretPublish():
    curPath = os.getcwd()
    lt = time.localtime(time.time())
    ver = str(lt.tm_mon) + '-' + str(lt.tm_mday) + '--' + str(lt.tm_hour) + '-' + str(lt.tm_min)
    st = os.system('egret publish --version ' + ver)
    if st == 0:
        binPath = curPath + '\\bin-release\\web\\' + ver
        print('打包成功：' + binPath)
        return binPath
    else :
        print('error: 打包失败！')
        return ''


# 移动文件并覆盖
def coverFiles(srcPath, destPath):
    for fileName in os.listdir(srcPath):
        if fileName == 'index.html':
            # print('注意：不拷贝index.html, 请手动来！')
            continue
        oldFilePath = os.path.join(destPath, fileName) 
        if os.path.exists(oldFilePath):
            if os.path.isfile(oldFilePath):
                os.remove(oldFilePath)
            else :
                shutil.rmtree(oldFilePath)
        shutil.move(os.path.join(srcPath, fileName), destPath)
    print('文件覆盖成功!')


# 拷贝index.html 并添加版本号
def copyIndexHtml(srcFile, targetDir):
    hasAddVer = False
    targetfile = open(targetDir + '/index.html', "w+", encoding='utf-8')
    count = 0
    with open(srcFile,"r",encoding='utf-8') as file:
        for line in file.readlines():
            count = count + 1
            if line.find('var BIN_VER') != -1 and hasAddVer == False:
                newVer = str(int(time.time()))
                targetfile.write('var BIN_VER = ' + newVer + '\n' )
                hasAddVer = True
                print('newVer : ' + newVer)
            else :    
                targetfile.write(line) 
    targetfile.close()


# git提交并推送
def gitPusher(path, log):
    isSucc = os.chdir(path)
    curPath = os.getcwd().replace('\\', '/')
    if curPath == path or curPath == path + '/':
        os.system('git add .')
        os.system('git commit -m ' + log)
        os.system('git push')
    else :
        print('error: 切换工作目录失败！')


#创建目录结构
def mkdir(path):
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path) 
        # print (path + ' 创建成功')
        return True
    else:
        # print (path+' 目录已存在')
        return False



'''
kone read me:
1、此py脚本放在egret工程的根目录下，
2、指定好游戏发布的git目录 gitPath，该git目录要先自己个git clone好
3、开发完运行此脚本,则会自动打包，然后拷贝新包文件到gitPath并提交、推送上git
4、该git有其他人改过要自己手动去同步
'''

prjPath = os.getcwd()
binPath = prjPath + 'bin-release/web'
gitPathH5 = 'E:/work/git-fac/' + 'w7nt(diagram'

# egret 打包
dirName = egretPublish()
if dirName == '':
    os._exit(0)

# h5 版 拷贝新包（index.html除外）
coverFiles(os.path.join(binPath, dirName), gitPathH5) 

# 拷贝 index.html 并添加版本号   
copyIndexHtml(prjPath + 'index.html', gitPathH5)

# 拷贝 public/carry.js
mkdir(gitPathH5 + 'public')
shutil.copy(prjPath + '/public/carry.js', gitPathH5 + '/public')

# 拷贝 css/index.css 
mkdir(gitPathH5 + 'css')
shutil.copy(prjPath + '/css/index.css', gitPathH5 + '/css')

# 提交git
gitPusher(gitPathH5, dirName)

# end of python


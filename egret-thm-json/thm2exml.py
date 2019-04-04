import os
import codecs
import json

'''
功能：
还原egret打包生成的default.thm.json文件，转化为对应的.exml 布局文件

使用：
1、先将 default.thm.json 文件用记事本打开，用另存为改为 ANSI编码的
2、确认下 default.thm.json 的格式有没有问题，里面的 path 全局替换下，把前面不要的前缀去掉
3、双击运行我
'''

# 创建utf-8格式文件
# eg: createFile('skins/a.exml', '内容')
def createFile(fileUrl, cont):
	tmp = fileUrl.split('/')
	fileName = tmp[len(tmp)-1]
	filePath = fileUrl.replace(fileName, '')
	isExist = os.path.exists(filePath)
	if isExist == False:
		os.makedirs(filePath)
	file = codecs.open(fileUrl, 'w', 'utf-8')
	file.write(cont)
	file.close()


with open('default.thm.json', 'r') as file:
	data = json.load(file)
	exmls = data['exmls']
	for info in exmls:
		print('创建文件：' + info['path'])
		createFile('skins/' + info['path'], info['content'])




input("没报错就是成功了，回车吧！")
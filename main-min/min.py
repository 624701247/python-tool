import os
import codecs
import re

'''
功能：
egret打包出来的 main.min.js 还原成对应 ts文件。
起码自动创建对应的ts文件能省很多时间


使用：
0、每步操作前记得备份

1、拿到main.min.js 先手动删除一些没用的 & 全局替换一些代码。
	var t = e.call(this) || this;  替换成  super()
	t.prototype. 替换成 public 
	删除掉  return __extends(t, e),

	    }      这样的接口替换掉那个逗号，注意前面的缩进也要拷贝进查找
	    ,

2、看需不需要运行下函数editPublic

3、重点，最后运行下函数toTsFile

'''


#  public xxFunc = function() {   替换成   public xxFunc() {
def editPublic():
	content = ''
	with open('main.min.js', 'r', encoding='utf-8') as file:
		for line in file.readlines():
			if line.find('public ') > 0 and line.find(' = function') > 0:
				newLine = line.replace(' = function', '')
				print(newLine)
				content += newLine
			else:
				content += line

	outfile = open('main.min.js', "w+", encoding='utf-8')
	outfile.write(content) 
	outfile.close()


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


def toTsFile():
	content = 'namespace ns1 { \n\n'
	with open('main.min.js', 'r', encoding='utf-8') as file:
		for line in file.readlines():
			if line.find('reflect(') > 0:
				mmm = re.search('(").+(")', line)
				fileName = mmm.group()
				fileName = fileName.replace('"', '')
				fileName = fileName.replace('"', '')
				print(fileName)
				content += '\n}'
				createFile('ts/' + fileName + '.ts', content)
				content = 'namespace ns1 { \n\n'
			else:
				content += line
import os
import codecs
from PIL import Image  

'''
功能：
excel 转json(省市区数据表转成 sarea插件需要的格式)
就是 excel.js 那样格式的文件转化成json,

使用：
运行我，然后复制打印出来的东西就是你想要的json格式
'''


data = {}
def listName(path, id):
	curShen = ''
	curShi = ''
	curQu = ''
	count = 0
	with open(path,"r", encoding='utf-8') as file:
		for line in file.readlines():
			count = count + 1
			shen = line.split()[0]
			shi = line.split()[1]
			qu = line.split()[2]
			if curShen != shen :
				data[shen] = {'items':{}}
				curShen = shen
			if curShi != shi :
				data[shen]['items'][shi] = {'items':{}}
				curShi = shi
			if curQu != qu:
				data[shen]['items'][shi]['items'][qu] = count
				curQu = qu


srcDir = 'excel.js'

listName(srcDir, 0)
listName(srcDir, 1)
listName(srcDir, 2)
print(data)

input("Prease <enter>")

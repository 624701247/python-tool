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


def newItems():
	return {'items':{}}

def newItemArr():
	return {'items':[]}

data = {}
def listName(path):
	curShen = ''
	curShi = ''
	# curQu = ''
	count = 0
	with open(path,"r", encoding='utf-8') as file:
		for line in file.readlines():
			count = count + 1
			tmp = line.split()
			# print(str(len(tmp)) + '   ' + str(count))
			shen = tmp[0]
			shi = tmp[1]
			# qu = line.split()[2]
			stop = tmp[2]
			addr = tmp[3]
			if curShen != shen :
				data[shen] = newItems()
				curShen = shen
			if curShi != shi :
				data[shen]['items'][shi] = newItemArr()
				data[shen]['items'][shi]['items'].append({'stop':stop, 'addr':addr})
				curShi = shi
			# if curQu != qu:
			# 	data[shen]['items'][shi]['items'][qu] = newItemArr()
			# 	curQu = qu
			data[shen]['items'][shi]['items'].append({'stop':stop, 'addr':addr})


srcDir = 'excel-30new.js'

listName(srcDir)
# listName(srcDir, 1)
# listName(srcDir, 2)
print(data)

input("Prease <enter>")

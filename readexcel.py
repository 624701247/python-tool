import os
from PIL import Image  
import codecs

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


srcDir = 'E:\\work\\python-tool\\excel.js'

listName(srcDir, 0)
listName(srcDir, 1)
listName(srcDir, 2)
print(data)

input("Prease <enter>")

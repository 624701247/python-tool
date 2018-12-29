import re
import os
import time
import re
import codecs

#创建utf-8格式文件b并写入内容
def createFile(fileName, cont):
	isExist = os.path.exists(fileName)
	print(isExist)
	if isExist:
		destfile = open(fileName, "w+", encoding='utf-8')
		destfile.write(cont) 
	else:
		destfile = codecs.open(fileName, 'w', 'utf-8')
		destfile.write(cont)
		destfile.close()


def delSpace(line):
	return re.sub('(\n)$', '', line)


def delHttp(line):
	return re.sub('http.*?:', '', line)


keys = ['title', 'txt1', 'txt2', 'prize',  
'tips1', 'tips2', 'tips3', 'tips4', 'tips5']
endKeys = ['pcUrl', 'mobileUrl']

# 
def formatOnePiece(slist):
	sid = 0
	eid = 0
	content = ''
	for idx in range(0, len(slist)):  
		line = slist[idx]
		if sid == 0:
			line = "{\n    '" + keys[sid] + "': '" + delSpace(line) + "',\n"
			sid += 1
		elif line.find('http') != -1 and line.find('//') != -1:
			line = "	'" + endKeys[eid] + "': '" + delHttp( delSpace(line) ) + "',\n"
			eid += 1
		else:
			line = "	'" + keys[sid] + "': '" + delSpace(line) + "',\n"
			sid += 1
		# 最后一项
		if idx == len(slist) - 1:
			line = line.replace(',\n', '\n}')
		content += line
	# 
	return content


# 
def formatOnePack(packKey, plist):
	content = "'" + packKey + "': ["
	isFirst = True
	for idx in range(0, len(plist)):  
		if len(plist[idx]) == 0:
			continue
		elif isFirst:
			content += formatOnePiece(plist[idx])
			isFirst = False
		else:
			content += ',	' + formatOnePiece(plist[idx])
	content += ']'
	return content


# 给index.html 添加版本号
def getAreaData(srcPath, destPath):
	data = {}
	curName = ''
	curPieceId = -1
	isNewPiece = False
	with open(srcPath,"r", encoding='utf-8') as file:
		for line in file.readlines():
			# 
			if line.find('packName') != -1: #一块区域开头
				curName = re.search('".*?"', line).group()
				curName = curName.replace('"', '')
				curName = curName.replace('"', '')
				print('curName ' + curName)
				data[curName] = []
				curPieceId = 0
				isNewPiece = False
			elif curPieceId >= 0:
				if line == '\n':
					if isNewPiece == False:
						data[curName].append([])
						curPieceId = len(data[curName]) - 1
						isNewPiece = True
					else:
						continue
				else:
					data[curName][curPieceId].append( line )
					isNewPiece = False
	# 
	# print(data['kone'])
	content = 'var areaData = {\n'
	isFirst = True
	for key in data:
		if isFirst:
			content += formatOnePack(key, data[key])
			isFirst = False
		else:
			content += ',\n\n' + formatOnePack(key, data[key])
	# 
	content += '\n\n}'
	createFile(destPath, content)
	# destfile = open(destPath, "w+", encoding='utf-8')
	# destfile.write(content) 
	# destfile.close()


# 
getAreaData('copywriter.js', 'copywriter-out.js')
input('搞定了')



import os
from PIL import Image  
import codecs


#罗列指定路径下的所有图片
# @return content : 
def listImgName(path, perfix):
    content = ''
    if perfix == '':
        content += path + '\n\n'
        content += '['
    for fileName in os.listdir(path):
        curPath = os.path.join(path, fileName)
        if os.path.isfile(curPath) == True:
            if fileName.find('.') > 0:
                if fileName.find('.png') > 0 or fileName.find('.jpg') > 0:
                    ''' # kone point: 读取文件宽高
                    img = Image.open(os.path.join(path, fileName))
                    wid, hei = img.size  
                    '''
                    ''' # kone point: 修改文件名，大写全部转小写。
                    newname = fileName.lower()
                    os.rename(os.path.join(path,fileName), os.path.join(path,newname))
                    fileName = newname
                    ''' 
                    content += "'" + perfix + fileName + "', "
        elif os.path.isdir(curPath) == True:
            content += listImgName(curPath, perfix + fileName + '/')

    if perfix == '':
        content = content[0: len(content) - 2]
        content += ']'
        # kone point: 统计字符串中指定字符的数量
        content += '\n\n文件数量：' + str(content.count(','))
    return content



# kone todo
'''
功能：
遍历文件夹，获取文件信息，批量操作文件
'''

srcDir = 'E:\\wamp64\\www\\gihl(aeg-care\\image'

content = listImgName(srcDir, '')
f_utf8 = codecs.open("listdir-output.txt", 'w', 'utf-8')
f_utf8.write(content)
# f_utf8.write('\n')
f_utf8.close()

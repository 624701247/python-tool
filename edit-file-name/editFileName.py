import os
import codecs

# pip install PIL 是旧版本了，python3点多的换成：  pip install Pillow
from PIL import Image


# 批量修改文件名
# 并获取图片文件宽高
def fileNameLower(path):
    # f_utf8 = codecs.open("output.txt", 'w', 'utf-8')
    for fileName in os.listdir(path):
        if os.path.isfile(os.path.join(path, fileName)) == True:
            newname = fileName.lower()  
            os.rename(os.path.join(path,fileName), os.path.join(path,newname))  # kone point :  修改文件名
            if newname.find('.png') > 0 or newname.find('.jpg') > 0:
                img = Image.open(os.path.join(path,newname))   # kone point : 获取图片尺寸
                wid, hei = img.size
                print(newname + ' 宽高：' + str(wid) + '、' + str(hei))
                # f_utf8.write(".divimg('" + newname + "', " + str(wid/100) + "rem, " + str(hei/100) + "rem);")
                # f_utf8.write('\n')
    # f_utf8.close()


fileNameLower("files")
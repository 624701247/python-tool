import os
from PIL import Image  
import codecs


# 批量修改文件名，大写统一转小写
# 并获取图片文件宽高
def fileNameLower(path):
    f_utf8 = codecs.open("editFileName-output.txt", 'w', 'utf-8')
    for fileName in os.listdir(path):
        if os.path.isfile(os.path.join(path, fileName)) == True:
            if fileName.find('.') > 0:
                newname = fileName.lower()
                os.rename(os.path.join(path,fileName), os.path.join(path,newname))
                if newname.find('.png') > 0 or newname.find('.jpg') > 0:
                    img = Image.open(os.path.join(path,newname))  
                    wid, hei = img.size
                    f_utf8.write(".divimg('" + newname + "', " + str(wid/100) + "rem, " + str(hei/100) + "rem);")
                    f_utf8.write('\n')
    f_utf8.close()



fileNameLower("E:\\work\\python-tool\\editFileName-test")



''' 
运行：
python editFileName.py

输出： editFileName-output.txt
// 资源名，图片宽， 高
.divimg('../image/p1-wz.png', 2.61rem, 1.11rem);


'''
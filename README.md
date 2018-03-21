# python批处理
    
    
    
###### 所用框架、技术：
python 3.6.4

  
#### 内容
######## 1. python editFileName.py
	输出： editFileName-output.txt 
	(内容： divimg('../image/p1-wz.png', 2.61rem, 1.11rem); //写less用 )
	批量修改文件名，大写统一转小写,并获取图片文件宽高

######## 2. python ansi2utf8.py
	解决window下 sublime打开一些含中文的ANSI格式文件乱码的问题，
	window下 ANSI格式转化为 utf-8格式 


######## 3. python publish.py
	1、此py脚本放在egret工程的根目录下，
	2、指定好游戏发布的git目录 gitPath，该git目录要先自己个git clone好
	3、开发完运行此脚本,则会自动打包，然后拷贝新包文件到gitPath并提交、推送上git
	4、该git有其他人改过要自己手动去同步
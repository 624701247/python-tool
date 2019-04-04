# python批处理
### 肖进超 

* 当前使用：python 3.6.4
* 需要查什么知识点请搜索 kone point


##目录功能索引：
* copywriter ： 南航页面项目用，将指定排列文本转化为.json配置
 
* egret-thm-json ： 还原egret打包生成的default.thm.json文件，转化为对应的.exml 布局文件
 
* main-min ： egret打包出来的 main.min.js 还原成对应 ts文件。

* ansi2utf8.py : 解决window下 sublime打开一些含中文的ANSI格式文件乱码的问题

* edit-file-name ：批量修改文件名、获取图片文件宽高 

* read-excel ： excel 转json(省市区数据表转成 sarea插件需要的格式)
 
#### 批量修改文件名，大写统一转小写,并获取图片文件宽高  
###### python editFileName.py
	输出目录： editFileName-output.txt 
	(内容： divimg('../image/p1-wz.png', 2.61rem, 1.11rem); )


#### 解决window下 sublime打开一些含中文的ANSI格式文件乱码的问题，
###### python ansi2utf8.py	
	window下 ANSI格式转化为 utf-8格式

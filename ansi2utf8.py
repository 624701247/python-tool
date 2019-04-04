import codecs


#解决window下 sublime打开一些含中文的ANSI格式文件乱码的问题
# window下 ANSI格式转化为 utf-8格式 
def ansi2utf8(file_name):
    f_ansi = codecs.open(file_name, 'r', 'ansi')
    cont = f_ansi.read()
    f_ansi.close()
    f_utf8 = codecs.open(file_name, 'w', 'utf-8')
    f_utf8.write(cont)
    f_utf8.close()


ansi2utf8("testDoc.txt")
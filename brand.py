# -*- coding: utf-8 -*-


import os
import shutil
import codecs
import time

targetfile = open('brand-out.txt', "w+", encoding='utf-8')


with open('brand.txt',"r") as file:
    for line in file.readlines():
        # count = count + 1
        newl = ('"' + line + '",').replace("\n", "")
        targetfile.write(newl + '\n')
    targetfile.close()
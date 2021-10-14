# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os

def imageDecode(f,fn):
    dat_read = open(f, "rb")
    out = output_path + fn + ".png"
    png_write = open(out, "wb")
    for now in dat_read:
        for nowByte in now:
            newByte = nowByte ^ 0xB9 #修改为自己的解密码
            png_write.write(bytes([newByte]))
    dat_read.close()
    png_write.close()

def findFile(f):
    fsinfo = os.listdir(f)
    for fn in fsinfo:
        temp_path = os.path.join(f, fn)
        if not os.path.isdir(temp_path):
            print('文件路径: {}' .format(temp_path))
            imageDecode(temp_path,fn)
        else:
            ...

path = r'F:\dat图片' #建议把\替换为/，因为\有时候会被错误识别为转义符，无法找到正确的路径
output_path = r'F:\jpg' #要保证这个路径存在，建议新建一个文件夹命名为Decoded
findFile(path)
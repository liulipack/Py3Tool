# -*- coding: utf-8 -*-
import os, sys, random

# 定义填充大小和文件名
FillSize = 1 * 1024 * 1024 * 1024 # 1 GB
File = open(os.path.dirname(os.path.realpath(sys.argv[0])) + '\\test.txt', 'a')

# 生成随机内容
def rand(len):
    chars = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&')
    fill = ''
    for num in range(len):
        fill += random.choice(chars)
    return fill

# 开始填充
for index in range(int(FillSize / 10240)):
    File.write( rand(10240) )
    print("进度 - " + str(index + 1) + ' / ' + str(int(FillSize / 10240)))

# 关闭文件
File.close()
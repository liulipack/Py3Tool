# _*_ coding: utf-8 _*_
"""
Time:     2022/02/13 18:31:35
Author:   LiuliPack
Version:  V 0.1
Describe: 填盘。
"""

# 基础参数
import os, sys, random

FillSize = 1 * 1024 * 1024 * 1024 # 1 GB
File = open(os.path.dirname(os.path.realpath(sys.argv[0])) + '\\Rainbow\'s End.txt', 'a')

# 生成随机内容
def rand(len):
    chars = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`!@#$%^&*()_=+[]{};:"\|,.')
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
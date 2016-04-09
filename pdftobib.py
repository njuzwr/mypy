#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__ = 'njuzwr'
# 扫描该目录下的文件并将PDF文件添加到STK.bib数据库中
import os

s = os.sep
lsep = os.linesep
path = 'd:' + s + 'Research' + s + 'STK'
pdfs = []
bib = open(path + s + 'STK.bib', 'a', encoding='utf-8')
# 可以在打开文件中加入编码方式
i = 0
for rt, dirs, files in os.walk(path):
    # os.walk方法返回三元tuple
    for f in files:
        if f.endswith('pdf'):
            i += 1
            bib.writelines('@BOOK{STK%d,' % i + lsep)
            bib.writelines('title = {%s},' % f.split('.')[0] + lsep)	# 去掉文件名后缀
            # 文件名中最好不要有'.'，有'.'会出问题
            bib.writelines('file = {:'+rt.replace('\\', '\\'*2).replace(':', '\\:')+s+s+f+':PDF},' + lsep)
            # LaTex中\需要转义\\，在Jabref中也是如此
            # txt文件中会多出一个空行，还不知道是为什么
            bib.writelines('publisher = {internet},' + lsep)
            bib.writelines('author = {internet},' + lsep)
            bib.writelines('editor = {njuzwr},' + lsep)
            bib.writelines('year = {2016},' + lsep)
            bib.writelines('}' + lsep)

bib.close()

# 以下代码有问题，如何进行递归调用是一个问题
# 代码的初衷是想遍历该文件夹及其子文件夹中的pdf文件，但在子文件夹递归调用程序本身会有问题，如何传递合适的参数给函数是一问题

# path = 'D:/Research/STK/Temp1/'
#
# def findpdfs(p):
# 	res = []
# 	lists = os.listdir(p)
# 	for eachlist in lists:
# 		subpath = path + eachlist + '/'
# 		if eachlist.endswith('pdf'):
# 			res.append(eachlist)
# 			continue
# 		if os.path.isdir(subpath):
# 			findpdfs(subpath)
# 			continue
# 	return res
#
# pdfs = findpdfs(path)
# print(pdfs)
# print(len(pdfs))

#!/usr/bin/python
#coding:utf-8
import os, shutil,sys


if len(sys.argv) < 4:
    print 'usage: python copyFilesOut.py [src path] [dst path] [number of file to copy]'
    sys.exit()

src = sys.argv[1]
dest = sys.argv[2]
num = int(sys.argv[3])

filenames = os.listdir(src)
filenames.sort()

for i in range(num):
    shutil.copy(os.path.join(src, filenames[i]), dest)



#!/usr/bin/python
# search the files in the directory or its subdirectory, whose names contain a certain key word

import os 
import sys

def search(path, word):
    for filename in os.listdir(path):
        fp = os.path.join(path, filename)
        if os.path.isfile(fp) and word.upper() in filename.upper():
            print fp
        elif os.path.isdir(fp):
            search(fp, word)

search(sys.argv[1], sys.argv[2])

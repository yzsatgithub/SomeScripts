#!/usr/bin/python
# search whether certain key words exist in the content of files inside the directory
import os
import sys

def search(path, word):
    for filename in os.listdir(path):
        fp = os.path.join(path, filename)
        if os.path.isfile(fp):
            with open(fp) as f:
                for line in f:
                    if word.upper() in line.upper():
                        print fp
                        break
        elif os.path.isdir(fp):
            search(fp, word)

search(sys.argv[1], sys.argv[2])


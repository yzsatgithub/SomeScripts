import sys

originfile = sys.argv[1]
newfile = sys.argv[2]

assert originfile != ""
assert newfile != ""

listf = open(originfile, 'r')
lines = listf.readlines()

newlines = []
for line in lines:
    words = line.split('/')[-1]
    #words = ['.',words]
    #line = '/'.join(words)
    newlines.append(words)

newf = open(newfile, 'w')
newf.writelines(newlines)
newf.close()

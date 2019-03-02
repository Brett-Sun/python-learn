import os, sys, glob
dirname = r'c:/Python37/Lib' if len(sys.argv) == 1 else sys.argv[1]

allsizes = []
allpy = glob.glob(dirname + os.sep + "*.py")
for filename in allpy:
    filesize = os.path.getsize(filename)
    allsizes.append((filesize, filename))

allsizes.sort()

import pprint
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])
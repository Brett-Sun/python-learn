import os, sys, pprint
dirname = r'c:\Python37\Lib' if len(sys.argv) == 1 else sys.argv[1]

allsizes = []
for (thisDir, subsHere, filesHere) in os.walk(dirname):
    # print(thisDir)
    for filename in filesHere:
        if filename.endswith('.py'):
            # print('...', filename)
            fullname = os.path.join(thisDir, filename)
            filesize = os.path.getsize(fullname)
            allsizes.append((filesize, fullname))

allsizes.sort()

pprint.pprint(allsizes[:1])
pprint.pprint(allsizes[-1:])
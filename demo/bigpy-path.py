import os, sys, pprint

py3 = sys.version_info[0] > 2

logfile = False

trace = 1 # 0代表关闭；1代表目录；2代表文件；3代表所有

allsizes = []
for srcdir in sys.path:
    if trace == 1 or trace == 3:
        if logfile:
            open('result.tmp', 'a').writelines("Searched path root: %s\n" % srcdir)
        else:
            print("Searched path root: ", srcdir)
    
    for (thisDir, subsHere, filesHere) in os.walk(srcdir):
        if trace == 1 or trace == 3:
            if logfile:
                open('result.tmp', 'a').writelines('... %s\n' % thisDir)
            else:
                print('...', thisDir)
        for filename in filesHere:
            if filename.endswith('.py'):
                if trace == 2 or trace == 3:
                    if logfile:
                        open('result.tmp', 'a').writelines('...... %s\n' % filename)
                    else:
                        print('......', filename)
                fullname = os.path.join(thisDir, filename)
                filesize = os.path.getsize(fullname)
                allsizes.append((filesize, fullname))

    allsizes.sort()
    pprint.pprint(allsizes[:1])
    pprint.pprint(allsizes[-1:])
    allsizes.clear()

    # if py3:
    #     input("Please input Enter key to continue to display the info ...")
    # else:
    #     raw_input("Please input Enter key to continue to display the info ...")
    if not logfile:
        input("Please input Enter key to continue to display the info ...")

# pprint.pprint(sys.path)
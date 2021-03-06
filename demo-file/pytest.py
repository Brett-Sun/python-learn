print("===============Python File Access: open===============")

# print("teddt")
data = "sp\xe4m"
print(data)
print(0xe4, bin(0xe4), chr(0xe4))
print(data.encode('latin1'))
print(data.encode('utf8'))
# print(data.encode('ascii'))

import sys
print(sys.getdefaultencoding())

print(open(r'demo-file\data.txt', 'w', encoding='latin1').write(data))
print(open(r'demo-file\data.txt', 'r', encoding='latin1').read())
print(open(r'demo-file\data.txt', 'r').read())
print(open(r'demo-file\data.txt', 'rb').read())


data = b"a\0b\rc\r\nd"
print(data)
print(open(r'demo-file\data.bin', 'w').write(data.decode()))
print(open(r'demo-file\data.bin', 'r').read())

print(open(r'demo-file\tmp.txt', 'r').read())
print(open(r'demo-file\tmp.txt', 'rb').read())
print(open(r'demo-file\tmp.txt', 'r', encoding='gb2312').read())


print("===============Python File Access: struct===============")


import struct
data = struct.pack('>i4shf', 2, b'spam', 3, 1.234)
print(data)
open(r"demo-file\data-1.bin", 'wb').write(data)

inputData = open(r'demo-file\data-1.bin', 'rb').read()
print(inputData)
print(struct.unpack('>i4shf', inputData))


print("===============Python Directory Access: glob===============")

import os
print(os.popen('dir /B').readlines())
print(os.popen('dir *.txt /B').readlines())

import glob
print(glob.glob('*'))
print(glob.glob('.git/*'))

print(os.listdir(os.curdir))
print(os.listdir('.git'))

for (thisdir, subshere, fileshere) in os.walk(os.curdir):
    print(thisdir + '==========')
    for fname in fileshere:
        path = os.path.join(thisdir, fname)
        print(path)

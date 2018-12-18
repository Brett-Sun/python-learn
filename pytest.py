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

print(open('data.txt', 'w', encoding='latin1').write(data))
print(open('data.txt', 'r', encoding='latin1').read())
print(open('data.txt', 'r').read())
print(open('data.txt', 'rb').read())


data = b"a\0b\rc\r\nd"
print(data)
print(open('data.bin', 'w').write(data.decode()))
print(open('data.bin', 'r').read())

print(open('tmp.txt', 'r').read())
print(open('tmp.txt', 'rb').read())
print(open('tmp.txt', 'r', encoding='gb2312').read())


print("===============Python File Access: struct===============")


import struct
data = struct.pack('>i4shf', 2, b'spam', 3, 1.234)
print(data)
open("data-1.bin", 'wb').write(data)

inputData = open('data-1.bin', 'rb').read()
print(inputData)
print(struct.unpack('>i4shf', inputData))


print("===============Python Directory Access: ===============")



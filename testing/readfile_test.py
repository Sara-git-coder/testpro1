"""
不同的编程语言读写文件的操作步骤大体都是一样的，分为以下几个步骤：
1、打开文件，获取文件描述符号
2、操作文件描述符号（读或写）
3、关闭文件
"""

f = open('testdata/test.txt')
# print (f.read ())
print (f.readlines())
f.close()

with open('testdata/test.txt') as f:
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break
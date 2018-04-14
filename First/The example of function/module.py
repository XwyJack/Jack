import math
import sys

import support

print('命令行参数如下:')
for i in sys.argv:
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')

print()
print(sys.path)

print()
support.prin_func('wanyi')

print()
print(dir())

# 1 output
print()
print('{}Website:"{}!"'.format('Cainiao', 'www.runoob.com'))

# 2
print('{0},{1}'.format('Google', 'runoob'))
print('{0},{1}'.format('Runoob', 'Google'))
# 3
print('{name}Website:{wangzhi}'.format(name='Cainiao', wangzhi='www.runoob.com'))

# 4
print('Site list:{0},{1},{other}'.format('Google', 'Baidu', other='Runoob'))

print('{!a}'.format(math.pi))
print('{!s}'.format(math.pi))
print('{!r}'.format(math.pi))
print('{0:.3f}'.format(math.pi))

print('%20.3f' % math.pi)
print('{0:10.3f},{1:10}'.format(math.pi, 12))
a = 3
print('b={0:10d}'.format(a))

print()
f = open('/home/macbookpro/a.txt', 'w+')
num=f.write("Python is a good language\nYes it is\n")
print(num)

# f=open('/home/macbookpro/a.txt', 'w+')
# str=f.read()
# print(str)
# f.close()

# f = open('/home/macbookpro/a.txt', 'w+')
# str1 = f.readline()
# print(str1)
# str1 = f.readline()
# print(str1)

# f = open('/home/macbookpro/a.txt', 'w+')
# str2=f.readlines()
# print(str2)

f = open('/home/macbookpro/a.txt', 'w+')
for line in f:
    print(line,end='')

f.close()

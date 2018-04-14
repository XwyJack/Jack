# 3月15日



import os

# class findFile(object):
#     relativePath = ''
#
#     def __init__(self, fileName):
#         self.fileName = fileName
#
#     def showPath(self, path='.'):
#         self.relativePath = self.relativePath + path + '/'
#         dirs = os.listdir(self.relativePath)
#         for dir in dirs:
#             if os.path.isdir(self.relativePath + dir):
#                 if dir != '__pycache__':
#                     self.showPath(dir)
#             else:
#                 if dir.find(self.fileName) >= 0:
#                     print(self.relativePath + dir)
#         self.relativePath = ''
#
#
# f = findFile('/home/macbookpro/PycharmProjects/First/IOFunction.py')
# print([f.showPath('/home/macbookpro/PycharmProjects/First/')])

# 上面的例子不能正确运行


# 3月21日
import pickle

d = dict(name='Jack', age=20, score=90)

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)  # 此函数反序列化出文件中的内容
f.close()
print(d)

# pickle模块用来实现序列化



# JSON,还没看



# _*_ coding : utf-8 _*_
# @Time : 2025/2/13 13:28
# @Author : 田园
# @File : 47-Python_文件的打开和关闭
# @Project : readme.md

# 创建一个test.txt文件
# 访问模式：w  可写
#         r  可读
# 事先未创建文件的情况下，写了访问路径，会为其创建一个新文件
# open('test.txt','w')

# 打开文件
# 创建变量file，用来接收调用open函数后的返回值
# file=open('test.txt','w')

# 给file文件，也就是test.txt文件里写点内容
# file.write('hello world')

# 不可调用open创建文件夹，目前只能手动创建新文件夹，才可调用open函数，在demo文件夹下创建新文件
file=open('demo/test.txt','w')
# 可以在指定的文件夹中创建新文件，并向其中添加新内容
file.write('good morning world')

# 文件的关闭，为避免CPU过载，也要记得关闭一些用完的文件
file2=open('file.txt','w')
file2.write('good night world')
# 虽然关闭后看似没什么大区别，但内存会被吃掉，所以在底层还是关闭了的
file2.close()



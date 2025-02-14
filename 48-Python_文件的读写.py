# _*_ coding : utf-8 _*_
# @Time : 2025/2/13 19:23
# @Author : 田园
# @File : 48-Python_文件的读写
# @Project : readme.md

# 写数据
# file=open('file_write_test.py','w')
# 调用write方法，在py文件中写入如下内容
# file.write('hello world, i am here.\n'*5)
# file.close()

# 若再次运行这段代码，会打印10次还是依旧是5次？答：5次
# 解析：因为文件的访问方式是w，意思就是，若该文件存在，则会先把原来的数据清空再写入新数据，也就是新内容会将旧内容覆盖掉；但若文件不存在，才是创建新文件并写入内容，因此依旧是5次，
# 但若想要追加内容，访问方式就用a，那新内容就会被追加在旧内容之后，访问方式是a的话，会是打印10次
# file=open('file_write_test.py','a')
# file.write('hello world, i am here\n'*5)
# file.close()

# 读数据
file=open('file_write_test.py','r')
# 调用read方法来读取py文件中的内容
# 默认情况系，read方法是一字节一字节地读，效率较低，
# content=file.read()
# print(content)
# content.close()

# 想要提高读取的效率，可以调用readline方法，但也只能读取一行
# content=file.readline()
# print(content)

# readlines方法用于多行读取，会将所有的数据都读取到，并且以一个列表的形式返回
# 而列表中的元素，就是一行一行的数据
content=file.readlines()
print(content)

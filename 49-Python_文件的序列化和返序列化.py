# _*_ coding : utf-8 _*_
# @Time : 2025/2/14 18:09
# @Author : 田园
# @File : 49-Python_文件的序列化和返序列化
# @Project : readme.md
from marshal import dumps

# file=open('test2.txt','w')
# 默认情况下，只能将字符串写入到文件中
# file.write('hello,world')
# file.close()

# file=open('test2.txt','w')
# 默认情况下，对象类型的数据无法写入到文件中，若想要写入到文件中，就必须进行序列化操作
# nameList=['Osborn','Evan']
# file.write(nameList)

# 序列化方法一：
# dumps()
# 先创建一个文件
# file2=open('test2.txt','w')
# # 定义一个列表
# nameList=['Osborn','Evan','Sariel','Charlie','Jesse']
# # json并不是Python提供，能直接提供程序员使用的，要使用的话，首先要导入json模块到该文件当中
# import json
# # 序列化，调用dumps方法，将python对象转换为json字符串
# # 在使用scrapy框架时，该框架会返回一个对象，需要做的就是讲对象写入到文件中，此时就可以调用json.dumps方法
# name=json.dumps(nameList)
# print(name)
# # 可以看到调用dumps方法转换后的结果是字符串类型的数据
# print(type(name))   #<class 'str'>
# # 将转换后的数据写入到文件中
# file2.write(name)
# # 记得关闭文件，以免内存泄漏
# file2.close()

# 序列化方法二：
# dump()
# 在将对象转换为字符串的同时，指定一个文件的对象，然后把转换后的字符串写入到该文件中
# 创建一个文件
# file3=open('test3.txt','w')
# nameList=['Luke','Artem','Richard','Marius']
# # 导入json
# import json
# # 调用dump方法，第一个参数为想要转换为字符串的数据，第二个参数就是想要将输入写入进去的那个指定的文件的变量名
# # 这一步骤就相当于dumps的name=json.dumps(nameList)和file2.write(name)这两步操作，dump给简化了，一步到位
# names=json.dump(nameList,file3)
# file3.close()

# 反序列化，就是将json字符串类型的数据变成对象类型的数据/python对象
file4=open('test3.txt','r')
# 读取文件中的数据
# content=file4.read()
# print(content)      #["Luke", "Artem", "Richard", "Marius"]
# # 转换前，读取到的数据是字符串类型的数据
# print(type(content))    #<class 'str'>

# 反序列化方法一：
# loads()
# 依旧先导入json
# import json
# # 调用loads方法，将json字符串转换为python对象
# loaded=json.loads(content)
# print(loaded)   #['Luke', 'Artem', 'Richard', 'Marius']
# # 转换后，json字符串类型的数据已变为python的list类型
# print(type(loaded))     #<class 'list'>
# file4.close()

# 反序列化方法二：
# load()
# 导入json
import json
# 调用loaded方法，一步到位将json字符串转换为python对象
loaded=json.load(file4)
print(loaded)       #['Luke', 'Artem', 'Richard', 'Marius']
print(type(loaded)) #<class 'list'>
# file4.close()
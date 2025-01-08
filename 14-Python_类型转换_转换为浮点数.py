# _*_ coding : utf-8 _*_
# @Time : 2025/1/8 13:04
# @Author : 田园
# @File : 14-Python_类型转换_转换为浮点数
# @Project : learn_PYTHON基础

# 当程序员在爬虫时，大部分情况下获取的都是字符串类型的数据，但因无法直接对其进行操作，因此需要将其转换成float。
# string --> float
a='12.47'
print(type(a))  #<class 'str'>
print(float(a)) #12.47
print(type(float(a)))   #<class 'float'>

# int --> float
b=947
print(type(b))  #<class 'int'>
print(float(b)) #947.0
print(type(float(b)))   #<class 'float'>

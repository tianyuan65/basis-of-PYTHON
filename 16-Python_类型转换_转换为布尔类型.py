# _*_ coding : utf-8 _*_
# @Time : 2025/1/8 18:30
# @Author : 田园
# @File : 16-Python_类型转换_转换为布尔类型
# @Project : learn_PYTHON基础

# int --> boolean
# 如果对非零的整型进行bool类型的转换，那么全是True，甚至负数也是True
a=1
print(type(a))  #<class 'int'>
print(bool(a))  #True
print(type(bool(a)))    #<class 'bool'>

b=2
print(bool(b))  #True
print(type(bool(b)))    #<class 'bool'>

c=-1
print(bool(c))  #True
print(type(bool(c)))    #<class 'bool'>

d=0
print(bool(d))  #False
print(type(bool(d)))    #<class 'bool'>

# float --> boolean
e=1.5
print(type(e))  #<class 'float'>
print(bool(e))  #True
print((type(bool(e))))  #<class 'bool'>

f=-2.5
print(type(f))  #<class 'float'>
print(bool(f))  #True
print((type(bool(f))))  #<class 'bool'>

# string --> boolean
# 只要字符串中有内容，在强制类型转换为bool类型是，就会返回True，也就是非空即是True。值得注意的是，无论是单双引号不影响前面那句话。
g='戏文说，相逢难逃别离'
print(type(g))  #<class 'str'>
print(bool(g))  #True
print(type(bool(g)))    #<class 'bool'>

# 就算是空格转换结果也是True
h=' '
print(type(h))  #<class 'str'>
print(bool(h))  #True
print(type(bool(h)))    #<class 'bool'>

i=''
print(type(i))      #<class 'str'>
print(bool(i))  #False
print(type(bool(i)))    #<class 'bool'>

# list --> boolean
# 只要列表中有数据，强制类型转换为bool类型时，返回的结果就是True。
j=['谷江山','于适','李昀锐','颜安']
print(type(j))  #<class 'list'>
print(bool(j))  #True
print(type(bool(j)))    #<class 'bool'>

# 若列表中没有任何数据，强制类型转换结果为False
j1=[]
print(type(j1))  #<class 'list'>
print(bool(j1))  #False
print(type(bool(j1)))    #<class 'bool'>

# tuple --> boolean
# 只要元组中有数据，在强制类型转换为bool类型时，就会返回True；
k=('萧逸','陆沉','齐司礼','查理苏','夏鸣星')
print(type(k))  #<class 'tuple'>
print(bool(k))  #True
print(type(bool(k)))    #<class 'bool'>

# 但若元组中没有数据，就会返回False。
k1=()
print(type(k1))  #<class 'tuple'>
print(bool(k1))  #False
print(type(bool(k1)))    #<class 'bool'>

# dictionary --> bool
# 只要字典中有数据，在强制类型转换为bool类型时，返回结果就是True；
l={'name':'夏彦','age':'24'}
print(type(l))  #<class 'dict'>
print(bool(l))  #True
print(type(bool(l)))    #<class 'bool'>

# 否则，返回False。
l1={}
print(type(l1))  #<class 'dict'>
print(bool(l1))  #False
print(type(bool(l1)))    #<class 'bool'>



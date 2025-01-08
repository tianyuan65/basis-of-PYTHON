# _*_ coding : utf-8 _*_
# @Time : 2025/1/8 15:21
# @Author : 田园
# @File : 15-Python_类型转换_转换为字符串
# @Project : learn_PYTHON基础

# 大部分的应用场景就是整型转换为字符串
# int --> string
a=83
print(type(a))  #<class 'int'>
# 强制类型转换为字符串的方法是str()
# print(string(a))    #会报错，且报错原因还是string没有声明，并且让你引入'string'
print(str(a))   #83，虽然没有引号，但已成功转换为string类型，只是Pycharm在显示时给优化了。
print(type(str(a))) #<class 'str'>

# float --> string
b=3.333
print(type(b))  #<class 'float'>
print(str(b))   #3.333
print(type(str(b))) #<class 'str'>

# boolean --> string
c=True
print(type(c))  #<class 'bool'>
print(str(c))   #True
print(type(str(c))) #<class 'str'>
d=False
print(type(d))  #<class 'bool'>
print(str(d))   #False
print(type(str(d))) #<class 'str'>


# _*_ coding : utf-8 _*_
# @Time : 2025/1/5 10:57
# @Author : 田园
# @File : 13-Python_类型转换
# @Project : learn_PYTHON基础

# 类型转换，强制类型转换为谁，就用什么方法
# string --> int
a='123'
print(type(a))  #<class 'str'>
# 将字符串转换为整型，并打印出来
print(int(a))   #123
# 查看将字符串转换为整型后，当前变量a的数据类型
print(type(int(a))) #<class 'int'>

# float --> int
b=1.73
print(type(b))  #<class 'float'>
# 若将float转换为int，其结果不是四舍五入，而是只截取小数点前的那个数字
# 将浮点数转换为整型，并打印出来
print(int(b))   #1
# 查看将浮点数转换为整型后，变量b的数据类型
print(type(int(b))) #<class 'int'>

# boolean  --> int
c=True
d=False
print(type(c))  #<class 'bool'>
print(type(d))  #<class 'bool'>
# 将boolean转换为int，输出结果为True转换结果是1；False是0
print(int(c))   #1
print(int(d))   #0
print(type(int(c))) #<class 'int'>
print(type(int(d))) #<class 'int'>

# string --> int
e='1.43'
print(type(e))  #<class 'str'>
# 字符串无法转换为整型的原因一：若字符串中的数字是小数，则无法转换为整型
# print(int(e))   #会报错
f='45ua'
print(type(f))  #<class 'str'>
# 字符串无法转换为整型的原因二：若字符串中有字母，也无法转换为整型
# print(int(f))   #会报错




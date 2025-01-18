# _*_ coding : utf-8 _*_
# @Time : 2025/1/15 14:14
# @Author : 田园
# @File : 20-Python_比较运算符
# @Project : learn_PYTHON基础

# 比较运算符，返回的都是布尔类型的数据
# ==    是判断==两边的变量是否一致
a=10
b=20
print(a==b) #False

# !=    是判断!=两边的变量是否不一致
print(a!=b) #True
# print(a<>b)
# 扩展：<> Python2使用的是这个，Python3中已不再使用它来表示不等式，若坚持使用会报Python3.13不再支持该种写法的错。

# >     判断>左边的变量是否大于右边的变量
print(a>b)  #False

# >=    判断>=左边的变量是否大于或等于右边的变量
print(10>=2)    #True
print(2>=2)     #True
print(2>=8)     #False

# <     判断<左边的变量是否小于右边的变量
print(10<9)     #False
print(1<2)      #True

# <=    判断<=左边的变量是否小于或等于右边的变量
print(10<=9)     #False
print(2<=2)      #True

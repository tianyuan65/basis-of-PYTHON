# _*_ coding : utf-8 _*_
# @Time : 2025/1/11 15:22
# @Author : 田园
# @File : 17-Python_算术运算符
# @Project : learn_PYTHON基础

a=5
b=2

# + 加
# print(a+b)  #7

# - 减
# print(a-b)  #3

# * 乘
# print(a*b)  #10

# / 除
# print(a/b)  #2.5

# // 取整除，就是取整数部分，它的结果有且只有一种就是int类型
# print(a // b)   #2

# % 取余，就是整除后剩下来的那个
# print(a%b)  #1

# ** 指数，就是a的b次幂
# print(a**b) #25

# () 小括号，提高运算优先级
# print(a*(a+b))  #35

# 扩展
# 可以用 +(加法) 进行两个字符串的拼接
# c='姻缘断情难续，殷勤多是假意，'
# d='人心道不明。'
# print(c+d)

# 在Python中，加号两端都是字符串才可以进行加法运算来实现拼接，也就是说，建议加法两端为同一类型的数据。但若硬要用下面这两个，建议把d先强制转换为string类型。
c='123'
d=456
# print(c+d)
# 强制转换为string类型，就可以进行拼接了。
print(c+str(d)) #123456

# 字符串的乘法是将字符串重复N次
a='初听只当戏，再听已懂曲中意。'
print(a*3)  #初听只当戏，再听已懂曲中意。初听只当戏，再听已懂曲中意。初听只当戏，再听已懂曲中意。
# _*_ coding : utf-8 _*_
# @Time : 2025/2/2 15:02
# @Author : 田园
# @File : 37-Python_切片
# @Project : 26-Python_流程控制语句_if案例练习.py

# 字符串切片
s='Hello World'
print(s)        #Hello World

# 直接写一个下标，就是查找/访问并输出对应的字符
# print(s[4])     #o

# [index1:index2]，遵循左闭右开的区间，输出在该区间内所有的字符
print(s[0:4])       #Hell

# [index:]，只写了起始值，没有写结束值，代表从起始值开始一直到末尾
print(s[1:])        #ello World

# [:index]，没写起始值，只写结束值，代表从下标为0的元素开始到结束位前一个为止
print(s[:5])        #Hello

# [index1:index2:step length]。起始值、结束值、步长俱全，但要是不写的话默认步长就是1，但写了就不同了
# 输出从下标为0的字符开始算起，到下标为8的前面的字符为止，间隔两个字符
print(s[0:8:2])     #HloW

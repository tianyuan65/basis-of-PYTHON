# _*_ coding : utf-8 _*_
# @Time : 2025/2/12 13:32
# @Author : 田园
# @File : 45-Python_函数的返回值
# @Project : readme.md

# 返回值的关键字是return，存在函数中
# def buyIceCream():
#     return '雪糕'
# 光在函数体内返回了返回值，并调用了是无法得到想要的结果的，
# buyIceCream()
# 需要用一个变量接收其结果，再输出才可
# dessert=buyIceCream()
# print(dessert)     #雪糕

# 案例：定义一个函数，让函数计算两个数值，并返回计算后的结果
def sum(a,b):
    return a+b

sum=sum(166,512)
print(sum)      #678

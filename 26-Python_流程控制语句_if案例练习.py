# _*_ coding : utf-8 _*_
# @Time : 2025/1/22 10:03
# @Author : 田园
# @File : 26-Python_流程控制语句if案例练习
# @Project : learn_PYTHON基础

# 在控制台输入一个年龄，如果年龄大于18，就打印可以去网吧了

# 这个age就是稍后我在控制台输入的数字，但input返回的是string类型，
age=input('请输入您的年龄')

# 由于age的类型为string类型，所以在下面的if语句中会报int与str无法进行比较的错。
# print(type(age))    #<class 'str'>

# 很显然，string和int无法进行比较，所以要把age强制类型转换为int类型。
if int(age)>18:
    print('成年了，可以去网吧了')

# 案例中考察的知识点
# 1. 控制台输入
# 2. 强制类型转换
# 3. int与string不能直接进行比较

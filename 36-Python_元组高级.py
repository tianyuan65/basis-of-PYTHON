# _*_ coding : utf-8 _*_
# @Time : 2025/2/1 20:25
# @Author : 田园
# @File : 36-Python_元组高级
# @Project : 26-Python_流程控制语句_if案例练习.py

foodTuple=('火锅','麻辣烫','酸菜炖猪肉','牛肉面')
# 尝试查
print(foodTuple[1])     #麻辣烫
print(foodTuple[3])     #牛肉面

# 尝试增
# 加在最后
# foodTuple.append('炒米粉')
# print(foodTuple)
# 指定下标增加
# foodTuple.insert(1,'羊肉串')
# print(foodTuple)
# 合并
# foodTuple2=('锅包肉','过桥米线')
# foodTuple.extend(foodTuple2)
# print(foodTuple)

# 尝试删
# 根据下标删除
# del foodTuple[2]
# print(foodTuple)
# pop()，删除最后一个
# foodTuple.pop()
# print(foodTuple)
# remove()，将元素值作为参数传进去
# foodTuple.remove('牛肉面')
# print(foodTuple)

# 尝试改，肯定是失败的，因为元组的元素值只可读不可改
# foodTuple[2]='小面'
# print(foodTuple)

# 定义只有一个元素的元组，就必须在唯一的元素后加一个逗号，
catTuple=('修喵咪~~~~')
# 不加逗号就会把括号识别成运算符号，因此在这里举的例子输出的是str类型
print(type(catTuple))     #<class 'str'>
puppyTuple=('修勾',)
# 只有加了逗号才会被识别为元组
print(type(puppyTuple))       #<class 'tuple'>


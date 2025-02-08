# _*_ coding : utf-8 _*_
# @Time : 2025/2/2 21:57
# @Author : 田园
# @File : 38-Python_字典高级_查(查询)
# @Project : 26-Python_流程控制语句_if案例练习.py

manMsg={'name':'Osborn','age':'24'}
print(manMsg)   #{'name': 'Osborn', 'age': '24'}
# 查询方式一：
# 查询字典中指定的键对应的值，格式：字典变量名['key的值']，格式这么复杂的原因是当初设定时键的类型被我写成了字符串类型，若写成数字，那就可以不加引号
print(manMsg['name'])   #Osborn
print(manMsg['age'])    #24

# 使用中括号，获取字典中不存在的key值时，会报该键值对不存在的错KeyError
# print(manMsg['gender'])

# 不可以用字典变量名.key值的方式来获取value的值，下面显示属性错误，dict里没有叫name的属性名
# print(manMsg.name)

#查询方式二：
# 调用字典的get方法，并将key值作为参数
print(manMsg.get('name'))   #Osborn
# 调用get方法来尝试获取dict中不存在的key时，会出现与第一个方法不同的结果，不会报错，只是输出None，表示该键值对不存在与dict中。
print(manMsg.get('gender')) #None


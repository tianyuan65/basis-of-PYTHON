# _*_ coding : utf-8 _*_
# @Time : 2024/12/30 13:20
# @Author : 田园
# @File : 10-Python_数据类型(List、Tuple、Dictionary)
# @Project : learn_PYTHON基础

# List  列表

# Tuple 元组

# Dictionary 字典

# List  列表(相当于前端里的数组，可读也可改)
# 应用场景：当获取到了很多数据的时候，可以将它们存储到列表中，并直接使用到列表访问。
name_list=['于适','谷江山']
# name_list[0]='颜安'
print(name_list)  #['于适', '谷江山']

# Tuple 元组(介于JS的数组和对象之间，但tuple只读，不能增删改里面的元素)
age_tuple=(71,75,28,18)
print(age_tuple)  #(71, 75, 28, 18)

# Dictionary 字典(相当于前端里的对象，里面可以有很多键值对)
# 应用场景：scrapy框架使用
# 格式：变量名={key:value,key1:value1}
person={'name':'孟子义','age':29,}
print(person) #{'name': '孟子义', 'age': 29}
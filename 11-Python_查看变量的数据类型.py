# _*_ coding : utf-8 _*_
# @Time : 2025/1/4 11:13
# @Author : 田园
# @File : 11-Python_查看变量的数据类型
# @Project : learn_PYTHON基础

# review
#     int
#     float
#     boolean
#     string
#     list
#     tuple
#     dictionary
# 用type方法来判断变量的数据类型，格式是type(变量名)

a=1 #int
print(a)    #1
print(type(a))  #<class 'int'>
b=1.2222
print(b)    #1.2222
print(type(b))  #<class 'float'>
c=True
print(c)    #True
print(type(c))  #<class 'bool'>
d='天打雷劈的一对儿'
print(d)    #天打雷劈的一对儿
print(type(d))  #<class 'str'>
e=[5,'整容计划就是斩首',False]
print(e)    #[5, '整容计划就是斩首', False]
print(type(e))  #<class 'list'>
f=(26,97.4,'如何呢？')
print(f)    #(26, 97.4, '如何呢？')
print(type(f))  #<class 'tuple'>
g={'name':'颜安','gender':'male','job':'actor'}
print(g)    #{'name': '颜安', 'gender': 'male', 'job': 'actor'}
print(g['name'])    #颜安
print(type(g))  #<class 'dict'>





# _*_ coding : utf-8 _*_
# @Time : 2025/2/8 12:20
# @Author : 田园
# @File : 39-Python_字典高级_改(修改)
# @Project : readme.md

manMsg={'name':'Osborn','age':'24'}
# 输出修改前的字典
print(manMsg)       #{'name': 'Osborn', 'age': '24'}

# 修改name的值为萧老大
# 方法：在[]中输入想要修改的key值，并赋值其对应的value值，且修改不像是查询，不可以调用get方法来进行
# manMsg['name']='萧老大'
# print(manMsg)       #{'name': '萧老大', 'age': '24'}

# 或者是调用__setitem__方法，第一个参数传要修改的key值，第二个参数传value值
manMsg.__setitem__('name','萧逸')
print(manMsg)       #{'name': '萧逸', 'age': '24'}


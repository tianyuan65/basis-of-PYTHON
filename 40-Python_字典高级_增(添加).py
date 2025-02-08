# _*_ coding : utf-8 _*_
# @Time : 2025/2/8 13:30
# @Author : 田园
# @File : 40-Python_字典高级_增(增加)
# @Project : readme.md

manMsg={'name':'Evan','age':'26'}
print(manMsg)       #{'name': 'Evan', 'age': '26'}

# 增加一个新键值对，key值为gender，其对应的value值为male
# key就是这样，[]中写入的key值，若存在于元素/字典中，则根据具体做法，会对其进行获取或修改的操作，但若不存在，又被赋了值，就进行新增元素的操作。
# 方法一：dicName['key']='value'，[]中写key值，等号后面写value值
manMsg['gender']='male'     #这是进行新增元素的操作
print(manMsg)       #{'name': 'Evan', 'age': '26', 'gender': 'male'}

# 这就是key值存在于字典中的情况，该情况下，就会变成修改元素的操作。
manMsg['name']='陆沉'         #这就是修改元素值的操作，做个复习
print(manMsg)       #{'name': '陆沉', 'age': '26', 'gender': 'male'}

# _*_ coding : utf-8 _*_
# @Time : 2025/2/8 14:29
# @Author : 田园
# @File : 41-Python_字典高级_删(删除)
# @Project : readme.md

manMsg={'name':'Charlie','age':28,'gender':'male','job':'doctor','marital status':'engaged'}
print(manMsg)   #{'name': 'Charlie', 'age': '28', 'gender': 'male', 'job': 'doctor', 'marital status': 'engaged'}

# 方法一：del，
#   删除字典中指定的某一个元素；
# del manMsg['age']
# print(manMsg)   #{'name': 'Charlie', 'gender': 'male', 'job': 'doctor', 'marital status': 'engaged'}
#   删除整个字典
# del manMsg
# print(manMsg)

# 方法二：clear，清空字典，但保留字典对象
manMsg.clear()
# 清空是指将字典中所有的数据抖删除掉，但保留字典的结构
print(manMsg)   #{}
print(type(manMsg))     #<class 'dict'>


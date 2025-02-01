# _*_ coding : utf-8 _*_
# @Time : 2025/2/1 15:44
# @Author : 田园
# @File : 34-Python_列表高级_查(查找)
# @Project : 26-Python_流程控制语句_if案例练习.py

# in是判断指定元素是否存在于列表中
# food_list=['火锅','麻辣烫','奶茶','过桥米线']

# 需求：判断在控制台输入的数据，是否存在于列表中
# food=input('请输入猪瘾犯时，想吃的食物')
# if food in food_list:
#     print('造吧，大馋丫头')
# else:
#     print('对不起，没有')

# not in
manList=['秦彻','萧逸','白起','夏彦','陆沉']
# 需求：在控制台上输入喜欢的男人，判断是否不在列表中
man=input('请输入你的男人')
if man not in manList:
    print('True-这儿没有你的男人')
else:
    print('False-带走你的男人')

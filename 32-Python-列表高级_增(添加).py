# _*_ coding : utf-8 _*_
# @Time : 2025/1/29 15:10
# @Author : 田园
# @File : 32-Python-列表高级_增(添加)
# @Project : 26-Python_流程控制语句_if案例练习.py

# append，追加，在列表的末端/最后添加一个新元素
food_list=['火锅','麻辣烫','酸菜馅饺子']
print(food_list)    #['火锅', '麻辣烫', '酸菜馅饺子']

# 调用append方法，将新元素添加到原列表的最末端
food_list.append('兰州牛肉面')
print(food_list)    #['火锅', '麻辣烫', '酸菜馅饺子', '兰州牛肉面']

# insert，插入
man_list=['Osborn','Sariel','Jesse']
print(man_list)     #['Osborn', 'Sariel', 'Jesse']
# 我的需求：要在Osborn和Sariel之间加上Evan，再在Sariel和Jesse之间插入Charlie
# insert方法的参数，第一个是索引位置，代表要插入的位置的下标；第二个是对象，就是要插入的元素内容
# insert(index-索引,object-对象)
man_list.insert(1,'Evan')
print(man_list)     #['Osborn', 'Evan', 'Sariel', 'Jesse']
# 看上一行，已成功插入对象，接下来照样，在第四个的位置插入Charlie
man_list.insert(3,'Charlie')
print(man_list)     #['Osborn', 'Evan', 'Sariel', 'Charlie', 'Jesse']

# exend，合并两个列表
num_list=[1,2,3]
num_list2=[4,5,6]
# extend方法的参数必须是可以迭代的数据，比如字符串、列表、元组、字典等，绝对不可以是int和float，但他俩是单个值不是系列值，想要变成可迭代就转为string或调用range方法。
num_list.extend(num_list2)
print(num_list)     #[1, 2, 3, 4, 5, 6]


# _*_ coding : utf-8 _*_
# @Time : 2025/2/8 19:44
# @Author : 田园
# @File : 42-Python_字典高级_遍历
# @Project : readme.md

# 遍历--》意思就是把数据一个一个的打印输出

manMsg={'name':'齐司礼','age':'3000','gender':'male','nickname':'翘屁嫩狐/狐狐'}

# 遍历方法一：遍历字典的key值，dicName.keys()
#     这里的keys()返回一个包含字典所有键的视图对象(dict_keys)，也就是可以获取到字典中所有的key值。当然.keys()也可以省略。
# for key in manMsg.keys():
#     print(key)

# 遍历方法二：遍历字典的value值，dicName.values()
#     这里的values()和上面的keys()的作用一样，只不过是用来获取字典中所有的value的。但在这里.values()不可以被省略，省略了就默认遍历key了。
# for value in manMsg.values():
#     print(value)

# 遍历方法三：遍历字典的key和value
#     调用items()，来获取字典的key和value，且for后面的变量必须是两个，缺其一就会返回元祖类型的数据
# for key,value in manMsg.items():
#     print(key,value)

# 遍历方法四：遍历字典的项/元素，其实就是键值对
for item in manMsg.items():
    print(item)



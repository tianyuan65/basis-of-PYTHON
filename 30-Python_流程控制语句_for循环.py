# _*_ coding : utf-8 _*_
# @Time : 2025/1/26 14:01
# @Author : 田园
# @File : 30-Python_流程控制语句_for循环
# @Project : 26-Python_流程控制语句_if案例练习.py

# 一、循环字符串，一个一个的输出字母，叫做循环，也叫做遍历
# country='China'
# 这不是循环或遍历，而是挑出来打印，当字符串长度很长时就无法使用
# print(country[0])   #C
# 格式：for 变量 in 要遍历的数据:
#           方法体
# 像前端里的forEach方法，
# 这里的c时字符串中一个又一个的字符串变量，country代表要遍历的数据
# for c in country:
#     print(c)

# 二、range(5)
# range方法的结果是一个可以遍历的对象
# range(5)代表的是0~4，默认从0开始到这个数字之前的数字结束，而且是左闭右开的区间，就是长这样[0,5)，
# print(range(5)) #range(0, 5)
# 所以将range(5)遍历，就会打印出0-4，这五个数字
# for r in range(5):
#     print(r)

# 三、range(1,6)
# range(起始值,结束值)
# 第一个参数代表起始值，也就是从指定的数字开始；第二个参数是结束值，到第二个参数前面的数字为止
# for r in range(1,6):
#     print(r)

# 四、range(1,10,3)
# range(起始值,结束值,步长)
# 从起始值开始，到结束值前一个数字结束，同样遵循左闭右开，在该区间内与前一个数字相差的数
# for r in range(1,10,3):
#     print(r)

# 五、循环一个列表--实际应用中用的最多
# 应用场景：爬虫时，会爬取并返回一个列表，需要做到的就是将列表中元素一个一个的遍历出来
manList=['秦彻','萧逸','左然']
# 遍历列表中的元素
# for man in manList:
#     print(man)
# 遍历列表中的下标
# 判断列表中元素的个数
# print(len(manList)) #3
# 遍历range方法返回的元素的个数，获取输出元素的下标
for num in range(len(manList)):
    print(num)

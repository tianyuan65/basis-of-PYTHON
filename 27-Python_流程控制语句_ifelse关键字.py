# _*_ coding : utf-8 _*_
# @Time : 2025/1/22 11:17
# @Author : 田园
# @File : 27-Python_流程控制语句_ifelse关键字
# @Project : 26-Python_流程控制语句_if案例练习.py

# ifelse语法
# if 判断条件:
#   判断条件为True时，执行的代码
# else:
#   判断条件为False时，执行的代码

age=input('请输入年龄')

if int(age)>18:
    print('可以去网吧了')
else:
    print('回家写作业！')

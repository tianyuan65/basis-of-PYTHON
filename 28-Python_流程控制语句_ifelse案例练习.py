# _*_ coding : utf-8 _*_
# @Time : 2025/1/25 13:38
# @Author : 田园
# @File : 28-Python_流程控制语句_ifelse案例练习
# @Project : 26-Python_流程控制语句_if案例练习.py

# 在控制台上输入一个数字，如果数字大于18，则输出欢迎光临娃娃屋；
# 否则，输出回家睡觉。

age=input('please enter your age.')

# 记得转换为整型
if int(age)>18:
    print('欢迎光临娃娃屋')
else:
    print('回家睡觉')

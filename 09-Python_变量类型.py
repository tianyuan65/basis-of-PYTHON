# _*_ coding : utf-8 _*_
# @Time : 2024/12/29 21:17
# @Author : 田园
# @File : 09-Python_变量类型
# @Project : learn_PYTHON基础

# 数据类型
# Number    数值
#   int
#   float
# Boolean   布尔
#   true
#   false
# String    字符串
# List      列表
# Tuple     元组
# Dictionary字典

# 变量类型的基本使用
# 定义一个变量并为其赋值时，不需要加前缀(比如向前端一样的var、const、let)
# Number---int
cash=10000
# Number---float
weight=54.1

# Boolean
# 在流程控制语句中使用
# 性别的变量，性别在实际的企业级开发中，使用的单词是sex或gender，且默认male是true
gender=True
sex=False

# String
# 用单或双引号圈起来的内容，但一单一双绝对不可以
lyrics='戏文说，相逢难逃别离，姻缘断情难'
lyrics2="殷勤多是假意，人心道不明。"
print(lyrics,lyrics2)
# 有一种情况，单引号和双引号的嵌套
lyrics3='"初听只当戏，"'
lyrics4="'再听已懂曲终意。'"
print(lyrics,lyrics2,lyrics3,lyrics4)
# 单引号套单引号，双引号套双引号，这两种怎么写都报错，属实是脱裤子放屁，实在没必要
# lyrics5=""""


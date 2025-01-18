# _*_ coding : utf-8 _*_
# @Time : 2025/1/18 14:16
# @Author : 田园
# @File : 22-Python_逻辑运算符的性能优化
# @Project : learn_PYTHON基础

# and的性能优化
a=67
# a>10 and print('hello world!')      #hello world!
# and的性能优化：当and左端的结果是False的情况下，后面的代码就不再执行了，即使执行了也没意义。
# a<10 and print('hello world!')

# or的性能优化
a=79
# 只要一端满足True，那么结果就是True
# a>93 or print('你好，世界@')     #你好，世界@
# 与and不同，or只要前面的结果为True的条件被满足，后面的代码将不再执行；
a>67 or print('你好，世界@')
# 但若顺序反过来，也就是只要满足前面的结果为True，or后面的就不再执行。
# 所以想用or，还想执行代码，那就把想要执行下去的写在or的前面
print('你好，世界@') or a>67     #你好，世界@

# and   短路与，and两端的条件都必须满足才可执行，有一端不满足则不会执行。
# or    短路或，or前面那一端的结果是False才会考虑后面那一端的执行，若or前面结果是True，后面的将不会执行，所以想要使用or，还想执行语句或其他代码，那就写在or的前面。

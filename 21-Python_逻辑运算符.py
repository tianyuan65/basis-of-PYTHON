# _*_ coding : utf-8 _*_
# @Time : 2025/1/18 12:19
# @Author : 田园
# @File : 21-Python_逻辑运算符
# @Project : learn_PYTHON基础

# 逻辑运算符
# and   与，and两边的数据必须全部都是True时，才会返回True，只要有一端返回的是False，就会返回False
# and两端都是False时，返回的就是False
print(10>11 and 2>3)    #False
# 与上面的作对比，当and有一端的结果是False，其返回的依旧是False
print(10<11 and 2>8)    #False
# 再与上面的两个作对比，必须保证and两端的返回结果都为True时，其返回结果才会是True
print(11>10 and 2<=3)   #True

# or    或，or两端只要有一端返回结果是True，另一端无论满不满足条件，都会返回True。也就是至少要有一端是True，其返回结果才会是True。
# or两端都是False的话，就会返回False
print(10>11 or 2>3)    #False
# 与上面的做个对比，or只要有一端满足条件，返回的就会是True
print(10<11 or 2>8)     #True
# 位置调换一下也是一样的结果
print(10>12 or 2>0)     #True
# 当然两端都是True也没毛病，只要有一端满足即可
print(11>9 or 3<=8)     #True

# not   非，取反
print(not True)     #False
print(not False)    #True
# 先算出not后面的结果，再not一下，得出的就是最终结果
print(not 1>2)      #True
print(not 1<=2)     #False

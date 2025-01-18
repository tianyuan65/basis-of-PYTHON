# _*_ coding : utf-8 _*_
# @Time : 2025/1/18 16:46
# @Author : 田园
# @File : 23-Python_输出
# @Project : learn_PYTHON基础

# 普通输出，就是print()
print('听锣鼓声断台下看客几经轮换，唯留余音婉转诉不清是曲难散')

# 格式化输出
# scrapy框架中会用到，爬虫后生成的json文件，可以放到excel文件或mysql又或者放到redis数据库中
age=29
name='谷江山'

# 需要注意要把int转换为string类型才可以正常打印输出
# print('人家刚满'+str(age)+'岁~') #人家刚满29岁~

# %s代表字符串的缩写，%d代表数值
# 这样就不需要进行强制数据类型转换和字符串拼接
print('大家好，我是729声工场的配音演员%s，今年%d岁' % (name,age)) #大家好，我是729声工场的配音演员谷江山，今年29岁
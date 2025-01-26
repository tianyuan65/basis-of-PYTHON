# _*_ coding : utf-8 _*_
# @Time : 2025/1/26 20:45
# @Author : 田园
# @File : 31-Python_字符串高级
# @Project : 26-Python_流程控制语句_if案例练习.py

# 获取长度：len，获取字符串的长度。
# 查找内容：find，查找指定内容在字符串中是否存在，若存在就返回该内容在字符串中第一次出现的开始位置索引值，若不存在，则返回-1.
# 判断：startswith,endswith，判断字符串是否以谁谁谁开头/结尾。
# 计算出现次数：count，返回str在start和end之间在mystr里出现的次数。
# 替换内容：replace，替换字符串中指定的内容，如果指定次数count，则替换不会超过count次。
# 切割字符串：split，通过参数的内容切割字符串。
# 修改大小写：upper,lower，将字符串中的大小写互换。
# 空格处理：strip，去空格。
# 字符串拼接：join，字符串拼接。

country='China'
# len()，除了判断字符串的长度，也可以判断列表的长度
print(len(country))     #5

# find()，区别于其他方法，大部分都是把变量作为参数传递进去，find函数是作为变量的方法被调用，就是xxx.find('想要查找的内容')
print(country.find('q'))    #-1
print(country.find('a'))    #4

# startswith和endswith，与find方法一样，是作为变量的方法被调用的
# startswith()，若以xxx开始，就返回True，否则返回False
print(country.startswith('C'))  #True
print(country.startswith('P'))  #False
# endswith()，若以xxx结尾，就返回True，否则返回False
print(country.endswith('y'))    #False
print(country.endswith('a'))    #True

# count()，用来统计某些字符出现的次数，作为变量的方法被调用，参数位置传递想要查询个数的字符，记得打引号，存在则返回其个数，不存在则返回0
words='aaabbbyfffciii'
print(words.count('f')) #3
print(words.count('w')) #0

# replace()，用于替换，还是作为变量的方法被调用，第一个参数传旧值或旧值中想要替换的字符，第二个参数传新值或想要替换为新值的字符
print(country.replace('C','c')) #china

# split()，依旧作为变量的方法被调用，切割想要去掉的符号或数字，在这里切割#，返回列表，在这里暂时返回列表，后续继续学着转换为字符串
symbol='1#2#3#4'
print(symbol.split('#'))    #['1', '2', '3', '4']

# upper()，将字符串中所有字母都转为大写
print(country.upper())  #CHINA
country1="PEOPLE'S REPUBLIC OF CHINA"
# lower()，将字符串中所有字母都转为小写
print(country1.lower())  #people's republic of china

# strip()，去掉所有空格
string='   a   '
print(len(string))  #7
print(string.strip())   #a
print(len(string.strip()))  #1

# join()，将两个字符串进行拼接
a='a'
# 意思是，将变量a插入到join方法参数字符串当中，但这不像是拼接，更像插入
print(a.join('string')) #sataraianag

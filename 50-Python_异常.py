# _*_ coding : utf-8 _*_
# @Time : 2025/2/15 12:59
# @Author : 田园
# @File : 50-Python_异常
# @Project : readme.md

# 报错的原因是文件的访问模式的问题，r访问模式在该文件不存在的情况下，就会报错
# file=open('test.txt','r')
# file.read()
# file.close()

# 异常的格式
# try:
#     可能出现异常的代码
# except 异常的类型
#     友好提示

try:
    file=open('test.txt','r')
    # file=open('test.txt','w')
    # file.write('古德猫宁')
    file.read()
except FileNotFoundError:
    print('系统正在升级，请稍后再试...')


# _*_ coding : utf-8 _*_
# @Time : 2025/1/30 13:56
# @Author : 田园
# @File : 33-列表高级_改(修改)
# @Project : 26-Python_流程控制语句_if案例练习.py

cityList=['北京','上海','深圳','兰州','西安']
print(cityList)     #['北京', '上海', '深圳', '兰州', '西安']

# 修改列表中的元素的值
# 需求：将西安改为沈阳
# 方法：通过下标来修改元素值
cityList[4]='沈阳'
print(cityList)     #['北京', '上海', '深圳', '兰州', '沈阳']

# 需求：将深圳改为天水
cityList[2]='天水'
print(cityList)     #['北京', '上海', '天水', '兰州', '沈阳']

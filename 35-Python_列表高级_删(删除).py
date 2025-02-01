# _*_ coding : utf-8 _*_
# @Time : 2025/2/1 17:46
# @Author : 田园
# @File : 35-Python_列表高级_删(删除)
# @Project : 26-Python_流程控制语句_if案例练习.py

movieList=['穿普拉达的女王','封神：朝歌风云','决战中途岛','红海行动','黑豹','长津湖']
print(movieList)    #['穿普拉达的女王', '封神：朝歌风云', '决战中途岛', '红海行动', '黑豹', '长津湖']

# del:根据下标删除列表中的元素
# 需求：删除movieList中的第三个元素
# 应用场景：若爬取的数据中，有不想要的个别数据，就可以通过下标的方式来删除
# del movieList[2]
# print(movieList)    #['穿普拉达的女王', '封神：朝歌风云', '红海行动', '黑豹', '长津湖']

# pop:删除列表中最后一个元素
# 需求：删除movieList中最后一个元素
# movieList.pop()
# print(movieList)

# remove:根据元素的值进行删除
# 需求：删除黑豹
movieList.remove('黑豹')
print(movieList)    #['穿普拉达的女王', '封神：朝歌风云', '决战中途岛', '红海行动', '长津湖']

# del是python语句，而不是列表方法，无法通过list来调用

# _*_ coding : utf-8 _*_
# @Time : 2025/1/25 14:57
# @Author : 田园
# @File : 29-Python_流程控制语句_elif
# @Project : 26-Python_流程控制语句_if案例练习.py

# 在控制台上输入成绩，
# 如果考了90或90以上，成绩为优秀；
# 如果考了80或80以上，成绩为良好；
# 如果考了70或70以上；成绩为中等；
# 如果考了60或60以上；成绩为及格；
# 否则，不及格

# score=int(input('please enter your score.'))

# 用if-else写法会导致穿透现象，就是如果输入了76，会把中等、及格都打印出来，因此这是个错误写法，不要这么写。
# if score>=90:
#     print('优秀')
# if score>=80:
#     print('良好')
# if score>=70:
#     print('中等')
# if score>=60:
#     print('及格')
# else:
#     print('不及格')

# elif相当于前端的switch判断，使用elif可以避免穿透现象
score=int(input('please enter your score.'))
if score>=90:
    print('优秀')
# 否则如果，成绩大于80，就打印良好；
elif score>=80:
    print('良好')
# 否则如果，成绩大于70，就打印中等；
elif score>=70:
    print('中等')
# 否则如果，成绩大于60，就打印及格；
elif score>=60:
    print('及格')
# 否则打印不及格
else:
    print('不及格')

# 用elif还有一个好处就是一旦某一条件成立，则后面的elif及else都不会再去判断了，减少了判断次数



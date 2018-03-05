# 0 -- 100
# 根据分数区间，打印出对应的级别
# 大于等于90, 并且  小于等于100
# 优秀
# 大于等于80, 并且  小于90
# 良好
# 大于等于60, 并且  小于80
# 及格
# 大于等于0, 并且  小于60
# 不及格
# score = input("请输入你的分数：")
# score = float(score)
# if score >= 90 and score <= 100:
#     print("优秀")
# if score >= 80 and score <= 90:
#     print("良好")
# if score >= 60 and score < 80:
#     print("及格")
# if score >= 0 and score < 60:
#     print("不及格")

score = input("请输入你的分数：")
score = float(score)
if 90 <= score <= 100:
    print("优秀")
if 80 <= score < 90:
    print("良好")
if 60 <= score < 80:
    print("及格")
if 0 <= score < 60:
    print("不及格")
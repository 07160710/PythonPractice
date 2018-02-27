# 格式化输出
name = "kf"
age = 20
print("我的姓名是%s,年龄是%d"%(name,age))

# %[(name)][(flags)][(width)][.precision]typecode        typecode类码
# []  可选参数

# （name）
# 表示，根据，制定的名称（key），查找对应的值，格式化到字符串当中
mathScore = 88
englishScore = 99
# print("我的数学分数是%d，英语的分数是%d"%(mathScore,englishScore))
print("我的数学分数是%(ms)d，英语的分数是%(es)d"%({"es":englishScore,"ms":mathScore}))

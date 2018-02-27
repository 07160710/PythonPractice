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
# ({字典})
print("我的数学分数是%(ms)d，英语的分数是%(es)d"%({"es":englishScore,"ms":mathScore}))


# width ,表示占用的宽度
# flags 空 ，表示右对齐 ；   -   表示左对齐 ；  空格 表示在正数的左侧填充一个空格，从而与负数对齐；  0  表示使用 0 填充(单位数不够时)。
print("%-5d" % mathScore)
print("% d" % mathScore)

min = 5
sec = 18
print("%02d分:%02d秒"%(min,sec))

# .precision 表示小数点后精确度
score = 59.9
print("%.2f" % score)

#typecode  i/d十进制表示   o 八进制   x十六进制  e E  整数，浮点数转化成科学计数法  f F浮点数    g自动调整将整数，浮点数转化成浮点型或科学计数法（超6位数用科学计数法）
# G 自动调整将整数，浮点数转化成浮点型或科学计数法（超6位数用科学计）s 获取对象的_str_方法返回值 。 r 获取_repr_方法返回值 。c 将数字转化成Unicode对应的值。
print("%d" % 0b1010)
print("%E" % 155555555555)
print("%g" % 1011111)
print("%s" % "abcd")
print("%c" % 19996)

#99%
# %% 表示一个百分号%
print("99%")
sss = 65
print("%d%%" % sss)


print(6 + 6)
print("6" + "6")
# 查看数据类型   type(xxx).....
print(type(6))
result = type("6")
print(result)
num = 10
print(type(num))
print("----------------------")
# 数据类型转化   int(xxx) float(xxx)
# str()转化成字符串
# repr(xxx)将xxx转换成一个表达式字符串
# chr()转化成字符
# unichr()转化成一个Unicode字符
# ord()转化成对应的整数值
# hex(x)转化成6进制
# tuple（） list()  eval()  oct()
nums = "6"
print(type(int(nums)))
print(4 + int(nums))
print(str(4) + nums)

score = input("请输入一个数字") #字符串数值类型
print(type(score))
print(int(score) + 6)
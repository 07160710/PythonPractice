# pyhon3.x 输出
import sys
from time import sleep
# 输出一个值
print(123)
#输出变量
num = 10
print(num)
# 输出多个变量
num2 = 66
print(num, num2)
# 格式化输出
name = "kf"
age = 20
# 我的名字是xxx，年龄是xx
print("我的名字是" ,name , ",年龄是",age)
print("我的名字是%s，年龄是%d"%(name,age))
print("我的名字是{0}",",年龄是{1}".format(name, age))
# 输出到文件中
f = open("test3.txt","w")
print("i am a itman",file=f)
# print("xxxxxxxxxxxxxxxx",file=sys.stdout)
# 输出不自动换行
print("abc",end="\n")
# 输出的各个数据，使用分隔符分割
print("1","2","3",sep="----")

print("---------------------------------")
# flush 参数说明
# print("请输入账号\n",end="")
print("请输入账号\n",end="",flush=True)

# 休眠5s
sleep(5)
# print("睡了5s")
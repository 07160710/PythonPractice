# + 加法运算符
print(1 + 1)
print("1" + "2")
print([1 , 2] + [3 , 4])
# — 减法运算符
print(10 - 3)
print(1 - 2)
# * 乘法运算符
print(2 * 6)
# ** 幂运算符
print(2 ** 5)
# / 除运算符
print(5 / 2)
print(5.2 / 2)
# // 整除运算符
print(5 // 2)
print(5.2 // 2)
# % 求余运算符
print(5 % 2)
print(9 % 3)
# = 赋值运算符
a = 10
c = 10
b = a + c
print(b)
d,e,f = 1,2,3
#链式赋值
i = r = s = 11
#不可除以0，优先级级  （）先使用
result = (1+2) *3 / 4
print(result)
#行列
# *   *   *   *
# *   *   *   *
# *   *
# num = 6
# row = num // 4
# col = num % 4
# print(row,col)
# 复合运算符  a x= 值   =》  a = a x 值
# +=运算符
num = 10
#num = num + 5
num += 5
print(num)
# -=运算符  *=  **=
w = 10
# w *= 20
w **= 2  # w = w ** 2
print(w)
# *= 运算符
# /=运算符  //=
# 比较运算符（>   <   ==  >=   <=  !=   is  ）  <>  等价于 !=
flag = 10 == 2
print(flag)
x = 10
bs = 10
# 比较唯一标识
# id()查看唯一标识码
print(id(x),id(bs))
print(x is bs)
print("--------------------")
a1 = [1]
b1 = [1]
print(a1 == b1)
print(id(a1),id(b1))
print(a1 is b1)


# 链式比较运算符

nums = 10
# nums > 5 && nums < 20
print(5 < nums < 20)

print("--------------------")
# 逻辑运算符（整个逻辑表达式不一定只是true 和 false）
# not 非  取反，真 --> 假 ； 假 ---> 真；
k = True
# 一元运算符
print(not k)
# and 与 ，并且 and 的两边，必须都为真，最终才会是真  真  and  真  - 》 真，一假全假
# 二元运算符
print(True and False)
# or 或 ，或者 ， or 的两边，只要有一个是真的，那么最终都是真的,一真全真
print(True or False)
# 非bool类型的，非0即真，非空即真
print(bool(1))
print(0 or True)
print(1 and 3)
print(1 or 3)
# print(bool(0))
# print(bool(""))


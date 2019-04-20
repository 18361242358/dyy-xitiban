import math
# print (1)
# ceil()向上取整
'''
help(math)
print(math.ceil(5.1) )


# floor()向下取整
# print(math.floor(5.9))
# 查看系统关键字 不能用来当做变量名
import keyword
print (keyword.kwlist)
# 四舍五入 python 内置函数
print(round(5.3))
print(round(5.5))

# sqrt(）开平方 返回浮点数
print(math.sqrt(9))

# sin 正弦

# pwd()与幂运算差不多，计算一个数的几次方，有两个参数，第一个是底数，第二个是指数
print(math.pow(4,3))   # 4 的 3 次方 返回浮点型
print(4**3)  #返回整形

# fabs()对一个数取绝对值 返回浮点数
print(math.fabs(-1))

# abs()获取绝对值 不是数学模块的 是Python内置函数
print(abs(-1))

#  fsum() 对整个序列求和 返回浮点数


# sum()Python内置求和 返回看给的类型

# math.modf()将一个浮点数拆分为小数部分跟整数部分 组成元祖
print(math.modf(4.5))
print(math.modf(0))
print(math.modf(3))

# copysign() 将第二个数的符号（正负号）传给第一个数 返回第一个数的浮点数
print(math.copysign(2,-3))
print(math.copysign(-2,3))


print(math.e)
print(math.pi)
'''
import random
# # random() 获取0-1之间的随机小数 包含0 不包含1
# for i in range(10):
'''
    # range可迭代 用for
    # print (random.random())
    # 随机指定开始和结束之间的整数值
    # print(random.randint(1,6))
    # random.randrange()获取指定开始和结束之间的值，可以指定间隔值
    # print(random.randrange(1,9,2))
 '''
# choice() 随机获取列表的值
# print(random.choice([10,24,4,15]))

# shuffle() 随机打乱序列，返回值是none
'''
list1 = ([10,24,4,15])
print(list1)
print(random.shuffle(list1))
print(list1)
'''
#  uniform() 随机获取指定范围内的值（包括小数）
for n in range(10):
    print(random.uniform(1,9)) 
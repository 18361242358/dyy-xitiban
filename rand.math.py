import random
import math

num = input("请输入一个三位数：")
# 检测输入是否为纯数字
if num.isdigit() and  100<= int(num) <=999:
    #判断输入的数，与系统随机数比较大小
    # 大于随机数
    pass
else:
    print("请按规定输入")
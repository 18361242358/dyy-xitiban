'''
#输入姓名
name = input ("请输入你的姓名:")
print ("你好，"+name)

#输入0-100整数
temp = input ("请输入一个0到100的整数：")
if temp.isdigit():
    temp = int(temp)
    if 1 <= temp <= 100:
        print("对了")
    else:
        print("不对")
else:
    print("budui")
print(type(temp)


#判断是否为闰年
year = input ("请输入年份：")
if year.isdigit():
    year = int (year)
    if year % 4 == 0 :
        print(str(year) + "是闰年")
    else:
        print(str(year) + "不是闰年")
else:
    print("叫你输入年份")

#猜数字
import random
secert = random.randint(1,100)
times = 3
while times:
    num = input("请输入数字：")
    if num.isdigit():
        temp = int(num)
        if temp == secert:
            print("对了")
            break
        elif temp < secert:
            print("小了")
            times = times - 1
        else:
            print("大了")
            times = times - 1
    else:
        print("输入数字")
print("机会用完了")

#0-100所有奇数,注意缩进
ls = range (0,101)
for i in ls:
    if i % 2 == 1:
        print(i)

#爱因斯坦阶梯
x = 0
while x < 1000:
    if (x % 2 == 1)\
        and(x % 3 == 2)\
        and(x % 5 == 4)\
        and(x % 6 == 5)\
        and(x % 7 == 0):
        print(x)
        x += 1
        #break
    else:
        x += 1
print("循环结束")
'''
#验证密码
password = "abc123"

times = 3
while times:
    input_password = input("请输入密码：")

    if '*'in input_password:
        print("密码中不能有*")
    else:
        if input_password == password:
            print("密码正确")
            break
        else:
            print("密码错误")
            times -= 1




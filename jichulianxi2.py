'''
#100-999之间的水仙花数(一个三位数为各位置的数的立方和，如153=1^3+5^3+3^3)
for i in range(100,1000):
    temp = list(str(i))
    a = int(temp[0])
    b = int(temp[1])
    c = int(temp[2])
    if a**3+b**3+c**3 == i:
        print(i)

#三色球问题
#有 红 黄 蓝三种球 红3 黄3 蓝6  12球混合 从中摸出8个 球各种颜色搭配
for red in range(4):
    for yellow in range(4):
        for blue in range (2,7):
            if red + yellow + blue == 8:
                print("red:{}".format(red))
                print("yellow.{}".format(yellow))
                print("blue.{}".format(blue))
                print("*"* 20)

#将列表中的图灵 替换成 大拿

ls = [1,[1,2,["图灵"]],3,5,8,9]
ls[1][2][0] = "dana"
print(ls)
'''
#用户名问题 （自己的）

user_pass = {"zhangsan":"111","lisi":"222","wangwu":"333"}

def user_creat(username,password):
    usernames = user_pass.keys()
    if username in usernames:
        print("用户名已注册")
    else:
        user_pass[username] = password
        print("你注册成功了")
user_creat(input("请输入用户名"),input("请输入密码"))
print(user_pass)


def user_login(username,password):
    usernames = user_pass.keys()
    if username not in usernames :
        print("用户名不存在")

    else:
        if password != user_pass[username]:
            print("密码错误")
        else:
            print("登录成功")
#user_login("lisi",222)
user_login(input("请输入用户名"),(input("请输入密码")))
print(user_pass)
''''
#示范
user_pass = {"zhangsan":111,"lisi":222,"wangwu":333}
def creat_user(username,password):
    usernames = user_pass.keys()
    if username in usernames:
        print("用户名已注册")
    else:
        user_pass[username] = password
        print("你注册成功了")
creat_user("dyy",123)
print(user_pass)

def login_user(username,password):
    usernames = user_pass.keys()
    if username not in usernames or password != user_pass[username]:
        print ("用户名或密码不正确")
    else:
        print("成功")
login_user("dyy",123)

'''



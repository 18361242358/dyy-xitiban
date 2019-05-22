def a():
    #打印字母A
    #控制行
    for i in range(1,6):
        #判断开始输入的位置
        for k in range(6-i):
            #print里 两个引号之间的空格随便去掉哪个都可以出现等腰三角的情况
            print("",end=" ")
        #控制列
        for j in range(1,i+1):
            if i==1 or i==3 or j==1 or j==i:
                print('*',end=" ")
            else:
                #此处就要全部有空格了
                print(" ", end=" ")
        print()
# a()

#打印字母B
def b():
    for i in range(1,4):
        for j in range(1,4):
            if i==1 or i==4 or j==1:
                if j<3:
                    print('*', end=" ")
            elif j==3:
                if i==2 or i==3:
                    print('*', end=" ")
            else:
                print(' ',end=" ")
        print()
    for i in range(1,5):
        for j in range(1,4):
            if i==1 or i==4 or j==1:
                if j < 3:
                    print('*', end=" ")
            elif j==3:
                if i==2 or i==3:
                    print('*', end=" ")
            else:
                print(' ', end=" ")
        print()
# b()

#打印C
def c():
    for i in range(1,5):
        for j in range(1,4):
            if i==1 or i==4:
                if j==1:
                    print(' ', end=" ")
                else:
                    print('*', end=" ")
            elif j == 1:
                if i == 2 or i == 3:
                    print('*', end=" ")
            else:
                print(' ', end=" ")
        print()
# c()

#打印D
def d():
    for i in range(1,5):
        for j in range(1,4):
            if i==1 or i==4 or j==1:
                if j<3:
                    print('*', end=" ")
            elif j==3:
                if i==2 or i==3:
                    print('*', end=" ")
            else:
                print(' ', end=" ")
        print()
# d()

#打印E
def e():
    for i in range(1,6):
        for j in range(1,4):
            if i==1 or i==3 or i==5 or j==1:
                print('*', end=" ")
            else:print(' ', end=" ")
        print()
# e()

#打印F
def f():
    for i in range(1,6):
        for j in range(1,4):
            if i==1 or i==3  or j==1:
                print('*', end=" ")
            else:print(' ', end=" ")
        print()
# f()

#打印G
def g():
    for i in range(1, 5):
        for j in range(1, 5):
            if i == 1 or i == 4:
                if j == 1 :
                    print(' ', end=" ")
                else:
                    print('*', end=" ")
            elif i == 2 and j == 1:
                    print('*', end=" ")
            elif i == 3:
                if j ==2 :
                    print(' ', end=" ")
                else:
                    print('*', end=" ")
            else:
                print(' ', end=" ")
        print()
# g()

#打印H
def h():
    for i in range(1,6):
        for j in range(1,4):
            if  i==3  or j==1 or j == 3:
                print('*', end=" ")
            else:print(' ', end=" ")
        print()
# h()

#打印I
def i():
    for i in range(1,6):
        for j in range(1,4):
            if   i == 1 or i == 5 or j==2 :
                print('*', end=" ")
            else:print(' ', end=" ")
        print()
# i()

#打印J
def j():
    for i in range(1,6):
        for j in range(1,5):
            if   i == 1 or j==3 :
                if i < 5:
                    print('*', end=" ")
            elif i == 4 and j == 1 :
                print('*', end=" ")
            elif i == 5 and j ==2 :
                print('*', end=" ")

            else:
                print(' ', end=" ")
        print()
# j()

#打印K
def k():
    for i in range(1,3):
        for j in range(i,4):
            if i ==1 and j == 2:
                print(' ',end=" ")
            else:
                print('*',end=" ")
        print()
    for i in range(1,4):
        for j in range(i):
            if j == 0 or j == i-1:
                print('*', end=" ")
            else:
                print(' ',end=" ")
        print()
# k()

#打印L
def l():
    for i in range(1,5):
        for j in range(1,4):
            if i==4 or j==1:
                print('*', end=" ")
            else:print(' ', end=" ")
        print()
# l()

#打印M
def m():
    for i in range(1,6):
        #判断开始输入的位置
        for k in range(6-i):
            #print里 两个引号之间的空格随便去掉哪个都可以出现等腰三角的情况
            print("",end=" ")
        #控制列
        for j in range(1,i+1):
            if i==1 or j==1 or j==i:
                print('*',end=" ")
            else:
                #此处就要全部有空格了
                print(" ", end=" ")

        #判断开始输入的位置
        for k in range(5-i):
            #print里 两个引号之间的空格随便去掉哪个都可以出现等腰三角的情况
            print(" ",end=" ")
        #控制列
        for j in range(1,i+1):
            if i==1 or j==1 or j==i:
                print('*',end=" ")
            else:
                #此处就要全部有空格了
                print(" ", end=" ")
        print()
m()
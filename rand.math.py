import random
import math
'''
输入一个三位数与程序给出的随机数比较，
1、如果大于随机数，分别输出各位数字
2、等于 你中奖了
3、小于 输出120个字符串 每一行都是一个12位字符串，前4字母后8数字
'''

class GameNum():
    def line(self):
        #定义字符串拼接函数
        str_num = ''
        #循环前四个随机字母 用ascii对应的值来随机再转化为字母
        for i in range(4):
            #随机小写字母的ascii值
            num = random.randrange(97,123)
            #将ascii值转换成对应的字母
            str_s = chr(num)
            #依次拼接得到随机字母
            str_num = str_num+str_s
        #循环后8个随机数字
        for i in range(8):
            num = random.randrange(0,10)
            str_num = str_num+str(num)
        #print(str_num)
        return str_num

    def num_game(self,total,source):

        while 1:

            num = input("请输入一个三位数，输入-1结束：")
            if num == '-1':
                break
            #随机数
            random_num = random.randrange(100,1000)
            # 检测输入是否为纯数字
            if num.isdigit() and  100 <= int(num) <= 999:
                total+=1
                print("有效次数为:%d次"%total)
                num = int(num)

                #判断输入的数，与系统随机数比较大小
                # 大于随机数
                if num > random_num:
                    #求百位数方法 地板除100或用数学模块中的floor()函数
                    bai = num//100
                    print(bai)
                    #十位数 把三位数取100的余数,再地板除10
                    shi = num%100//10
                    print(shi)
                    #个位数 直接取10的余
                    ge = num%10
                    print(ge)
                    print("你输入的比随机数大，随机数是",random_num)
                    print("这个三位数的个位是{0}，十位数是{1},百位数是{2}".format(ge,shi,bai))

                if num == random_num:
                    source = source+100
                    print("你中奖了,目前分数为",source)
                if num < random_num:
                    print("你输入的比随机数小，随机数是",random_num)
                    for i in range(10):
                        str_line = GameNum.line(self)
                        #print(str_line)
                        #执行文件存入操作
                        with open('str_num.txt','a') as f:
                            f.write(str_line+'\n')


            else:
                print("请按规定输入")

if __name__ == '__main__':#调试代码
    print(__name__)#本身模块是__main__，导入其他模块 就是其他模块名字
    print(11111)#这里可以打印 导入到其他模块 不会打印
    #定义一个变量存储初始分数
    source = 0
    #定义一个变量表示有效输入次数
    total = 0
    # num_game(total,source)


    #GameNum.num_game(0,total,source)
    #实例化类
    game = GameNum()
    game.num_game(total,source)
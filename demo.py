import rand_math
import rand_zimu

print('请选择游戏\n1.数字游戏\n2.字母游戏')
game = input('输入1或2:')
if game == '1':
    #下面GameNum有()表示实例化，下面num_game只需要传两个参数
    #           没有()则需要三个参数
    game_num = rand_math.GameNum()
    game_num.num_game(0,0)
elif game == '2':
    game_zimu = rand_zimu.GameZiMu()
    game_zimu.a()

else:
    print('输入错误')
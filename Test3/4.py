import random

a = random.randint(0,101)
n = 0
while True:
    print(a)
    b = int(input('请输入一个整数：'))
    
    if b > a:
        print('大了')
        n = n + 1
    elif b < a:
        print('小了')
        n = n + 1
    else:
        n = n + 1
        if n <= 5:
            print(f'经过{n}次的回答，答对了')
            break
        else:
            Quit = input('游戏失败，要继续游戏吗？ YES/NO :')
            if Quit.upper() == 'NO':
                break

        
        
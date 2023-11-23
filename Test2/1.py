import random

a = random.randint(0,1001)
n = 0
while True:
    b = int(input('请输入一个整数：'))
    if b > a:
        print('大了')
        n = n + 1
    elif b < a:
        print('小了')
        n = n + 1
    else:
        n = n + 1
        print(f'经过',n,'次的回答，答对了')
        break
def factor(num):
    factors = []
    for i in range(1,num // 2 + 1):
        if num % i == 0:
            factors.append(i)
    return factors

while True:
    try:
        a = int(input('请输入大于0的整数：'))
        if a == 0:
            break
        elif a > 0:
            factors = factor(a)
            print(f'{a}:',end='')
            for i in factors:
                print(i,end=' ')
            print()
    except ValueError:
        print('输入无效，请输入一个正整数')
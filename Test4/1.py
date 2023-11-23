def PrimeNumber(a):
    for i in range(2,int(a**0.5)+1):
        if a % i == 0:
            return False
    return True 
        
while True:
    try:
        a = int(input('请输入大于0的整数：'))
        if a == 0:
            break
        elif PrimeNumber(a):
            print(f'{a}是素数')
        else:
            print(f'{a}不是素数')
    except ValueError:
        print('输入无效，请输入一个正整数')
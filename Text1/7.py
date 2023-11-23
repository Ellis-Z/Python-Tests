while True:
    a = int(input('请输入一个整数：'))
    if a >= 2:
        prime = True
        for i in range(2, int(a**0.5) + 1):
            if a % i == 0:
                prime = False
                break
        if prime:
            print(a, '是素数')
        else:
            print(a, '不是素数')
    else:
        break

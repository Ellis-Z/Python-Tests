while True:
    a = int(input('请输入大于0的整数：'))
    if a > 0:
        flag = True
        for i in range(2,a-1):
            if a % i == 0:
                flag = False
                print(f'{a}不是素数')
                break
        if flag == True:
            print(f'{a}是素数')
    elif a == 0:
        break

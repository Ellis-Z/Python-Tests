
while True:
    a = int(input('请输入一个整数：'))
    list = []
    if a > 0:
        b = a
        while b > 0:
            list.append(b % 10)
            b //= 10
    else:
        break
    print(sum(list))
    
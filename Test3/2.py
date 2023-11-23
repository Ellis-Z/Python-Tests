n = int(input('请输入一个N：'))

for i in range(n+1):
    for j in range(n-i):
        print(' ',end='')
    for k in range(2*i-1):
        print('*',end='')
    print()
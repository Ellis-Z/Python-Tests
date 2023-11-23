
def flower(a):
    hundreds = a // 100
    tens = (a // 10) % 10
    ones = a % 10
    if hundreds**3 + tens**3 + ones**3 == a:
        return True

while True:
    try:
        a = int(input('请输入大于0的整数：'))
        if a <= 100 or a >= 999:
            break
        elif flower(a):
            print(f'{a}是水仙花数')
        else:
            print(F'{a}不是水仙花数')
    except ValueError:
        print('输入无效，请输入一个正整数')
def GCD_function(a,b):
    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(smaller-1,2,-1):
        if a % i == 0 and b % i == 0:
            return i

while True:
    try:
        a = int(input('请输入第一个大于0的整数：'))
        b = int(input('请输入第二个大于0的整数：'))
        if a == 0 or b == 0:
            break
        elif a > 0 and b > 0:
            gcd = GCD_function(a,b)
            lcm = a * b // gcd
            print(f'最大公约数是{gcd}')
            print(F'最小公倍数是{lcm}')
    except ValueError:
        print('输入无效，请输入一个正整数')

# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# def lcm(a, b):
#     return a * b // gcd(a, b)     
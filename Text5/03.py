def Fibonacci(num):
    if num < 2:
        return 1
    else:
        return Fibonacci(num-1) + Fibonacci(num-2)  

while True:
    try:
        a = int(input('请输入大于0的整数：'))
        if a <= 0:
            break
        elif a > 0:
            Fibon = Fibonacci(a)
            print(f'第{a}个斐波那契数列是{Fibon}')
    except ValueError:
        print('输入无效，请输入一个正整数')

# def Fibonacci(num):
#     if n <= 0:
#         return "输入错误"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         a, b = 0, 1
#         for i in range(2, n):
#             a, b = b, a + b
#         return b
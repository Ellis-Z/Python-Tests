a = int(input('请输入一个整数：'))
list = []
s = 0
while a > 0:
    list.append(a % 10)
    a //= 10
print(sum(list))
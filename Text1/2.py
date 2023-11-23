while True:
    a = int(input('请输入成绩：'))
    if a >= 0 and a <= 100:
        if a <= 100 and a >= 90:
            print('优秀')
        elif a<=89 and a >= 80:
            print('良好')
        elif a<=79 and a >= 70:
            print('中等')
        elif a<=69 and a >= 60:
            print('及格')
        else:
            print('不及格')
    else:
        break
    


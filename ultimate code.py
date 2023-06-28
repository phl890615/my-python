import random
num = random.randint(1,99)
Max = 100
Min = 0
answer = 0
while answer != num:
    answer = int(input('猜一個數字1~100:'))
    if answer > Min and answer < Max:
        if answer > num:
            print(Min,'~',answer)
            Max = answer
        elif answer < num:
            print(answer,'~',Max)
            Min = answer
        else:
            print('恭喜猜對了')
    else:
        print('超出範圍')


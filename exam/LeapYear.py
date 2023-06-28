s = str(input())
ss=s.split(',')
y = int(ss[0])
m = int(ss[1])
if m == 2:
    if y%4==0 and y%100!=0:
        print(29)
    elif y%400==0:
        print(29)
    else:
        print(28)
elif m == 4 or m ==6 or m == 9 or m ==11:
    print(30)
else:
    print(31)
    

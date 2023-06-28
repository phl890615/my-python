n = int(input())
d = float(input())
if n==1:
    if d<=100:
      print(d*2.5)
    elif d<=300:
      print(d*3.3)
    else:
      print(d*4.2)
elif n==2:
    print(150+d*1.9)
elif n==3:
    if d<=300:
        print(d*6)
    else:
        print(d*6.8)

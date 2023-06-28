a=int(input())
b=int(input())
c=abs((30*a)-(6*b))
if c>180:
    x=360-abs((6*b)-(30*a))
elif c<180:
    x=(30*a)-(6*b)
print(int(abs(x)))


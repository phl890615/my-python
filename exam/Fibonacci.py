n=int(input())
a=1
b=1
for i in range(1,n-1):
    g=a+b
    a=b
    b=g
print(g)


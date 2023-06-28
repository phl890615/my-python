n=int(input())
a=n//100
b=(n//10)%10
c=n%10
g=a**3+b**3+c**3
if g==n:
    print("true")
else:
    print("false")

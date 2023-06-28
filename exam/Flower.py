money=int(input())
a=0
b=0
c=0
d=0
if money>=50:
    a=money//50
    money=money%50
if money>=10:
    b=money//10
    money=money%10
if money>=5:
    c=money//5
    money=money%5
if money>=1:
    d=money//1
print(a+b+c+d,a,b,c,d)
----------------
m=int(input())
a=int(m//50)
b=int((m-a*50)//10)
c=int((m-a*50-b*10)//5)
d=int((m-a*50-b*10-c*5)//1)
sum=a+b+c+d
print(sum.a.b.c.d)


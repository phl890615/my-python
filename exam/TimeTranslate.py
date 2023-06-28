n=eval(input())
h=n//3600
m=(n%3600)//60
s=n-(h*3600)-(m*60)
print(str(h)+'時'+str(m)+'分'+str(s)+'秒')

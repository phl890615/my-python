s=str(input())
ss=s.split('#')
n=len(ss)
i=n-1
for x in range(1,n+1):
    if x == n:
        print(ss[i],end=' ')
    else:
        print(ss[i],end='#')
        i-=1

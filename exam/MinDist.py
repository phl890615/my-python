s=input()
ss=s.split(',')
n=len(ss)
a=[]
for i in range(n):
    ss[i]=int(ss[i])
for i in range(1,n):
    if abs(ss[i]-ss[i-1])>0:
        a.append(abs(ss[i]-ss[i-1]))
print(min(a))


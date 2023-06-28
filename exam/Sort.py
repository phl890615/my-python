s=input()
ss=s.split(',')
n=len(ss)
for i in range(n):
    ss[i]=int(ss[i])
ss=sorted(ss)
for j in ss:
 print(j,end=' ')

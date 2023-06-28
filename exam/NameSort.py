s=input("")
ss=s.split(",")
n=len(ss)
a=sorted(ss,key=len,reverse=True)
for i in range(0,n):
    print(a[i],end=" ")
 

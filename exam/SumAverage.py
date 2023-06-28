s =input()
ss=s.split(',')
n=len(ss)
a=0
for i in range(n):
    ss[i]=int(ss[i])
for i in ss:
  a=a+i
  b=a//n  
print("sum:",end='')
print(a,"average:",end='')
print(b/1)


=============
s=input()
ss=s.split(',')
n=len(ss)
sum=0
for i in range(n):
    ss[i]=int(ss[i])
for i in ss:
    sum+=i
print('sum:',end='')
print(sum,'average:',end='')
print(sum//n/1)
#自己寫的


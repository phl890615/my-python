n =int(input())
d =int(input())
count=0
for i in range(1,n+1):
   if n%i==0 and i%d==0:
       count+=1
print(count)

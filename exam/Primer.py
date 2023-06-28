def prime(n):
    for j in range(2,n):
         if n % j ==0:        
            return False
    else:
     return True 
n=int(input())
for j in range(2,n+1):
    if prime(j):
     if prime(n-j):
         print(j,n-j)
         break
     

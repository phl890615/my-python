def prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
n = int(input('輸入一個正整數:'))
for i in range(2,n+1):
    a = prime(i)
    if a:
        print(i,end=' ')

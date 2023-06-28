def factorial(n):
    sum = 1
    for i in range(1,n+1):
        sum *= i
    return sum
def exp(n):
    a = 0
    b = 0
    for i in range(1,n+1):
        a = 2**i    
        b += a
    return b
n = int(input('輸入一個整數:'))
temp = factorial(n)
top = exp(n)
print(temp,'',top)

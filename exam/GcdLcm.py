def GCD(a, b):
        m = a % b
        while (m > 0):
                a = b
                b = m
                m = a % b
        return b

def LCM(a, b):
        return a * b // GCD(a, b)
a=int(input())
b=int(input())
x=GCD(a,b)
y=LCM(a,b)
print(x,y)

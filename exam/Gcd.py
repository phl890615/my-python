a = int(input())
b = int(input())
m = a % b
while (m > 0):
        a = b
        b = m
        m = a % b
print(b)

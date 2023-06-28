s=input()
a=''
b=0
for i in s:
    if s.count(i)//2>0:
        if i not in a:
            a+=i
            b+=s.count(i)//2
print(b)

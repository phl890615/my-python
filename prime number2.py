flag = True
n = int(input("輸入一個數字:"))
for i in range(2,n):
    if n % i == 0:
        flag = False
        break
if flag:
    print('這是質數') 
else:
    print('這不是質數')

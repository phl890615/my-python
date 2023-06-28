n = int(input("輸入一個數字:"))
for i in range(2,n):
    if n % i == 0:
        print('這不是質數')
        break
else:
    print('這是質數')

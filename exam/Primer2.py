def prime(x):
     for i in range(2,x):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=' ')

x=eval(input())
prime(x)

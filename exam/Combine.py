s=input()
ss=s.split(',')
x=ss[0][0]+ss[0][1]+ss[0][2]
for i in range(0,8):
    if ss[1][i] not in x:
        x+=ss[1][i]    
print(x)





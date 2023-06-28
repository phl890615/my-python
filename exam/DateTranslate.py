s=input()
ss=s.split('/')
if int(ss[0])==1:
    print('January',end='')
elif int(ss[0])==2:
    print('February',end='')
elif int(ss[0])==3:
    print('March',end='')
elif int(ss[0])==4:
    print('April',end='')
elif int(ss[0])==5:
    print('May',end='')
elif int(ss[0])==6:
    print('June',end='')
elif int(ss[0])==7:
    print('July',end='')
elif int(ss[0])==8:
    print('August',end='')
elif int(ss[0])==9:
    print('September',end='')
elif int(ss[0])==10:
    print('October',end='')
elif int(ss[0])==11:
    print('November',end='')
else:
    print('December',end='')
print(' '+ss[1]+','+ss[2],end='')
    

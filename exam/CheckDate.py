y=int(input())
m=int(input())
d=int(input())
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    if d<=31:
        print(y,end="/")
        print(m,end="/")
        print(d)
    else:
        print("日期錯誤")
if m==4 or m==6 or m==9 or m==11:
    if d<=30:
        print(y,end="/")
        print(m,end="/")
        print(d)
    else:
        print("日期錯誤")
if m==2:
    if y%400==0:
        if d<=29:
            print(y,end="/")
            print(m,end="/")
            print(d)
        else:
            print("日期錯誤")
    elif y%4==0 and y%100!=0:
        if d<=29:
            print(y,end="/")
            print(m,end="/")
            print(d)
        else:
            print("日期錯誤")
    else:
        if d<=28:
            print(y,end="/")
            print(m,end="/")
            print(d)
        else:
            print("日期錯誤")




                

    
        

s=input()
ss=s.split(",")
for i in range(0,1):
    if (int(ss[i+1])-int(ss[i]))== (int(ss[i+2])-int(ss[i+1])):
        print("YES")
    else:
        print("NO")
                                
                    
    


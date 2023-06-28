s=input()
ss=s.split(",")
if int(ss[3])/int(ss[2])== int(ss[2])/int(ss[1]) and int(ss[2])/int(ss[1]) == int(ss[1])/int(ss[0]):
    print("Yes")
else:
    print("No")

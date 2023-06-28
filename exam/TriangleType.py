x=int(input())
y=int(input())
z=int(input())
if(x+y>z and x+z>y and y+z>x):
  if(x==y==z ):
     print("正三角形")
  elif(x==y or x==z or y==z):
     print("等腰三角形")
  else:
     print("一般三角形")
else:
 print("非三角形")

     

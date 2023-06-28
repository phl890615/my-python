a=str(input())
z=0
a=a.lower()
x=["a","b","d","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in a:
  if i in x:
    z+=1
print(z)


-------------
a=str(input())
z=0
for i in a:
  x=str.isalpha(i)
  if x==True:
    z+=1
print(z)

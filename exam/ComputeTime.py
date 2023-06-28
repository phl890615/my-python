h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())
g1=h1*60+m1
if h2==0:
 g2=24*60+m2
else:
 g2=h2*60+m2
if g1-g2>0:
 print(24*60-(g1-g2))
else:
 print(g2-g1)


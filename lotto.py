import random
s = set()
while len(s) < 6:
    r = random.randint(1,49)
    s.add(r)
print(sorted(s,reverse=True))


d1 = { 'a': 100, 'b': 200, 'c': 300 }
d2 = { 'b': 200, 'd': 400, 'a': 300 }
for i,j in d2.items():
    if i in d1.keys():
        d1[i] += j
    else:
        d1[i] = j
print(d1)


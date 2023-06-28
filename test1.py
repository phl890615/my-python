x = [[95,100,100],[86,90,75],[98,98,96],[78,90,80],[70,68,72]]
t = []
for i in range(3):
    subtotal = 0
    for j in range(5):
        subtotal += x[j][i]
    t.append(subtotal/5)
print(t)

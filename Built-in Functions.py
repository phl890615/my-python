data = [['John',40,174,65],['Amy',28,165,44],['Jessie', 32,158,45],['Trump',55,190,100],['Joe',60,180,50]]
for i in range(5):
    for j in range(3,2,-1):
        a = data[i][j]
        b = data[i][j-1]
        BMI = a/(b/100)**2
        BMI = round(BMI,2)
        data[i].append(BMI)
c=sorted(data,key=lambda data:data[4],reverse=True)
print(c)

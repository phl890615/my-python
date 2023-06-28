phonebook =[['張三','0912123456'], ['李四','0933123456'],['王五','0921123456']]
while True:
    s = input('輸入姓名:')
    for x in phonebook:
        if s == x[0]:
            print(x[1])
        break
    else:
        print('查無此人')

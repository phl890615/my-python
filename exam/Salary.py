a=int(input())
if a<=60:
    print((a*75)/1)
elif a<75:
    print(((a-60)*75*1.25+60*75)/1)
else:
    print(((a-75)*75*1.75+15*1.25*75+60*75)/1)

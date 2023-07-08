a = eval(input("請輸入三角形邊長:"))
b = eval(input("請輸入三角形邊長:"))
c = eval(input("請輸入三角形邊長:"))
if a<b+c and b<a+c and c<a+b:
    if a == b == c:
        print("正三角形")
    elif a == b or a == c or b == c:
        print("等腰三角形")
    else:
        print("一般三角形")
else:
    print("非三角形")

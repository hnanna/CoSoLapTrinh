a=float(input(""))
b=float(input(""))
c=float(input(""))
if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
    if a*a==b*b+c*c or b*b==a*a+c*c or c*c==b*b+c*c:
        print("Tam giac vuong")
    elif a==b or b==c or c==a:
        print("Tam giac deu")
    else:
        print("Tam giac loai khac")
else:
    print("Khong hop le")
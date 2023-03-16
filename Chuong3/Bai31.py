a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if (a+b)>c and (a+c)>b and (b+c)>a :
    import math
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Dien tich=",(round(s,3)),sep='')
else:
    print("Khong hop le")
a=int(input("M1="))
b=int(input("M2="))
c=int(input("M3="))
tt=int(input("S="))
if tt>=0:
    if tt<=100:
        x=tt*a
        print("Phai tra=",x,sep='')
    if 101<=tt<=150:
        x=tt*b
        print("Phai tra=",x,sep='')
    if tt>=151:
        x=tt*c
        print("Phai tra=",x,sep='')
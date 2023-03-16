x=float(input("x="))
y=float(input("y="))
ch=input("Phep toan:")
if ch=="+":
    print(x,"+",y,"=",str(x+y),sep='')
if ch=="-":
    print(x,"-",y,"=",str(x-y),sep='')
if ch=="*":
    print(x,"*",y,"=",str(x*y),sep='')
if ch=="/":
    print(x,"/",y,"=",str(x/y),sep='')
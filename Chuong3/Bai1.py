a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
min=max=a
if max<b:
    max=b;
if max<c:
    max=c;
print("SLN=",max,sep='')
if min>b:
    min=b;
if min>c:
    min=c;
print("SNN=",min,sep='')
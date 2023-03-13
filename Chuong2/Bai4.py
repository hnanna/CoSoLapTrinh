a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
S=float((a+b+c)/2)
import math
Dt=float(S*(S-a)*(S-b)*(S-c))
print("Dien tich=", math.sqrt(Dt))
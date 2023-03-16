tt=float(input("Tieu thu="))
if 1<=tt<=100:
    x=tt*550+0.1
elif 101<=tt<=150:
    x=tt*750+0.1
elif 151<=tt<=200:
    x=tt*950+0.1
elif tt>=201:
    x=tt*1350+0.1
print("Phai tra=",x,sep='')
        
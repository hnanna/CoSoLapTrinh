service=6
salary=400
bonus=0
if service<5:
    if salary<500:
        bonus=100
    else:
        bonus=200
else:
    bonus=700
print("Bonus amount: ", bonus)
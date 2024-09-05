is_hot= True
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("wear warm clothes")
else:
    print("It's a lovely day")
print("enjoy your day")

good_credit = False
if good_credit:
    print("price of house is $900000")
else:
    print("price of house is $800000")


price=1000000
with_good_credit= False
if with_good_credit:
    down_payment=0.1*price
else:
    down_payment=0.2*price
print(f"Down payment: ${down_payment}")
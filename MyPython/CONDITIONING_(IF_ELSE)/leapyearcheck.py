y=int(input("Enter Year: "))
if y%4==0 or y%100==0 or y%400==0:
    print("It is a Leap Year")
else:
    print("It is not a leap year")    
    


y=int(input("Enter Year: "))
if y%100==0:
    if y%400==0:
        print("Leap Year")
    else:
        print("Not a Leap year")
elif y%4==0:
    print("It is a leap year")
else:
    print("Not a leap year")                
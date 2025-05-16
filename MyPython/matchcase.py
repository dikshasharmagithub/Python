dayno=int(input("Enter a number: "))
match dayno:
    case 0:
        print("monday")
    case 1:
        print("Tuesday")
    case 2:
        print("wednesday")
    case 3:
        print("Thursday")
    case 4:
        print("Friday")
    case 5:
        print("saturday")
    case 6:
        print("Sunday")
    case _:
        print("Invalid number Entered!")                            
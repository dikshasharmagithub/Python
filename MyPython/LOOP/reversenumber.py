d=int(input("Enter number: "))
reverse=0
r=0
while d>0:
    r=d%10
    reverse= (reverse*10)+r
    d=d//10
print("The reverse number is: ",reverse)    
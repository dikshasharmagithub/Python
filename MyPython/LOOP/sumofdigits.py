d=int(input("Enter the Number: "))
r=0
sum=0
while d>0:
    r=(d%10)
    sum=sum+r
    d=d//10

print("The sum of digits are: ", sum)    
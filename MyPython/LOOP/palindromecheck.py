d=int(input("Enter a Number: "))
n=d
rev=0
while d>0:
    r=d%10
    rev= (rev*10)+r
    d=d//10
if n==rev:
    print("It is a Palindrome")
else:
    print("Entered number is not a palindrome")    
    

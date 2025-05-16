n=int(input("Enter a number: "))
rev=0
while n>0:
    r=n%10
    rev=(rev*10)+r
    n= n//10
print("Reverse Number is: ", rev)    


n=10
sum=0
while n<100:
    sum= sum+n
    print(sum)
    n=n+2

print(sum)    
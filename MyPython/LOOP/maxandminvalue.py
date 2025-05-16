n=5
print("Enter",n, "numbers: ")
i=0
max= float('-inf')
min= float('inf')

while i<n:
    a=int(input())
    i=i+1
    if a>max:
        max=a
    if a<min:
        min=a
print("Max= ",max)   
print("Min= ",min)        

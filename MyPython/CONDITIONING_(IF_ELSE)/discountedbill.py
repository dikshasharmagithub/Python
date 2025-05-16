import math
a= int(input("Enter Bill generated: "))
if a <=1000:
    a-=a*0.1
elif a >=1000 and a<= 5000:
    a-=a*0.15
elif a>= 5000 and a<= 10000:
    a-=a*0.2
else:
    a-=a*0.25
print("PAY: ",a)            

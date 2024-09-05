names = ["diksha"," nakul", "shriya", "swati", "srishti"]
names[2]= "john"
print(names[0])
print(names[-2])
print(names[2:])
print(names[:])
print(len(names))

numbers = [3,6,2,8,4,10,18]
max = numbers[0]
for number in numbers:
    if number > max:
        max= number
print(max)        
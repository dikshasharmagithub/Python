number=[1,2,3,4]
number.append(18)
print(number)

number.insert(0, 10)
print(number)

number.remove(3)
print(number)

number.pop()
print(number)

number.reverse()
print(number)

print(number.index(4))

print(50 in number)

number.sort()
print(number)

number2= number.copy()
number.append(100)
print(number2)

number.clear()
print(number)


numbers=[1,1,2,2,3,3,4,4]
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)        


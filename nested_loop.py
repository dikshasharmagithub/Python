for x in range(4):
    for y in range(3):
        print(f'{x}, {y}')

print("*****")
print("**")
print("*****")
print("**")
print("**")
print("**")  

print("another method")

numbers = [5,2,5,2,2]
for x_count in numbers:
    print('x'* x_count)

print("another way")

numbers = [1,1,1,1,8]
for x_count in numbers:
    output=''
    for count in range(x_count):
        output += 'x'
    print(output)

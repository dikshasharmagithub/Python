d1='Diksha Nakul'
print(d1[2])

print(d1[1:9:2])

print(d1[ : : 2])

print(d1[-7:-2:1])

print(d1[ : ])


d2=d1[10:5:-1]
print(d2)

d2=d1[-12:-7:1]
print(d2)

d2=d1[ : :-1]
print(d2)

print(d1[2:3])

print(d1)

count=0
for x in range(len(d1)):
    count+=1
    print(d1[x], end='')
print(count)


for x in d1:
    print(x,":", end='')
print('')    




for x in [2,5,6,-7]:
    print(x, end='')

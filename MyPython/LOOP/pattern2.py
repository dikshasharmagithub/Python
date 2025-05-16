for i in range(1,6):
    for j in range(1,6):
        if i<=j:
            print('* ', end=' ')
    print(' ')        


for i in range(1,6):
    for j in range(1,6-(i-1)):
            print('8 ', end=' ')
    print(' ')      


for i in range(1,6):
    print('8 '*(6-i))
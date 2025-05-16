a='     Diksha'
b=a.lstrip()
print(b)

a='++++Nakul'
b=a.lstrip('+')
print(b)

a='Shriya______'
b=a.rstrip('_')
print(b)

a='Asha    '
b=a.rstrip()
print(b)

a='+++Virat++'
b=a.strip('+')
print(b)

a='+_Diksha and Nakul=k = +)'
b=a.strip('+_= +k)')
print(b)
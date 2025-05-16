a=18
b=123456789123456789123456789
print(a)
print(b)

import sys
print(sys.getsizeof(a))
print(sys.getsizeof(b))

d=18
print(id(d))
d=3
print(id(d))

a=1
b=1.1
c=-1.1E2
d=-1.11e-2
print(a,b,c,d)

x=True
y= False
print(x,y)

print(type(y))

print(int(y))

a=19
b=4
print(b>a)

c=9+8j
print(type(c))
print(c)

d=complex(4.9,7.9)
print(d)

e=complex(10)
print(e)

e=12.5_7
print(e)

f= 1.234e-4
print(f)

name = 'kaki'
name1 ="kaki"
name2 ='"kaki"'
print(name,name1,name2)

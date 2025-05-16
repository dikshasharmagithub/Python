a='D-i-k-s-h-a'
b=a.replace('-','_')
print(b)

b=a.replace('-','*',2)
print(b)

b=a.replace('n','a')
print(b)

b='Nakul '
c=a.join(b)
print(c)

d='>'
e=d.join(b)
print(e)

f='Diksha nakul shriya'
g=f.split()
print(g)

f='Diksha-nakul-shriya'
g=f.split()
print(g)

f='Diksha-nakul-shriya-asha-swati'
g=f.split('-',2)
print(g)


g=f.rsplit('-',2)
print(g)

h='My name is Diksha \n i am learning python \n i am liking python'
i=h.splitlines()
print(i)


h='My name is Diksha \ i am learning python \ i am liking python'
i=h.splitlines(keepends=True)
print(i)
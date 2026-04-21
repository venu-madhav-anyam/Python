lst = ['a', 'b', 'c', 'd']

d2 = d1={}

for i in lst:
    d1[i] = {}
    d1 = d1[i]

print(d2)
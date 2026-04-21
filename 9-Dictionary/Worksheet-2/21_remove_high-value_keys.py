d = {'a': 5, 'b': 10, 'c': 15, 'd': 'big'}
limit = 10

for k in list(d.keys()):
    if isinstance(d[k],(int,float)) and d[k] > limit:
        del d[k]

print(d)
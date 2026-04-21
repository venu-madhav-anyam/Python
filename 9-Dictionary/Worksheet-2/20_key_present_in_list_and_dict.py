d = {'a': 100, 'b': 200, 'c': 300}
lst = ['b', 'c', 'd']

res = {}

for i in d:
    if i in lst:
        res[i] = d[i]
print(res)
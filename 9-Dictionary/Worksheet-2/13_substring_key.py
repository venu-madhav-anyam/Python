d = {'hello': 1, 'world': 2, 'hell': 3}
substring = 'hell'
lis = []
for i in d:
    if substring in i:
        lis.append(i)

print(lis)
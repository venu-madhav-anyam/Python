d = {'sun': 1, 'sunny': 2, 'rain': 3}
substring = 'sun'
res = {k: v for k, v in d.items() if substring not in k}

print(res)


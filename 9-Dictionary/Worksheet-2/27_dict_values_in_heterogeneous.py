d = {'x': 100, 'y': 'hello', 'z': 200}
res = {k: v for k,v in d.items() if isinstance(v,int)}
print(res)
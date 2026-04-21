odes = {'alpha': 'ok', 'beta': 'wait'}
new_labels = {'alpha': 'red', 'beta': 'blue'}

res = dict(zip(new_labels.values(),map(lambda x:x,odes.values())))
print(res)
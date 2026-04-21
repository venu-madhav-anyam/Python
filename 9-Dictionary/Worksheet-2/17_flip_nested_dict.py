d = {'x': {'p': 1}, 'y': {'q': 2}}

res = {inner_key: {outer_key: d[outer_key][inner_key]}
       for outer_key in d
       for inner_key in d[outer_key]}

print(res)
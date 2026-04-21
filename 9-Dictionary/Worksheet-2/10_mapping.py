names = ['Alice', 'Bob', 'Eve'] 
seats = [5, 12, 8]

merged = dict(zip(names,map(lambda x : x,seats)))
print(merged)


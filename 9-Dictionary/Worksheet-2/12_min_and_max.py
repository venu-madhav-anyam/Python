valuables = {'ring': 5, 'necklace': 9, 'watch': 2}

maxi = max(valuables,key=valuables.get)
mini = min(valuables,key=valuables.get)

print("Max: ",maxi)
print("Min: ",mini)
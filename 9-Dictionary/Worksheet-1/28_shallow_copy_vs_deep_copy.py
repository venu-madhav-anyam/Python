import copy

original = {'name': 'Alice', 'score': [80,90,75]}

shallow = copy.copy(original)

deep = copy.deepcopy(original)

original['score'].append(100)

print("Original: ",original)
print("Shallow: ",shallow)
print("Deep: ",deep)
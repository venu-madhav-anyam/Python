words = ["education", "python", "sequoia"]
vowels = set('aeiou')

res = [word for word in words if vowels.issubset(set(word.lower()))]
print(res)
str1 = input("Enter a string: ")

vowels = set('aeiouAEIOU')
res = sum(1 for char in str1 if char in vowels)
print(res)
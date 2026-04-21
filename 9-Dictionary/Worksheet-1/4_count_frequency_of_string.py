#from collections import Counter
str1 = input("Enter a string: ")
#d = dict(Counter(str1))
d = {}

for i in str1:
    d[i] = str1.count(i)
    
print(d)
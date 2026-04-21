"""
Description: Identify and print elements that occur more than once in a tuple.
Spotting duplicates in sequences is common in data cleaning and interviews.
Input: t = (2, 4, 6, 2, 8, 4, 6, 2)
Output: 2, 4, 6
"""

tup1 = tuple(map(int, input("Enter members in tuple: ").split()))

print(tuple(set(elem for elem in tup1 if tup1.count(elem) > 1)))

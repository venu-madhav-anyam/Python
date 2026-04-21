"""
Description: Find the index of a specified value in a tuple using the index() method.
Locating elements within tuples is crucial for data lookup and manipulation.
Input: t = ("cat", "dog", "rabbit"), Find: "dog"
Output: 1
"""

tup1 = tuple(map(str, input("Enter members in tuple: ").split()))
find = input("Enter value: ")

print(tup1.index(find))

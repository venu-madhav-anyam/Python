"""
Description: Count how many times a particular value occurs in a tuple.
Element frequency counting is useful for analytics and validation tasks.
Input: t = (1, 2, 3, 2, 2, 4), Count: 2
Output: 3
"""

tup1 = tuple(map(int, input("Enter members in tuple: ").split()))
find = int(input("Enter value: "))

print(tup1.count(find))

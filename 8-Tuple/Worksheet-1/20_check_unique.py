"""
Description: Check whether all elements in a tuple are unique using set comparison.
Ensures data integrity in scenarios where duplicate values are not allowed.
Input: t = (1, 2, 3, 4, 5)
Output: True
"""

tup1 = tuple(map(int, input("Enter members in tuple: ").split()))
my_set = set(tup1)
tup2 = tuple(my_set)
print(tup1 == tup2)

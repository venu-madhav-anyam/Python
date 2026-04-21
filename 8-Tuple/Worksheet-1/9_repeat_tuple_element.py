"""
Description: Repeat a tuple’s elements multiple times using the * operator.
Tuple repetition is useful for generating predictable patterns or test data.
Input: t = (5, 6)
Output: (5, 6, 5, 6, 5, 6)
"""

tup1 = tuple(map(int, input("Enter members in tuple1: ").split())) * 3
print(tup1)

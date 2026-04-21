"""
Description: Join two tuples together using the + operator and print the result.
Concatenation helps combine multiple tuples into a single sequence for further processing.
Input: t1 = (1, 2), t2 = (3, 4)
Output: (1, 2, 3, 4)
"""

tup1 = tuple(map(int, input("Enter members in tuple1: ").split()))
tup2 = tuple(map(int, input("Enter members in tuple2: ").split()))

print(tup1 + tup2)

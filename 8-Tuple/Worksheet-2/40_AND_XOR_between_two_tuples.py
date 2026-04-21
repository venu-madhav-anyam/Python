"""
Description: Perform elementwise AND and XOR operations between two tuples of integers of equal length.
Elementwise bitwise operations are crucial in low-level data processing and algorithm optimization.
Input: t1 = (1, 2, 3), t2 = (2, 2, 2)
Output: AND: (0, 2, 2), XOR: (3, 0, 1)
"""

from operator import and_, xor

t1 = tuple(map(int, input("Enter elements for tuple1: ").split()))
t2 = tuple(map(int, input("Enter elements for tuple2: ").split()))

res1 = tuple(map(and_, zip(t1, t2)))
res2 = tuple(map(xor, zip(t1, t2)))

print(res1)
print(res2)

"""
Description: Compute the element-wise sum of multiple tuples of equal length.
This exercise teaches how to combine tuples by adding corresponding elements, often used in mathematical and data processing tasks.
Input: t1 = (1, 2, 3, 4), t2 = (3, 5, 2, 1), t3 = (2, 2, 3, 1)
Output: (6, 9, 8, 6)
"""

tup1 = tuple(map(int, input("Enter numbers for tuple1: ").split()))
tup2 = tuple(map(int, input("Enter numbers for tuple2: ").split()))
tup3 = tuple(map(int, input("Enter numbers for tuple3: ").split()))

res = tuple(map(sum, zip(tup1, tup2, tup3)))
print(res)

res = tuple(sum(x) for x in zip(tup1, tup2, tup3))
print(res)

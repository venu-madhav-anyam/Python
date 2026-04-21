"""
Description: Convert a tuple of positive integers into a single integer by concatenating their values.
This is a common data transformation task, often seen in problems that require generating a unique number from a sequence.
Input: t = (1, 2, 3)
Output: 123
"""

tup1 = tuple(map(int, input("Enter numbers for tuple1: ").split()))
# res=0
# for i in tup1:
#     res = (res * 10) + i
# print(res)

res = int("".join([str(i) for i in tup1]))
print(res)

res = int("".join(map(str, tup1)))
print(res)

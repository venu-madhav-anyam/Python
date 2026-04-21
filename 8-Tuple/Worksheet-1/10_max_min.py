"""
Description: Find and print the maximum and minimum values in a tuple of numbers.
This is helpful for statistical analysis and summarizing numeric data in tuples.
Input: t = (11, 3, 55, 21)
Output: 55
3
"""

tup1 = tuple(map(int, input("Enter members in tuple1: ").split()))
print(max(tup1))
print(min(tup1))

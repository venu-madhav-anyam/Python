"""
Description: Sort a list of tuples by the total number of digits across all elements in each tuple.
This requires counting the digits and sorting accordingly, which strengthens comprehension of tuple processing.
Input: lst = [(1, 2), (10, 11), (3, 44)]
Output: [(1, 2), (3, 44), (10, 11)]
"""

lst = [(1, 2), (10, 11, 7), (3, 44)]
sorted_list = sorted(lst, key=lambda x: len(x))
print(sorted_list)

"""
Task: Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample input: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Output: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""

tuples_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

sorted_list = sorted(tuples_list, key=lambda x: x[-1])

print(sorted_list)

"""
Task: Write a Python program to flatten a shallow list.
Sample input: [[1, 2], [3, 4], [5, 6]]
Output: [1, 2, 3, 4, 5, 6]
"""

l1 = [[1, 2], [3, 4], [5, 6]]

flat = []
for sublist in l1:
    for item in sublist:
        flat.append(item)

print(flat)

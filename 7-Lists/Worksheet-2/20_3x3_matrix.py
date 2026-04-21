"""
Task: Write a Python program to create a 3x3 matrix using nested list comprehensions.
Sample input: Rows: 3, Columns: 3
Output: [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
"""

matrix = [[i for j in range(3)] for i in range(3)]
print(matrix)

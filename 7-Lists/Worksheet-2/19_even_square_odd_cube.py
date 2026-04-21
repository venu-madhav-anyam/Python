"""
sTask: Write a Python program to create a list of numbers from 1 to 20, where each number is squared if it is even, and cubed if it is odd.
Sample input: Range: 1 to 20
Output: [1, 4, 27, 16, 125, 36, 343, 64, 729, 100, 1331, 144, 2197, 196, 3375, 256, 4913, 324, 6859, 400]
"""

list = []

for i in range(1, 21):
    if i % 2 == 0:
        list.append(i**2)
    else:
        list.append(i**3)
print(list)

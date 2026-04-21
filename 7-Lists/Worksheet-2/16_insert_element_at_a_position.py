"""
Task: Write a Python program to insert an element at a specified position in a list.
Sample input: [1, 2, 3, 4], element: 5, position: 2
Output: [1, 2, 5, 3, 4]
"""

nums = list(map(int, input("Enter numbers: ").split()))
ele = int(input("Enter element to insert: "))
pos = int(input("Enter position: "))
nums.insert(pos, ele)
print(nums)

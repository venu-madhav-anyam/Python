"""
Task: Write a Python program to remove duplicates from a list.
Sample input: [1, 2, 3, 2, 4, 3, 5]
Output: [1, 2, 3, 4, 5]
"""

nums = list(map(int, input("Enter numbers: ").split()))

s1 = set(nums)
new_list = list(s1)
print(new_list)

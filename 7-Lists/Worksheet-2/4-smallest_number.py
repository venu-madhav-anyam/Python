"""
Task: Write a Python program to get the smallest number from a list.
Sample input: [1, 2, 3, 4, 5]
Output: 1
"""

nums = list(map(int, input("Enter numbers: ").split()))
nums.sort()
print("Smallest = ", nums[0])

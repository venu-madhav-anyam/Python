"""
Task: Write a Python program to get the largest number from a list.
Sample input: [1, 2, 3, 4, 5]
Output: 5
"""

nums = list(map(int, input("Enter numbers: ").split()))
nums.sort(reverse=True)
print("Largest = ", nums[0])

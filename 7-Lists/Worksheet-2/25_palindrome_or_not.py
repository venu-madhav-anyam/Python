"""
Task: Write a Python function to check if a given list is a palindrome (reads the same forwards and backwards).
Sample input: [1, 2, 3, 2, 1]
Output: True
"""

nums = list(map(int, input("Enter numbers: ").split()))
nums1 = nums[::-1]
print("True" if nums == nums1 else "False")

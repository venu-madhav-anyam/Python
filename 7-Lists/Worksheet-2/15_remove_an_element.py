"""
Task: Write a Python program to remove all occurrences of a specific element from a list.
Sample input: [1, 2, 3, 2, 4, 2, 5], element to remove: 2
Output: [1, 3, 4, 5]
"""


nums = list(map(int,input("Enter numbers: ").split()))
element = int(input("Enter an element to remove: "))
nums = [x for x in nums if x != element]
print(nums)

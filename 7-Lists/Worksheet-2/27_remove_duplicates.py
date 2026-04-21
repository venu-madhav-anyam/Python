"""
Task: Write a Python function to remove duplicates from a list while preserving the original order of the remaining elements.
Sample input: [1, 2, 2, 3, 4, 4, 5, 6, 5]
Output: [1, 2, 3, 4, 5, 6]
"""


def remove_duplicates(nums):
    return list(set(nums))


nums = list(map(int, input("Enter numbers: ").split()))
print(remove_duplicates(nums))

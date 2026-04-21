"""
Task: Write a Python function to reverse a list at a specific location.
Sample input: [1, 2, 3, 4, 5, 6], position: 3
Output: [1, 2, 3, 6, 5, 4]
"""


def reverse(lst, index):
    lst[index:] = lst[index:][::-1]
    return lst


nums = list(map(int, input("Enter numbers: ").split()))
pos = int(input("Enter the position: "))
res = reverse(nums, pos)
print(res)

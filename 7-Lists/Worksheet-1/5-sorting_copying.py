"""
5. Sorting and Copying Lists
Log Session a list of numbers: [3, 1, 4, 2, 5].
Sort the list in ascending order.
Sort the list in descending order.
Copy the sorted list to a new list.
Print both lists to verify they are separate copies.
"""

nums = [3, 1, 4, 2, 5]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

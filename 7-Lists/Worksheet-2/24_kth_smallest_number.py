"""
Task: Write a Python function to find the k-th smallest element in a list.
Sample input: [7, 10, 4, 3, 20, 15], k = 3
Output: 7
"""

nums = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter k value: "))
nums.sort()
print(nums[k - 1])

"""
Task: Write a Python program to sum all the items in a list.
Sample input: [1, 2, 3, 4, 5]
Output: 15
"""

nums = list(map(int, input("Enter numbers: ").split()))
sum = 0
for i in nums:
    sum += i
print("Sum = ", sum)

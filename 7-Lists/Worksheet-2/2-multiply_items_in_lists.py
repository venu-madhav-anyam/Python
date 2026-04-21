"""
Task: Write a Python program to multiply all the items in a list.
Sample input: [1, 2, 3, 4]
Output: 24
"""


nums = list(map(int,input("Enter numbers: ").split()))
product = 1
for i in nums:
    product *= i
print("Product = ",product)
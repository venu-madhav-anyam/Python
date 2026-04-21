"""
Description: Iterate through all elements in a tuple and print each one on a separate line.
Looping over tuples is a fundamental skill for data processing and display.
Input: t = ("apple", "banana", "cherry")
Output: apple
banana
cherry
"""


tup = tuple(map(str,input("Enter members: ").split()))

for item in tup:
    print(item)
"""
Description: Check if a specified value exists in a tuple and print the result.
Use the "in" keyword to efficiently search for elements inside a tuple.
Input: my_tuple = ('a', 'b', 'c'), Check: 'b'
Output: True
"""

tup = tuple(map(str, input("Enter members: ").split()))
key = input("Enter element to find: ")
print("True" if key in tup else "False")

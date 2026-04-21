"""
Description: Add an item to a tuple by converting it to a list and back to a tuple.
This demonstrates tuple immutability and how to work around it for adding elements.
Input: t = (1, 2, 3), Add: 4
Output: (1, 2, 3, 4)
"""

tup1 = tuple(map(int, input("Enter members in tuple: ").split()))
ele = int(input("Enter an element to add: "))

my_list = list(tup1)
my_list.append(ele)
print(tuple(my_list))

"""
Description: Remove a specific element from a tuple by converting it to a list and back.
Removing elements from tuples is a common interview question testing immutability handling.
Input: t = (1, 2, 3, 4), Remove: 2
Output: (1, 3, 4)
"""

tup1 = tuple(map(int, input("Enter members in tuple: ").split()))
ele = int(input("Enter an element to remove: "))

my_list = list(tup1)
my_list.remove(ele)
print(tuple(my_list))

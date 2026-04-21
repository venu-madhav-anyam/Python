"""
Description: Convert a tuple of characters to a string and then back to a tuple.
Useful for text manipulation and transitioning between data representations.
Input: t = ('P', 'y', 't', 'h', 'o', 'n')
Output: String: "Python"
Tuple: ('P', 'y', 't', 'h', 'o', 'n')
"""

tup1 = tuple(map(str, input("Enter members in tuple: ").split()))
my_str = "".join(tup1)
print("String: ", my_str)
print(tuple(my_str.split(" ")))

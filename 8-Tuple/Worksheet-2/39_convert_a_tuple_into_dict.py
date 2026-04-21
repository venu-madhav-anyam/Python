"""
Description: Convert a tuple of key-value pairs into a dictionary.
This conversion is fundamental in Python for transitioning between sequence and mapping data types for fast lookups.
Input: t = (('a', 1), ('b', 2), ('c', 3))
Output: {'a': 1, 'b': 2, 'c': 3}
"""

t = (("a", 1), ("b", 2), ("c", 3))

d = dict(t)
print(d)

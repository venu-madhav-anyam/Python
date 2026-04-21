"""
Description: Check if a specified value is present in any of the inner tuples in a tuple of tuples.
This teaches how to search through nested tuples, which is useful in multi-dimensional data handling.
Input: t = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime')), Check: 'White'
Output: True
"""

t = (
    ("Red", "White", "Blue"),
    ("Green", "Pink", "Purple"),
    ("Orange", "Yellow", "Lime"),
)

for ele in t:
    if "White" in t:
        print("True")
else:
    print("False")

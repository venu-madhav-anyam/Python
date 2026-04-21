"""
Description: Sort a tuple of (string, float) pairs by the float value in descending order.
Sorting by a specific field is essential in data analysis and organization, especially when dealing with mixed data types.
Input: t = (('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5'))
Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
"""

t = (("item1", "12.20"), ("item2", "15.10"), ("item3", "24.5"))

sorted_tup = sorted(t, key=lambda x: x[1], reverse=True)
print(sorted_tup)

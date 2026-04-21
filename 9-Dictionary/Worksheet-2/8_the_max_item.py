from collections import Counter
orders = ['latte', 'espresso', 'latte', 'tea', 'espresso', 'latte']
d = dict(Counter(orders))
print(d)
from collections import Counter

marbles = ["red", "blue", "red", "green", "blue", "red"]
freq = Counter(marbles)
min_bags = max(freq.values())
print(min_bags)


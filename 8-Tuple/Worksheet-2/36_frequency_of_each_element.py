"""
Description: Compute the frequency of each element in a tuple and return the result as a dictionary.
Element frequency counting is widely used for data summarization, analytics, and validation tasks.
Input: t = (1, 2, 2, 3, 3, 3)
Output: {1: 1, 2: 2, 3: 3}
"""

t1 = tuple(map(int, input("Enter elements for tuple: ").split()))

# freq_dict = dict(Counter(t1))
# print(freq_dict)

freq_dict = {}
for ele in t1:
    freq_dict[ele] = freq_dict.get(ele, 0) + 1
print(freq_dict)

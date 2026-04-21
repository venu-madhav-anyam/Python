"""
Task: Write a Python function to find the union and intersection of two lists.
Sample input: [1, 2, 3, 4], [3, 4, 5, 6]
Output: Union: [1, 2, 3, 4, 5, 6]
Intersection: [3, 4]
"""


def union(list1, list2):
    return list(set(list1 + list2))


def intersection(list1, list2):
    n_list = list1 + list2
    intersection = []
    for i in n_list:
        if n_list.count(i) > 1 and i not in intersection:
            intersection.append(i)
    return intersection


list1 = list(map(int, input("Enter list1: ").split()))
list2 = list(map(int, input("Enter list2: ").split()))

print("Union: ", union(list1, list2))
print("Intersection: ", intersection(list1, list2))

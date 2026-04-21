"""
6. Joining and Extending Lists
Log Session two lists: list1 = ["a", "b", "c"] and list2 = [1, 2, 3].
Concatenate the two lists into a new list.
Use the extend() method to add list2 to list1.
Print the final lists.
"""

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
new_list = []
list2.extend(list1)
new_list.extend(list2)
print(new_list)

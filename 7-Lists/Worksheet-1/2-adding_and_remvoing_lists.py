"""
2. Adding and Removing Items
Append "orange" to the fruits list.
Insert "mango" at the second position.
Remove "apple" from the list.
Use the pop() method to remove the last item.
Clear the entire list.
"""

fruits = ["apple","banana","cherry"]
fruits.append("orange")
print(fruits)
fruits.insert(2,"mango")
print(fruits)
fruits.remove("apple")
print(fruits)
fruits.pop()
print(fruits)
del fruits
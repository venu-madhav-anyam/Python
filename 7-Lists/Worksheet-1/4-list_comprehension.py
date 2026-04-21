"""
4. List Comprehension
Log Session a list of fruits: "apple", "banana", "cherry", "kiwi", "mango".
Use list comprehension to create a new list containing fruits with the letter "a".
Convert all fruit names to uppercase using list comprehension.
Replace "banana" with "orange" using list comprehension.
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_fruits = [x for x in fruits if "a" in x]
print(new_fruits)
upper = [x.upper() for x in fruits]
print(upper)
new_list = ["orange" if item == "banana" else item for item in fruits]
print(new_list)

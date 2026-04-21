"""
3. Looping Through Lists
Log Session a list of numbers from 1 to 5.
Use a for loop to print each number.
Use a while loop to print each number.
Use list comprehension to create a new list with each number squared.
"""

num = [1, 2, 3, 4, 5]
for i in num:
    print(i)
j = 0
while j < len(num):
    print(num[j])
    j += 1

new_list = [x**2 for x in num]
print(new_list)

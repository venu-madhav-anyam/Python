"""
Task: Write a Python program to find the list of words that are longer than n from a given list of words.
Sample input: ['hello', 'world', 'python', 'is', 'great'], n = 4
Output: ['hello', 'world', 'python', 'great']
"""

l1 = list(map(str, input("Enter the items: ").split()))
n = int(input("Enter n value: "))

new_list = [word for word in l1 if len(word) > n]
print(new_list)

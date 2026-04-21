"""
Task: Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are the same from a given list of strings.
Sample input: ['abc', 'xyz', 'aba', '1221']
Output: 2
"""

strings = list(map(str, input("Enter strings: ").split()))
count = 0
for item in strings:
    if (len(item) >= 2) and (item[0] == item[len(item) - 1]):
        count += 1
print(count)

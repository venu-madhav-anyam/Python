"""
1. Basic Syntax and Data Types
• Concepts: Variables, basic data types (integers, floats, strings), and control structures (ifelse,
loops).
• Task:
• Write a script that reads a text file and counts the occurrence of each word.
• Validation: Verify that the output dictionary correctly represents word counts for
given test files.
"""

file = open("text.txt", "r")

text = file.read()

words = text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
        
print(word_count)

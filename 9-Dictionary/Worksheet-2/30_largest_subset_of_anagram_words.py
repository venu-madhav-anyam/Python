""""
30. Largest Subset of Anagram Words
Given a list of words, find the size of the largest subset where all are anagrams of each other.
Input: words = ['bat', 'tab', 'eat', 'tea', 'tan', 'nat']
Expected Output: 3
"""

students = ['A', 'B']
subjects = ['math', 'sci']
scores = [[90, 80], [85, 95]]

res = {students[i] : dict(zip(subjects,scores[i])) for i in range(len(students))}

print(res)

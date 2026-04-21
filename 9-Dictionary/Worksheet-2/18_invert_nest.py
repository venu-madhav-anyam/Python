d= {'math': {'john': 90, 'jane': 80}, 'science': {'john': 85, 'jane': 95}}

result = {student: {subject: d[subject][student] for subject in d} for student in d['math']}
print(result)
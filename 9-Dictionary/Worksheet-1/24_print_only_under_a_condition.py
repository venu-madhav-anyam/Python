scores = {'math': 75, 'science': 55, 'english': 82}
# [print(i) for i in scores if scores[i] > 60]   
for sub,score in scores.items():
    if score > 60:
        print(sub)
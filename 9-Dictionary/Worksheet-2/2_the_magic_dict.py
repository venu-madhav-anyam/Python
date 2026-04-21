pets = {'Harry': 'owl', 'Ron': 'rat'}
query = 'Hermione'

if not pets.get(query):
    print("No record,maybe try another student!")
else:
    print(pets[query])
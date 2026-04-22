import re

text = "The rain in Spain"

print(re.split("\s", text))  # ['The', 'rain', 'in', 'Spain']
print(re.split("\s", text, 1))  # ['The', 'rain in Spain']

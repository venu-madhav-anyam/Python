import re

text = "The rain in Spain"

match = re.search(r"\bS\w+", text)
print(match.span())   # (12, 17)
print(match.string)   # The rain in Spain
print(match.group())  # Spain
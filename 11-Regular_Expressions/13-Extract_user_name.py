import re
mail = "Nothing@mailcom"

match = re.search(r"(\w+)@(\w+)", mail)

print(match.group(1))
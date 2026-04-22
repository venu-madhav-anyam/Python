import re

text = "The Rain in Spain Falls Mainly"

matches = re.findall(r"\b[A-Z]\w*", text)
print(matches)
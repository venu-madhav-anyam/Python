import re

text = "The bee is flying while the plane is landing"

matches = re.findall(r"\b\w+ing\b", text)
print(matches)
import re

text = "Hello123World45"

digits = re.findall(r"\d+", text)
print(digits)
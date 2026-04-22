import re

text = "Today is 21-04-2026 and tomorrow is 22-04-2026"

dates = re.findall(r"\b\d{2}-\d{2}-\d{4}\b", text)
print(dates)
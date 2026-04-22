import re
text = "The rain in Spain"
matches = re.findall("i", text)
print(matches)  # ['ai', 'ai']
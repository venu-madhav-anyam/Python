import re

text = "The rain in Spain"

match = re.search("i", text)
print("Found at:", match.start())

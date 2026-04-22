import re
text = "The rain in Spain"
result = re.search("^The.*Spain$", text)
print(result)
import re

text = "Regular_Expressions"

count = len(re.findall(r"[aeiouAEIOU]", text))
    
print(count)

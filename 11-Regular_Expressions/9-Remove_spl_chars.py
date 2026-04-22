import re

text = "Hello@# World!! 123"

clean = re.sub(r"[^A-Za-z0-9 ]", "", text)
print(clean)
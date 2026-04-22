import re

num = "9874563210"

if re.match(r"^[6-9]\d{9}$", num):
    print("Valid number")
else:
    print("Invalid number")
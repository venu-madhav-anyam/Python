s1 = input("Enter a string: ")
s2 = ""

for ch in s1:
    if ch.isalnum() or ch.isspace():
        s2 += ch

print(s2)

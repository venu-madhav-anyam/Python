s = input("Enter string: ")
sub = input("Enter substring: ")
ind = s.find(sub)

print(s[0:ind+len(sub)])
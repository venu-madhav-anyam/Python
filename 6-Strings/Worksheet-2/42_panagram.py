s = input("Enter a string: ")
alphabets = "abcdefghijklmnopqrstuvwxyz"
s1 = s.lower()
for ch in alphabets:
    if ch not in s1:
        print("Not a panagram")
        break
else:
    print("Is a panagram")
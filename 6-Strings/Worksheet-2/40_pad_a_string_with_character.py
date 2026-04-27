string = input("Enter a character: ")
Length = int(input("Enter the length: "))
Pad_char = input("Enter the character: ")

str_len = len(string)
diff = Length - str_len
s1 = Pad_char * diff
print(s1+string)
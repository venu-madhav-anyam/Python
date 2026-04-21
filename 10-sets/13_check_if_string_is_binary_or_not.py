def is_binary(s):
    return set(s).issubset({'0','1'})

str1 = input("Enter a string1: ")

print(is_binary(str1))


def is_panagram(s):
    alpha = set('abcdefghijklmnopqrstuvwxyz')
    return alpha.issubset(s.lower())


str1 = input("Enter a string: ")
print(is_panagram(str1))

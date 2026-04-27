s = input("Enter string: ")
sub = input("Enter substring: ")
first = s.find(sub)
second = first + len(sub)

lst=[]
lst.append(first)
lst.append(second)
print(lst)
s = input("Enter string: ")
n = int(input("Enter n value: "))
res = [s[i:i+n] for i in range(0,len(s),n)]
print(res)

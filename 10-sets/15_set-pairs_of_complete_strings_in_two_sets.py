A = {"abc", "defg", "xyz"}
B = {"mnopq", "rstuv", "wxyz"}

count = 0

for s1 in A:
    for s2 in B:
        if len(set(s1+s2)) == 26:
            count += 1

print(count)
l1 = list(map(int,input("Enter list1: ").split()))
l2 = list(map(int,input("Enter list2: ").split()))

new_list = [num for num in l1 if num in l2]
print(new_list)
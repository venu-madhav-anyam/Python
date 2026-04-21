students = {}
n = int(input("Enter number of students: "))

for i in range(n):
    roll_numbers = int(input("Enter roll number: "))
    name = input("Enter name: ")
    students[roll_numbers] = name
print(students)
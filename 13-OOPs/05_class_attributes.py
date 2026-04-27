class Student:
    school_name = "ABC"

    def __init__(self,name):
        self.name = name

s1 = Student("John")
s2 = Student("Jack")

print(s1.school_name)
print(s2.school_name)
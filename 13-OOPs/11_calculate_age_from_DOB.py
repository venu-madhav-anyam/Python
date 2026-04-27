class Person:
    def __init__(self,DOB):
        self.DOB = DOB
    
    def cal_age(self):
        return 2025 - self.DOB
    
a = Person(2000)
print(a.cal_age())
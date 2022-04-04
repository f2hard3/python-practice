class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
    def sum(self):
        return self.korean + self.math + self.english + self.science
    
    def average(self):
        return self.sum() / 4
    
    def show(self):
        print(self.name, self.sum(), self.average(), sep='\t')

students = [
    Student('Yoon', 87, 98, 88, 95),
    Student('Yeon', 87, 98, 88, 95),
    Student('Ku', 87, 98, 88, 95),
    Student('Na', 87, 98, 88, 95),
    Student('Yoon', 87, 98, 88, 95),
    Student('Yoon', 87, 98, 88, 95),
]

print('name', 'sum', 'average', sep='\t')

for student in students:
    student.show()
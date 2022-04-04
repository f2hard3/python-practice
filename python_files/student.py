class Student:
    def __init__(self, name, age):
        print('object is instantiated.')
        self.name = name
        self.age = age
    # def __del__(self):
    #     print('garbage collected.')
    # def output(self):
    #     print(self.name, self.age)
    # def __str__(self):
    #     return f'{self.name}: {self.age}'
    def __eq__(self, other):
        return self.age == other.age and \
                self.name == other.name
    def __ne__(self, other):
        return self.age != other.age
    def __gt__(self, other):
        return self.age > other.age
    def __ge__(self, other):
        return self.age >= other.age
    def __lt__(self, other):
        return self.age < other.age
    def __le__(self, other):
        return self.age <= other.age

student = Student('Park', 37)
# student.output()
# print(str(student))
print(student == student)
print(student != student)
print(student > student)
print(student >= student)
print(student < student)
print(student <= student)

# Bài 7:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split('-')
        return cls(name, int(age))

    def __str__(self):
        return f"Person: {self.name}, {self.age} tuổi"


def bai7():
    print("Bài 7: Lớp Person với class method")
    person = Person.from_string("Nam-20")
    print(person)
    print("-" * 50)
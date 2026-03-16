# Bài 9:
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print(f"{self.name} says: Gau Gau!")


def bai9():
    print("Bài 9: Kế thừa Animal và Dog")
    dog = Dog("Buddy")
    dog.sound()
    print("-" * 50)
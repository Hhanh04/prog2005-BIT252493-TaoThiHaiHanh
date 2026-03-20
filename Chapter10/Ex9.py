class A:
    def __init__(self, x):
        if x < 0:
            raise ValueError("Sai")
        self.x = x

    def __str__(self):
        return str(self.x)

    def tang(self):
        self.x += 1

    @classmethod
    def hello(cls):
        print("Hello")

    @staticmethod
    def check(x):
        return x >= 0

    def __eq__(self, other):
        return self.x == other.x


class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def __str__(self):
        return str(self.x) + " " + str(self.y)


b = B(5, 10)
print(b)
b.tang()
print(b)
print(B.check(3))
B.hello()
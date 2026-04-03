class Book:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    def get_price(self):
        return self.__price
    def set_price(self, price):
        self.__price = price
book1 = Book("Python", 50000)
print("Giá sách:", book1.get_price())
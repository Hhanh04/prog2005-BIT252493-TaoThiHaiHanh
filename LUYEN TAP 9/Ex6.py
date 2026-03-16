# Bài 6:
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError("Giá phải lớn hơn 0")

    def __str__(self):
        return f"Product có giá: {self._price}"


def bai6():
    print("Bài 6: Lớp Product")
    product = Product(100000)
    print(product)
    product.price = 150000
    print(f"Giá mới: {product.price}")
    print("-" * 50)
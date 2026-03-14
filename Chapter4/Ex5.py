class Product:
    def __init__(self, price=0):
        self._price = 0
        self.price = price  # Sử dụng setter
    
    @property
    def price(self):
        """Getter"""
        return self._price
    
    @price.setter
    def price(self, value):
        """Setter với validation"""
        if value <= 0:
            raise ValueError("Giá phải lớn hơn 0!")
        self._price = value
    
    def __str__(self):
        return f"Product - Giá: {self._price} VND"

# Test
try:
    product1 = Product(100000)
    print(product1)
    
    # Test setter
    product1.price = 150000
    print(product1)
    
    # Test validation
    product1.price = -50  # Sẽ raise error
except ValueError as e:
    print(f"Lỗi: {e}")

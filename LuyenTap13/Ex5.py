class Flower:
    def __init__(self, color):
        self._color = color
    def get_color(self):
        return self._color
    def set_color(self, new_color):
        self._color = new_color
my_flower = Flower("Red")
print(f"Màu sắc ban đầu: {my_flower.get_color()}")
my_flower.set_color("Yellow")
print(f"Màu sắc sau khi thay đổi: {my_flower.get_color()}")
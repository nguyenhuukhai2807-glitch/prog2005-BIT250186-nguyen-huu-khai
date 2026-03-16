class Product:
    def __init__(self, price):
        self._price = price   # thuộc tính ban đầu

    # Getter
    @property
    def price(self):
        return self._price

# Setter
@price.setter
def price(self, value):
    if value > 0:
        self._price = value
    else:
        print("Giá phải lớn hơn 0")

    # Hàm hiển thị thông tin
    def __str__(self):
        return f"Price: {self._price}"
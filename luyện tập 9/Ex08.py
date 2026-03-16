class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Nạp chồng toán tử +
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    #hiển thị vector
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Tạo hai vector
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Cộng hai vector
v3 = v1 + v2

#In kết quả
print(v1)
print(v2)
print(v3)

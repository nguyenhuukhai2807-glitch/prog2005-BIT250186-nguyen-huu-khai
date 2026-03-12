import random

# Nhập kích thước ma trận
m = int(input("Nhập số hàng (M): "))
n = int(input("Nhập số cột (N): "))

# Khởi tạo ma trận với giá trị ngẫu nhiên
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(random.randint(1, 100))
    matrix.append(row)

# Hiển thị ma trận
print("Ma trận:")
for row in matrix:
    print(row)

# Hiển thị hàng theo yêu cầu
hang = int(input("Nhập số hàng muốn xem: "))
if 1 <= hang <= m:
    print("Hàng", hang, ":", matrix[hang - 1])
else:
    print("Hàng không hợp lệ")

# Hiển thị cột theo yêu cầu
cot = int(input("Nhập số cột muốn xem: "))
if 1 <= cot <= n:
    print("Cột", cot, ":")
    for i in range(m):
        print(matrix[i][cot - 1])
else:
    print("Cột không hợp lệ")

# Tìm giá trị lớn nhất trong ma trận
max_value = matrix[0][0]
for i in range(m):
    for j in range(n):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]

print("Giá trị lớn nhất trong ma trận:", max_value)
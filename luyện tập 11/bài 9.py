def input_matrix(rows, cols, name):
    matrix = []
    print(f"\nNhập ma trận {name}:")

    for i in range(rows):
        row = []
        for j in range(cols):
            value = input(f"{name}[{i}][{j}] = ").strip()

            # Kiểm tra nhập rỗng
            if value == "":
                print("Lỗi: Giá trị không được để trống!")
                exit()

            # Kiểm tra có phải số không
            try:
                num = int(value)
            except:
                print("Lỗi: Giá trị phải là số nguyên!")
                exit()

            row.append(num)
        matrix.append(row)

    return matrix


# Nhập kích thước
rows = int(input("Nhập số hàng: "))
cols = int(input("Nhập số cột: "))

# Nhập 2 ma trận
A = input_matrix(rows, cols, "A")
B = input_matrix(rows, cols, "B")

# Cộng ma trận
C = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    C.append(row)

# In kết quả
print("\nMa trận tổng:")
for row in C:
    print("\t".join(map(str, row)))
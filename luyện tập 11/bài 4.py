import math

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# 1. Khởi tạo danh sách
lst = [1, 2, 3, 4, 5]
print("Danh sách ban đầu:", lst)

# 2. Thêm phần tử
x = int(input("\nNhập phần tử muốn thêm: "))
lst.append(x)
print("Danh sách sau khi thêm:", lst)

# 3. Nhập k và đếm số lần xuất hiện
k = int(input("\nNhập giá trị k: "))
count = lst.count(k)
print(f"Số lần xuất hiện của {k}: {count}")

# 4. Tính tổng số nguyên tố
prime_sum = sum(num for num in lst if is_prime(num))
print("Tổng các số nguyên tố:", prime_sum)

# 5. Sắp xếp danh sách
lst.sort()
print("Danh sách sau khi sắp xếp:", lst)

# 6. Xóa danh sách
lst.clear()
print("Danh sách sau khi xóa:", lst)
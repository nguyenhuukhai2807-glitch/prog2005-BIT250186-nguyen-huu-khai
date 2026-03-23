# Danh sách 5 chuỗi đã được sắp xếp (giả sử từ Bài 9)
strings = ["An", "Binh", "Chi", "Dung", "Hanh"]

# Hàm Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # trả về vị trí
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # không tìm thấy


# Nhập chuỗi cần tìm
target = input("Nhập chuỗi cần tìm: ").strip()

if target == "":
    print("Lỗi: Không được để trống!")
    exit()

# Tìm kiếm
result = binary_search(strings, target)

# In kết quả
if result != -1:
    print(f"Tìm thấy '{target}' tại vị trí index: {result}")
else:
    print(f"Không tìm thấy '{target}' trong danh sách")
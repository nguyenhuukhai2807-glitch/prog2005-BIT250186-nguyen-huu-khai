# Nhập 5 chuỗi
arr = []
for i in range(5):
    s = input(f"Nhập chuỗi {i+1}: ")
    arr.append(s)

n = len(arr)

# Bubble sort giảm dần theo độ dài
for i in range(n - 1):
    for j in range(n - i - 1):
        if len(arr[j]) < len(arr[j + 1]):
            # hoán đổi
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

        # In từng bước
        print(f"Bước i={i}, j={j}: {arr}")

print("Kết quả cuối:", arr)
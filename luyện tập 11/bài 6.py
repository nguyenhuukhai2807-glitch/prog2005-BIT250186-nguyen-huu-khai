students = {}

n = int(input("Nhập số người: "))

for i in range(n):
    name = input(f"\nNhập tên người thứ {i + 1}: ").strip()

    if name == "":
        print("Lỗi: Tên không được để trống!")
        exit()

    age_input = input("Nhập tuổi: ").strip()

    if age_input == "":
        print("Lỗi: Tuổi không được để trống!")
        exit()

    try:
        age = int(age_input)
    except:
        print("Lỗi: Tuổi phải là số!")
        exit()

    students[name] = age

# Tính tuổi trung bình
total_age = sum(students.values())
average_age = total_age / len(students)

# In kết quả
print("\nDanh sách:")
for name, age in students.items():
    print(f"{name}: {age}")

print(f"\nTuổi trung bình: {average_age:.2f}")
import math

# Nhập hai số
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))

# Lũy thừa
luy_thua = a ** b

# Căn bậc 2 của a
can_bac_2 = math.sqrt(a)

# Chia lấy phần nguyên
chia_nguyen = a // b

# Chia lấy phần dư
chia_du = a % b

# Làm tròn số a
lam_tron = round(a)

# In kết quả
print("Lũy thừa:", luy_thua)
print("Căn bậc 2 của a:", can_bac_2)
print("Chia lấy phần nguyên:", chia_nguyen)
print("Chia lấy phần dư:", chia_du)
print("Làm tròn số a:", lam_tron)
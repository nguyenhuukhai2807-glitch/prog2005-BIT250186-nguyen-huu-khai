# Nhập chuỗi
chuoi = input("Nhập chuỗi: ")

# Đảo ngược chuỗi
chuoi_dao = ""

for i in range(len(chuoi) - 1, -1, -1):
    chuoi_dao += chuoi[i]

# In kết quả
print("Chuỗi đảo ngược là:", chuoi_dao)
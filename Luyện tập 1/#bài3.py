# Nhập số từ 1 đến 9
n = int(input("Nhập một số từ 1 đến 9: "))

#Kiểm tra điều kiện
if 1 <= n <= 9:
    print(f"Bảng cửu chương của {n}:")
    for i in range(1, 10):
        print(f"{n} x {i} = {n*i}")
else:
    print("Vui lòng nhập số trong khoảng từ 1 đến 9")

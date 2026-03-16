#Nhập số từ người dùng
number = input("Nhập một số: ")

#Khởi tạo biến tổng
total = 0

#Duyêt từng chữ số và cộng vaò tổng
for digit in number:
    total += int(digit)

#Hiển thị kết quả
print("Tổng các chữ số là:", total)
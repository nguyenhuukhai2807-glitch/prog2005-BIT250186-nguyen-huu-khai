# Nhập tên người dùng
name = input("Nhập tên: ")

# Chuẩn hóa tên
name = name.strip()      # bỏ khoảng trắng ở đầu và cuối
name = name.title()      # viết hoa chữ cái đầu mỗi từ

# Hiển thị kết quả
print("Tên sau khi chuẩn hóa:", name)

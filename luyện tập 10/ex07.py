mat_khau_dung = "python123"

while True:
    mat_khau = input("Nhập mật khẩu: ")

    if mat_khau == mat_khau_dung:
        print("Đăng nhập thành công!")
        break
    else:
        print("Sai mật khẩu, vui lòng thử lại.")
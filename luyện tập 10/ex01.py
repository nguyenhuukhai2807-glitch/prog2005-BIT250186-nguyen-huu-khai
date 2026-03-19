def lay_ten_file(duong_dan):
    return duong_dan.split("\\")[-1]

# Ví dụ
path = "d:\\music\\muabui.mp3"
print(lay_ten_file(path))  # muabui.mp3
def lay_ten_bai_hat(duong_dan):
    ten_file = duong_dan.split("\\")[-1]
    return ten_file.split(".")[0]

# Ví dụ
path = "d:\\music\\muabui.mp3"
print(lay_ten_bai_hat(path))  # muabui
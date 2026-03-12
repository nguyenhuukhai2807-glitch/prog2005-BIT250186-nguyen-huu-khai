class Student:
    def __int__(self, ten, diem):
        self.ten = ten
        self.diem = diem

# Khởi tạo 2 đối tượng
sv1 = Student("Khải", 8.5)
sv2 = Student("Bình", 7.8)

#In thông tin
print("Sinh viên 1:", sv1.ten, "_", sv1.diem)
print("Sinh viên 2:", sv2.ten, "_", sv2.diem)

